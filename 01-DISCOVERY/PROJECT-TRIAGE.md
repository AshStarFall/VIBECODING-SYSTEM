# Project Triage and Retrieval

Classify before loading guidance. A project can match multiple types; mark only the relevant ones.

| Signal | Load |
| --- | --- |
| Static, content, SEO, landing, docs site | `07-STACK-PLAYBOOKS/WEB-AND-FRONTEND.md`; design/accessibility; SEO/performance resources |
| Authenticated web product or API | Web plus backend/database playbooks; security and operations |
| Android/mobile, offline, device permissions | `07-STACK-PLAYBOOKS/ANDROID-MOBILE.md`; mobile security and device testing |
| Windows/macOS/Linux desktop | `07-STACK-PLAYBOOKS/DESKTOP.md`; installer, signing, update, local-data security |
| LLM, agent, RAG, model/provider integration | `07-STACK-PLAYBOOKS/AI-APPLICATIONS.md`; AI security, evals, privacy, cost/latency |
| Payments, health, identity, children, sensitive data, multi-tenant access | Threat model and security review early; ask about jurisdiction/obligations; raise human review |
| User uploads, media, real-time, background jobs | Include storage, validation, quotas, lifecycle, abuse, and failure/retry planning |
| Prototype, one-off script, low-risk change | Lightweight scope and only the relevant quality checks |

## Intake dimensions

Capture the user/problem, primary user, platform, core workflow, data and trust boundaries, integrations, constraints, deployment/maintenance owner, success measure, and unknowns. Use [`QUESTION-FRAMEWORK.md`](QUESTION-FRAMEWORK.md); do not ask every possible question by default.

## Select resources

1. Search [`../12-RESOURCES/README.md`](../12-RESOURCES/README.md) by capability, not by popularity.
2. Prefer the official docs and a small number of complementary tools.
3. Verify current status, compatibility, license, permissions, security, pricing, and operational cost from primary sources.
4. State why selected and what simpler alternative was considered. Skip resources that add no measurable value.

Output: project classification, applicable documents to load, highest-impact questions/assumptions, risk flags, and the next artifact. Do not generate a broad tool shopping list.