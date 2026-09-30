"""Refresh the public Shields.io badge from GitHub's 14-day traffic API."""

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


def build_badge(views: int, unique_visitors: int, updated_at: str) -> dict[str, object]:
    return {
        "schemaVersion": 1,
        "label": "repo views (14d)",
        "message": f"{views:,} views, {unique_visitors:,} unique",
        "color": "blue",
        "views": views,
        "uniqueVisitors": unique_visitors,
        "windowDays": WINDOW_DAYS,
        "updatedAt": updated_at,
    }


def main() -> int:
    token = os.environ.get("TRAFFIC_TOKEN", "").strip()
    repository = os.environ.get("GITHUB_REPOSITORY", "AshStarFall/VIBECODING-SYSTEM")
    if not token:
        print("REPO_TRAFFIC_TOKEN is not configured; leaving the badge unchanged.")
        return 0

    request = Request(
        f"https://api.github.com/repos/{repository}/traffic/views?per=day",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": API_VERSION,
            "User-Agent": "VibeCoding-System-traffic-badge",
        },
    )

    try:
        with urlopen(request, timeout=30) as response:
            traffic = json.load(response)
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
    except (URLError, TimeoutError) as error:
        print(f"Could not reach GitHub traffic API: {error}", file=sys.stderr)
        return 1

    views = int(traffic.get("count", 0))
    unique_visitors = int(traffic.get("uniques", 0))
    updated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    OUTPUT.write_text(
        json.dumps(build_badge(views, unique_visitors, updated_at), indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Updated repository traffic snapshot ({WINDOW_DAYS}-day window).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())