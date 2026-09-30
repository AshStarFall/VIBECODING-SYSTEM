---
name: verify-slice
description: Verify a code change against its acceptance criteria and actual runtime behavior.
---

# Verify a Slice

1. Restate the behavior changed and its acceptance criterion.
2. Run the narrowest relevant test or reproduction first; inspect the exact failure if it fails.
3. Run appropriate type, lint, build, integration, or end-to-end checks based on touched boundaries.
4. When UI or platform behavior is involved, launch the app and verify the user path in a browser/device if available.
5. Check failure/empty/loading behavior and nearby regressions in proportion to the change.
6. Report commands and outcomes accurately. Label unavailable checks and remaining risks; never infer success from code inspection alone.