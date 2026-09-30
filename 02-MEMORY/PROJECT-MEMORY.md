# Project Memory

Keep durable project knowledge in the project repository, not in an assumed model memory. Store only information that will change future decisions or prevent repeated investigation.

## Recommended files

- `PROJECT-CONTEXT.md`: product, users, stack, current status, key constraints, entry commands.
- `docs/decisions/NNNN-title.md`: accepted architectural/product decisions and consequences.
- `docs/lessons-learned.md`: verified pitfalls and remedies, with scope and date.
- `docs/operations/`: runbooks, deployment, backup, recovery, and ownership.
- `SESSION-HANDOFF.md` (temporary): current task state, evidence, next check; prune after resolution.

## Memory rules

- Record why a choice was made, not just what was chosen. Include alternatives and conditions that would reopen it.
- Separate current facts from hypotheses and stale notes. Date volatile details such as versions, prices, provider limits, and policies.
- Never persist secrets, raw credentials, or unnecessary personal data.
- Prefer a concise index that points to authoritative docs over copied duplicate instructions.
- Review for contradictions when implementation or policy changes; archive obsolete decisions with a replacement link.

See [`../13-TEMPLATES/ADR.md`](../13-TEMPLATES/ADR.md) for decision records.