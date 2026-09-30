---
name: project-kickoff
description: Discover, scope, and specify a new application or substantial feature before implementation.
---

# Project Kickoff

## Inputs

User idea, target repository (if any), constraints, and any existing references or designs.

## Steps

1. Read project instructions and inspect the repository state. If no repo exists, identify the intended platform and working location.
2. Classify with [`../../01-DISCOVERY/PROJECT-TRIAGE.md`](../../01-DISCOVERY/PROJECT-TRIAGE.md); load only relevant playbooks.
3. Ask a small batch of high-impact questions using [`../../01-DISCOVERY/QUESTION-FRAMEWORK.md`](../../01-DISCOVERY/QUESTION-FRAMEWORK.md). State reversible assumptions.
4. Draft a PRD and technical plan using [`../../13-TEMPLATES/PRD.md`](../../13-TEMPLATES/PRD.md) and [`../../13-TEMPLATES/TRD.md`](../../13-TEMPLATES/TRD.md).
5. Define v1 acceptance criteria, explicit non-goals, risk flags, and unresolved decisions.
6. Present the artifacts and pause for approval before substantial implementation if scope or architecture is material.

## Output

Project classification, selected context, PRD, technical plan, and open questions. Do not fabricate validation evidence or write implementation code during discovery unless the user expressly asks for a small exploratory prototype.