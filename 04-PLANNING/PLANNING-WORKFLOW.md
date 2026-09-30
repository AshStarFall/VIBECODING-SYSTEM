# Planning Workflow

Create only the artifacts needed to make the next decisions safe and clear. For a material build, the default set is a PRD, a technical plan, and a small task sequence.

## PRD

Describe the problem, users, jobs, goals/non-goals, v1 scope, key flows, constraints, risks, and measurable acceptance criteria. Requirements should be testable and prioritized. Keep ideas outside v1 visible as deferred rather than quietly expanding scope.

## Technical plan

Document stack and rationale, system boundaries, major data entities, trust boundaries, API/event contracts, migrations, deployment, observability, failure modes, and decisions still open. Do not prematurely specify every class or endpoint implementation.

## Slice the implementation

Break work into vertical slices that can be run or demonstrated. For each slice record: user-visible outcome, prerequisites, files/subsystems likely involved, acceptance test, security/data implications, and rollback strategy if needed. Sequence high-risk assumptions early.

## Approval gates

Show the PRD and technical plan before substantial implementation when requirements or architecture are material. Seek explicit approval before data deletion/migration, paid services, public releases, or production changes. For small contained tasks, agree on a concise scope and proceed.

Use [`../13-TEMPLATES/PRD.md`](../13-TEMPLATES/PRD.md), [`../13-TEMPLATES/TRD.md`](../13-TEMPLATES/TRD.md), and [`../13-TEMPLATES/TASK-PLAN.md`](../13-TEMPLATES/TASK-PLAN.md).