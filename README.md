# VibeCoding-System

An AI-native engineering playbook for turning a software idea into a tested, secure, maintainable release. It is an operating system for project work, not a bundle of copied prompts or an unfiltered list of links.

## Start here

Give your coding agent your project idea and this repository URL. Ask it to read [`AGENTS.md`](AGENTS.md), then follow [`00-CORE/VIBECODING-PROTOCOL.md`](00-CORE/VIBECODING-PROTOCOL.md). The agent should classify the project, load only relevant playbooks, ask high-impact questions, create project specifications, and wait for approval before implementation when scope is material.

```text
I want to build: <your idea>
Use https://github.com/AshStarFall/VIBECODING-SYSTEM as the engineering system.
Read AGENTS.md and follow the project protocol. Start with discovery; do not code until
the requirements, acceptance criteria, and first implementation slice are agreed.
```

## The workflow

```text
Idea -> classify -> clarify -> validate the problem -> specify -> design/architect
     -> slice the work -> implement in verified increments -> audit -> release -> learn
```

The system optimizes for useful outcomes, not code volume. It requires evidence for important claims, explicit assumptions, small reversible changes, and validation against the running product where possible. It does not require every project to use every tool or phase at maximum depth.

## Navigate by need

| Need | Start with |
| --- | --- |
| Give an agent durable operating rules | [`AGENTS.md`](AGENTS.md), [`00-CORE/SYSTEM-RULES.md`](00-CORE/SYSTEM-RULES.md) |
| Triage an idea and decide what to load | [`01-DISCOVERY/PROJECT-TRIAGE.md`](01-DISCOVERY/PROJECT-TRIAGE.md) |
| Ask better questions and expose ambiguity | [`01-DISCOVERY/QUESTION-FRAMEWORK.md`](01-DISCOVERY/QUESTION-FRAMEWORK.md) |
| Keep context and token use lean | [`03-CONTEXT/CONTEXT-POLICY.md`](03-CONTEXT/CONTEXT-POLICY.md) |
| Write requirements and architecture | [`04-PLANNING/PLANNING-WORKFLOW.md`](04-PLANNING/PLANNING-WORKFLOW.md), [`13-TEMPLATES/`](13-TEMPLATES/) |
| Use role prompts or repeatable skills | [`05-AGENTS/`](05-AGENTS/), [`06-SKILLS/`](06-SKILLS/) |
| Choose platform-specific guidance | [`07-STACK-PLAYBOOKS/README.md`](07-STACK-PLAYBOOKS/README.md) |
| Improve product and avoid generic output | [`08-PRODUCT-DESIGN/`](08-PRODUCT-DESIGN/) |
| Address security, testing, and release readiness | [`09-SECURITY/SECURITY-GATES.md`](09-SECURITY/SECURITY-GATES.md), [`10-QUALITY/QUALITY-GATES.md`](10-QUALITY/QUALITY-GATES.md), [`11-DELIVERY/RELEASE-PLAYBOOK.md`](11-DELIVERY/RELEASE-PLAYBOOK.md) |
| Find and evaluate a tool/reference | [`12-RESOURCES/README.md`](12-RESOURCES/README.md) |

## Project types covered

Websites and web apps, full-stack services, Android/mobile apps, desktop apps, AI/LLM products, data-backed applications, and other software. Load only applicable platform guidance. The stack defaults in a playbook are suggestions, never requirements.

## Design principles

- Discover the user, real problem, desired outcome, and constraints before selecting a stack.
- Keep an explicit distinction between requirements, decisions, assumptions, and open questions.
- Prefer the smallest complete vertical slice; build schema/contracts before dependent layers.
- Treat security, privacy, accessibility, and operations as design concerns, not end-of-project decorations.
- Use tests and live behavior to verify claims; report what was and was not checked.
- Select tools by fit, risk, maintenance, setup cost, and context cost. Do not add tools to look sophisticated.
- Never copy third-party prompts, skills, code, screenshots, or documentation wholesale without permission and license review.

## Repository map

- `00-CORE`: system rules, agent context, and lifecycle protocol.
- `01-DISCOVERY` to `04-PLANNING`: intake, requirements, context use, specifications, and architecture.
- `05-AGENTS` and `06-SKILLS`: copy-ready role prompts and portable task workflows.
- `07-STACK-PLAYBOOKS` to `11-DELIVERY`: platform, product/design, security, quality, and operations.
- `12-RESOURCES`: deduplicated discovery index and resource-card standard.
- `13-TEMPLATES`: project artifacts to copy into a new project.
- `14-MAINTENANCE`: keep this system and its recommendations current.

## Resource handling

The catalog combines resources supplied in `REPOS.txt` and `Resorce.txt`, consolidates repeated entries, and adds broad categories identified in the notes. It records selection guidance rather than mirroring external repositories. Links are discovery leads, not endorsements or current compatibility guarantees. Verify activity, official documentation, security posture, license, pricing, and platform fit before adoption. No supplied screenshot archive or third-party source content is redistributed here.

## Use with any coding agent

`AGENTS.md` is the canonical portable entrypoint. For systems that support project instructions, skills, or slash commands, adapt these documents to that system and keep a single source of truth. Do not assume that a skill is installed just because this repository links to it.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). Keep guidance concise, tool-neutral where possible, and linked to a decision or quality outcome. See [`14-MAINTENANCE/RESOURCE-REVIEW.md`](14-MAINTENANCE/RESOURCE-REVIEW.md) before adding or refreshing references.