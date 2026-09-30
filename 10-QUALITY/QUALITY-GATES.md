# Quality Gates

Choose checks based on changed boundaries and user risk. A green unit-test suite does not prove the product works end to end.

## Change-level loop

- Reproduce the issue or identify the intended behavior.
- Run the narrowest targeted test immediately after the change.
- Run relevant formatter/linter/type checks and tests for adjacent contracts.
- Inspect the diff for scope, accidental files/secrets, and unintended behavior.

## Project-level evidence

- Unit tests for meaningful logic and boundary conditions.
- Integration/contract tests for persistence, APIs, authentication, and external dependencies.
- End-to-end tests for critical user journeys on the actual platform.
- Accessibility and responsive checks for user-facing interfaces.
- Security, performance, and reliability checks proportionate to risk.
- Build/package/install checks for the intended release artifact.

## Completion report

For each important acceptance criterion, report evidence and result. Name failed, skipped, or unavailable checks and why. Verify actual runtime behavior where possible. Include known defects, migration concerns, and follow-up risk; do not use “done” to conceal gaps.