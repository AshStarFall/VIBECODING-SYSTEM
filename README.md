<div align="center">
     <img src="assets/VibeCoding-System_logo_unique_boot.gif" width="220" alt="VibeCoding-System animated logo">
     <h1>VibeCoding-System</h1>
     <p><strong>A free, reusable engineering kit for building software with AI agents.</strong></p>
     <p>From a rough idea to a specified, usable, accessible, tested, and supportable release.</p>
     <p>
          <a href="https://github.com/AshStarFall/VIBECODING-SYSTEM/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/AshStarFall/VIBECODING-SYSTEM?style=flat-square&label=stars"></a>
          <a href="https://github.com/AshStarFall/VIBECODING-SYSTEM/network/members"><img alt="GitHub forks" src="https://img.shields.io/github/forks/AshStarFall/VIBECODING-SYSTEM?style=flat-square&label=forks"></a>
          <a href="https://github.com/AshStarFall/VIBECODING-SYSTEM/watchers"><img alt="GitHub watchers" src="https://img.shields.io/github/watchers/AshStarFall/VIBECODING-SYSTEM?style=flat-square&label=watchers"></a>
          <a href="https://github.com/AshStarFall/VIBECODING-SYSTEM/blob/main/LICENSE"><img alt="MIT License" src="https://img.shields.io/github/license/AshStarFall/VIBECODING-SYSTEM?style=flat-square"></a>
          <a href="https://github.com/AshStarFall/VIBECODING-SYSTEM/commits/main"><img alt="Latest commit" src="https://img.shields.io/github/last-commit/AshStarFall/VIBECODING-SYSTEM?style=flat-square"></a>
     </p>
</div>

---

VibeCoding-System is an AI-native engineering playbook for turning a software idea into a tested, secure, maintainable release. It works as an operating system for project work: a set of rules, workflows, role prompts, playbooks, quality gates, and templates that a coding agent (or a human) can follow from first idea to supportable release. It is not a bundle of copied prompts or an unfiltered list of links.

> **Educational use:** This free kit is made for vibecoders and people learning to build software with AI. It provides general guidance and is not legal, security, or compliance advice. Read the full [disclaimer](DISCLAIMER.md).

## Who this is for

- **Vibecoders and learners** who build with AI assistants and want a structure that prevents rework, insecure code, and unfinished products.
- **Solo builders and small teams** who want a lightweight, repeatable process without heavy tooling.
- **Anyone directing a coding agent** who wants consistent behavior: clarify first, plan, build in small verified steps, and report honestly.

## What you get

- **Agent operating rules** that any coding agent can follow (`AGENTS.md`, `00-CORE/`).
- **Discovery and question frameworks** that expose ambiguity before code is written.
- **Planning workflow and templates** for requirements, architecture, and task slices.
- **Role prompts and portable skills** for repeatable tasks.
- **Stack playbooks** for web, full-stack, mobile, desktop, and AI/LLM projects.
- **Product design and experience audits** covering usability, likability, accessibility, and feedback.
- **Security, quality, and release gates** so "done" means verified, not assumed.
- **A curated resource index** with a selection standard for tools and references.
- **Maintenance guidance** to keep the system itself current.

## Start here

Give your coding agent your project idea and this repository URL. Ask it to read [`AGENTS.md`](AGENTS.md), then follow [`00-CORE/VIBECODING-PROTOCOL.md`](00-CORE/VIBECODING-PROTOCOL.md). The agent should classify the project, load only relevant playbooks, ask high-impact questions, create project specifications, and wait for approval before implementation when scope is material.

<details open>
<summary><strong>Copy-ready kickoff prompt</strong></summary>

```text
I want to build: <your idea>
Use https://github.com/AshStarFall/VIBECODING-SYSTEM as the engineering system.
Read AGENTS.md and follow 00-CORE/VIBECODING-PROTOCOL.md. Inspect my project
repository and local instructions. First classify the project, load only relevant
guidance, ask questions that could change scope or safety, and draft project-specific
requirements, technical plan, and task slices. Show me the files and wait for approval
before substantial implementation. Build in small, verified increments and report
actual checks and remaining risks.
```

</details>

> An AI with repository access can create project-specific files in your project repo. A chat without file access can draft their contents for you to save yourself. This kit does not automatically install frameworks or guarantee a professional outcome.

## Quick start

1. Open your coding agent inside your **project** repository (or an empty folder for a new project).
2. Paste the kickoff prompt above with your idea filled in.
3. Answer the agent's clarifying questions.
4. Review the generated requirements, technical plan, and task slices. Approve or change them.
5. Let the agent build in small increments, and check the reported test results and remaining risks at each step.

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
| Keep project memory and decisions organized | [`02-MEMORY/`](02-MEMORY/) |
| Keep context and token use lean | [`03-CONTEXT/CONTEXT-POLICY.md`](03-CONTEXT/CONTEXT-POLICY.md) |
| Write requirements and architecture | [`04-PLANNING/PLANNING-WORKFLOW.md`](04-PLANNING/PLANNING-WORKFLOW.md), [`13-TEMPLATES/`](13-TEMPLATES/) |
| Use role prompts or repeatable skills | [`05-AGENTS/`](05-AGENTS/), [`06-SKILLS/`](06-SKILLS/) |
| Choose platform-specific guidance | [`07-STACK-PLAYBOOKS/README.md`](07-STACK-PLAYBOOKS/README.md) |
| Audit user experience, likability, usability, accessibility, and feedback | [`08-PRODUCT-DESIGN/EXPERIENCE-AUDIT.md`](08-PRODUCT-DESIGN/EXPERIENCE-AUDIT.md), [`13-TEMPLATES/EXPERIENCE-AUDIT.md`](13-TEMPLATES/EXPERIENCE-AUDIT.md) |
| Address security, testing, and release readiness | [`09-SECURITY/SECURITY-GATES.md`](09-SECURITY/SECURITY-GATES.md), [`10-QUALITY/QUALITY-GATES.md`](10-QUALITY/QUALITY-GATES.md), [`11-DELIVERY/RELEASE-PLAYBOOK.md`](11-DELIVERY/RELEASE-PLAYBOOK.md) |
| Find and evaluate a tool or reference | [`12-RESOURCES/README.md`](12-RESOURCES/README.md) |
| Keep this system current | [`14-MAINTENANCE/RESOURCE-REVIEW.md`](14-MAINTENANCE/RESOURCE-REVIEW.md) |

