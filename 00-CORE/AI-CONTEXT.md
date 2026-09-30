# AI Context Contract

Give an agent the smallest context that can support the next decision or change.

## Always provide

- The requested user outcome and who needs it.
- The target repository, branch/state, and relevant project instructions.
- Constraints, known facts, acceptance criteria, and what must not change.
- Relevant files, failing behavior, reproducible steps, and available validation commands.

## Load only when relevant

Select from discovery, planning, stack playbooks, design, security, quality, delivery, and resource catalogs. Include only the applicable project type, high-risk concerns, and current implementation slice. Prefer links or file paths over pasting entire documents when the agent can read them.

## Keep context clean

- Label unverified claims and distinguish decisions from proposals.
- Summarize previous work as current state, open questions, decisions, and next check; omit stale reasoning.
- Replace large logs with the relevant excerpt and command. Preserve the full output path if needed.
- Do not paste credentials, private user data, or unrelated source code.
- Ask the agent to state what it inspected and what evidence supports a consequential conclusion.

## Handoff format

```text
Goal:
Current state:
Relevant paths/evidence:
Constraints / do not change:
Acceptance checks:
Open questions / assumptions:
Next action:
```