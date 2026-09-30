# Context and Cost Policy

The goal is sufficient context for a correct next action, not the shortest prompt at any cost. Rework, tool calls, and unverified assumptions can cost more than reading a relevant file.

## Retrieval sequence

1. User request and explicit constraints.
2. Target project instructions, current state, and relevant source/tests.
3. The owning abstraction and one nearby call site or test.
4. Relevant system playbook only when it changes a decision.
5. Official documentation or external resources for version-sensitive facts.

## Keep context useful

- Search narrowly, read the caller and owner, and expand only when evidence requires it.
- Request focused tool output; summarize long logs with error, cause, and path to full output.
- Reuse a short handoff after interruptions: goal, changes, checks, open questions, next action.
- Do not load all skills, all resources, or unrelated project files into every session.
- Batch independent reads when tooling allows. Avoid repeated reads of unchanged content.
- Use a cheaper/smaller model only when the task's ambiguity, risk, and reasoning demands permit; verify its output.

## Stop and compact

Compact context when the agent repeats exploration, carries stale hypotheses, or loses the next check. Preserve decisions, evidence, exact relevant paths, validation status, and remaining risk; discard unneeded transcript detail. Never compress away uncertainty or failed checks.

## Resource cost note

For optional tools, consider setup time, credentials, runtime footprint, maintenance, output volume, and model/context consumption. Add an integration only when the expected improvement outweighs these costs.