## Project types covered

Websites and web apps, full-stack services, Android/mobile apps, desktop apps, AI/LLM products, data-backed applications, and other software. Load only applicable platform guidance. The stack defaults in a playbook are suggestions, never requirements.

## Design principles

- Discover the user, real problem, desired outcome, and constraints before selecting a stack.
- Keep an explicit distinction between requirements, decisions, assumptions, and open questions.
- Prefer the smallest complete vertical slice; build schema and contracts before dependent layers.
- Treat security, privacy, accessibility, and operations as design concerns, not end-of-project decorations.
- Use tests and live behavior to verify claims; report what was and was not checked.
- Select tools by fit, risk, maintenance, setup cost, and context cost. Do not add tools to look sophisticated.
- Never copy third-party prompts, skills, code, screenshots, or documentation wholesale without permission and license review.

## Repository map

| Path | Purpose |
| --- | --- |
| `AGENTS.md` | Canonical, portable entrypoint for coding agents. |
| `00-CORE` | System rules, agent context, and lifecycle protocol. |
| `01-DISCOVERY` | Project triage, intake, and question framework. |
| `02-MEMORY` | Guidance for keeping durable project memory, decisions, and assumptions. |
| `03-CONTEXT` | Context and token-use policy. |
| `04-PLANNING` | Requirements, specifications, architecture, and task slicing. |
| `05-AGENTS` | Copy-ready role prompts. |
| `06-SKILLS` | Portable, repeatable task workflows. |
| `07-STACK-PLAYBOOKS` | Platform- and stack-specific guidance. |
| `08-PRODUCT-DESIGN` | Product design and experience audits. |
| `09-SECURITY` | Security gates and practices. |
| `10-QUALITY` | Testing and quality gates. |
| `11-DELIVERY` | Release and operations playbooks. |
| `12-RESOURCES` | Deduplicated discovery index and resource-card standard. |
| `13-TEMPLATES` | Project artifacts to copy into a new project. |
| `14-MAINTENANCE` | Keeping this system and its recommendations current. |
| `assets` | Logo and other repository media. |
| `data` | Supporting data files, such as aggregate traffic data for the repository badge. |
| `scripts` | Helper scripts used by repository automation. |
| `.github/workflows` | GitHub Actions workflows, including the daily traffic snapshot. |
| `CONTRIBUTING.md`, `DISCLAIMER.md`, `SECURITY.md`, `LICENSE` | Contribution, educational-use, security, and license information. |

## Resource handling

The resource catalog consolidates repeated entries and records selection guidance rather than mirroring external repositories. Links are discovery leads, not endorsements or current compatibility guarantees. Verify activity, official documentation, security posture, license, pricing, and platform fit before adoption. No third-party source content or screenshot archive is redistributed here.

## Use with any coding agent

`AGENTS.md` is the canonical portable entrypoint. For systems that support project instructions, skills, or slash commands, adapt these documents to that system and keep a single source of truth. Do not assume that a skill is installed just because this repository links to it.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). Keep guidance concise, tool-neutral where possible, and linked to a decision or quality outcome. See [`14-MAINTENANCE/RESOURCE-REVIEW.md`](14-MAINTENANCE/RESOURCE-REVIEW.md) before adding or refreshing references.

## Usage and project activity

The badges above show public GitHub signals: stars, forks, watchers, license, and latest commit. They are not counts of people who installed the kit or used it in an AI conversation.

This repository also includes an optional [traffic workflow](.github/workflows/repo-traffic.yml) that keeps a cumulative count of repository page views. GitHub only exposes the latest 14 days of traffic, so history that expired before the workflow first ran cannot be recovered, and the total is marked as partial in that case. The count measures page-view events, not distinct people, installs, or AI-kit usage.

To enable it, create a fine-grained token limited to this repository with **Administration: read**, then save it under **Settings → Secrets and variables → Actions** as `REPO_TRAFFIC_TOKEN`. The workflow uses that secret only to read GitHub's aggregate traffic API. A separate `GITHUB_TOKEN` publishes the aggregate JSON badge data. GitHub can delay scheduled runs. Never put the token in a file or prompt. Maintainers can also inspect GitHub → Insights → Traffic directly.

## License and security

Original materials in this repository are offered under the [MIT License](LICENSE). External projects and linked materials retain their own licenses and terms. See [DISCLAIMER.md](DISCLAIMER.md) for educational-use limits and [SECURITY.md](SECURITY.md) for private vulnerability reporting guidance.
