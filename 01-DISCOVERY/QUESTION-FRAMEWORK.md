# Question Framework

Ask questions in a short batch, prioritizing decisions that change what gets built. Offer concrete options where useful and allow “other / not sure.” Avoid asking questions already answered by the repository or user.

## High-value questions

- Who has the problem, and what do they do today?
- What is the one end-to-end outcome the first version must deliver?
- Which users/platforms are in scope now? Which are explicitly later?
- What data is collected, where does it come from, and who may read/change/delete it?
- Which integrations, accounts, devices, or external services are required?
- Are there existing repos, stack constraints, designs, domain names, budgets, deadlines, or deployment accounts?
- What would make v1 useful enough to keep using? How can that be observed?
- What must never happen (data loss, public exposure, charges, downtime, unsafe advice)?

## Ambiguity check

Before planning, make sure each requirement has an actor, trigger, expected behavior, and observable acceptance condition. Resolve conflicting goals, undefined terms, unclear ownership, unspecified failure behavior, hidden platform assumptions, and missing data/security constraints. Label each item as confirmed, assumed, deferred, or open.

## Question budget

Ask at most a few questions per turn unless the user requests a workshop. Group related choices. If unanswered, proceed only when the assumption is low-risk and reversible; state it and invite correction. Do not block progress on preferences that can be decided during a reviewable design step.