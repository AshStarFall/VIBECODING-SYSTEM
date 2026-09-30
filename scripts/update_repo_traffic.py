"""Maintain a cumulative public badge from GitHub's rolling traffic API."""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


API_VERSION = "2022-11-28"
WINDOW_DAYS = 14
OUTPUT = Path(__file__).resolve().parents[1] / "data" / "repo-traffic.json"


def parse_daily_views(traffic: dict[str, object], created_at: str) -> dict[str, int]:
    created_day = datetime.fromisoformat(created_at.replace("Z", "+00:00")).date()
    rows = traffic.get("views", [])
    if not isinstance(rows, list):
        raise ValueError("GitHub traffic response did not contain a views list")

    daily_views: dict[str, int] = {}
    for row in rows:
        if not isinstance(row, dict):
            continue
        viewed_day = datetime.fromisoformat(
            str(row["timestamp"]).replace("Z", "+00:00")
        ).date()
        if viewed_day >= created_day:
            daily_views[viewed_day.isoformat()] = int(row["count"])
    return daily_views


def update_totals(
    state: dict[str, object],
    daily_views: dict[str, int],
    repository_created_at: str,
    updated_at: str,
) -> dict[str, object]:
    created_day = datetime.fromisoformat(
        repository_created_at.replace("Z", "+00:00")
    ).date()
    today = datetime.fromisoformat(updated_at.replace("Z", "+00:00")).date()
    total = state.get("allTimeViews")

    if total is None:
        history_complete = (today - created_day).days < WINDOW_DAYS
        tracked_from = created_day.isoformat() if history_complete else min(
            daily_views, default=today.isoformat()
        )
        total = sum(daily_views.values())
    else:
        total = int(total)
        history_complete = bool(state.get("historyComplete", False))
        tracked_from = str(state.get("trackingStartedAt") or created_day.isoformat())

        previous_updated = state.get("updatedAt")
        if previous_updated:
            previous_day = datetime.fromisoformat(
                str(previous_updated).replace("Z", "+00:00")
            ).date()
            if (today - previous_day).days >= WINDOW_DAYS:
                history_complete = False

        previous_daily = state.get("recentDailyViews", {})
        if not isinstance(previous_daily, dict):
            previous_daily = {}
        for viewed_day, count in daily_views.items():
            total += count - int(previous_daily.get(viewed_day, 0))

    return {
        "schemaVersion": 2,
        "label": "repo views",
        "message": (
            f"{int(total):,} since creation"
            if history_complete
            else f"{int(total):,} tracked (partial)"
        ),
        "color": "blue" if history_complete else "orange",
        "allTimeViews": int(total),
        "trackingStartedAt": tracked_from,
        "historyComplete": history_complete,
        "recentDailyViews": daily_views,
        "updatedAt": updated_at,
    }


def request_json(url: str, token: str) -> dict[str, object]:
    request = Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": API_VERSION,
            "User-Agent": "VibeCoding-System-traffic-badge",
        },
    )
    with urlopen(request, timeout=30) as response:
        result = json.load(response)
    if not isinstance(result, dict):
        raise ValueError("GitHub API returned an unexpected response")
    return result


def main() -> int:
    token = os.environ.get("TRAFFIC_TOKEN", "").strip()
    repository = os.environ.get("GITHUB_REPOSITORY", "AshStarFall/VIBECODING-SYSTEM")
    if not token:
        print("REPO_TRAFFIC_TOKEN is not configured; leaving the badge unchanged.")
        return 0

    try:
        repository_info = request_json(f"https://api.github.com/repos/{repository}", token)
        traffic = request_json(
            f"https://api.github.com/repos/{repository}/traffic/views?per=day", token
        )
        created_at = str(repository_info["created_at"])
        updated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
        daily_views = parse_daily_views(traffic, created_at)
        state = json.loads(OUTPUT.read_text(encoding="utf-8")) if OUTPUT.exists() else {}
        badge = update_totals(state, daily_views, created_at, updated_at)
    except HTTPError as error:
        if error.code in (401, 403):
            print(
                "GitHub denied traffic access. Check that REPO_TRAFFIC_TOKEN is "
                "a fine-grained token with Administration: read for this repository.",
                file=sys.stderr,
            )
            return 1
        print(f"GitHub traffic API returned HTTP {error.code}.", file=sys.stderr)
        return 1
    except (URLError, TimeoutError, ValueError, KeyError, json.JSONDecodeError) as error:
        print(f"Could not reach GitHub traffic API: {error}", file=sys.stderr)
        return 1

    OUTPUT.write_text(
        json.dumps(badge, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        f"Updated cumulative repository views: {badge['allTimeViews']} "
        f"(history_complete={badge['historyComplete']})."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())