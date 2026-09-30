# Project Protocol

Scale this protocol to the risk and size of the work. A tiny script does not need a full PRD; a payments app, AI product, or mobile app needs more discovery and release planning.

## 0. Orient

Read target-repository instructions, check working-tree state, identify runtime and existing conventions, and confirm the user's requested boundary. Preserve in-progress work.

## 1. Classify and retrieve

Use [`../01-DISCOVERY/PROJECT-TRIAGE.md`](../01-DISCOVERY/PROJECT-TRIAGE.md). Record platform, users, data sensitivity, integrations, deployment model, and risk. Load only matching playbooks; use [`../03-CONTEXT/CONTEXT-POLICY.md`](../03-CONTEXT/CONTEXT-POLICY.md) to control context.

## 2. Discover

Ask the minimum questions that can change the v1 scope, platform, access model, data handling, or release constraints. Separate must-haves from ideas. Identify the user problem and how to test it. If a decision is low-risk and reversible, state a reasonable assumption.

## 3. Specify

For material projects, create PRD and TRD using [`../13-TEMPLATES/PRD.md`](../13-TEMPLATES/PRD.md) and [`../13-TEMPLATES/TRD.md`](../13-TEMPLATES/TRD.md). Include user flows, non-goals, acceptance criteria, data/security constraints, architecture, and open decisions. Present them and pause for approval before substantial implementation.

## 4. Design and plan

For interfaces, create a project-specific visual and interaction brief before UI implementation. For data-backed work, design schema and migrations before dependent APIs. Decompose the approved scope into small vertical slices with testable outcomes, dependencies, rollback/migration notes, and a demo path.

## 5. Build incrementally

For each slice: inspect the owner and nearby tests; state a local hypothesis and focused check; make the smallest coherent change; run that check immediately; repair or re-route based on the result. Keep docs/contracts current as behavior changes. Avoid parallel agents unless explicitly requested and safe.

## 6. Verify and audit

Use [`../10-QUALITY/QUALITY-GATES.md`](../10-QUALITY/QUALITY-GATES.md) and [`../09-SECURITY/SECURITY-GATES.md`](../09-SECURITY/SECURITY-GATES.md). Test the actual user path on the target platform where possible. Review accessibility, error handling, performance, privacy, observability, backups, and recovery according to risk.

## 7. Release and learn

Follow [`../11-DELIVERY/RELEASE-PLAYBOOK.md`](../11-DELIVERY/RELEASE-PLAYBOOK.md). Require explicit authorization before pushing, deploying, changing production data, or incurring cost. Record release evidence, known issues, rollback steps, and lessons in the target project.

## Stop conditions

Pause for user input when a decision is irreversible, affects real users/data, involves legal/security uncertainty, changes the agreed scope, or cannot be safely inferred. Otherwise proceed with a documented reversible assumption.