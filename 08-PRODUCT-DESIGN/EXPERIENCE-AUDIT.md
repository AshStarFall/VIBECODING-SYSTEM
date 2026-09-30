# User Experience Audit System

Use this process before a meaningful public launch, after a major journey change, or when evidence shows users are struggling. Scale it to risk: a small prototype may need a walkthrough and a few user sessions; a high-impact service needs representative research, a formal accessibility evaluation, privacy review, and accountable sign-off.

Copy [`../13-TEMPLATES/EXPERIENCE-AUDIT.md`](../13-TEMPLATES/EXPERIENCE-AUDIT.md) into the project for each audit. Relevant source material and tools are indexed in [`../12-RESOURCES/README.md`](../12-RESOURCES/README.md).

## Keep the dimensions separate

| Dimension | Question | Useful evidence |
| --- | --- | --- |
| Desirability / likability | Does this solve a meaningful problem in a way users value, trust, and want to return to? | User stories, observed preference, satisfaction comments, retention/return behavior, reasons for abandonment |
| Usability | Can intended users complete important tasks effectively, efficiently, and with acceptable satisfaction in their real context? | Task completion, critical errors, recovery, observed friction, time-on-task where meaningful, post-task ease/confidence |
| Accessibility and inclusion | Can people with different abilities, devices, input modes, assistive technologies, languages, and contexts perceive, understand, and operate the product? | Applicable conformance evaluation, manual AT/keyboard checks, disabled-user sessions, platform-specific accessibility checks |
| Trust and safety | Do users understand what the product does with their data and can they recover from mistakes or unsafe/unexpected outcomes? | Comprehension checks, permission/consent behavior, reversibility, complaints, privacy/security findings |
| Product quality in use | Does the experience work reliably under actual network, device, content, and account conditions? | Real-device/browser checks, telemetry, support issues, errors, performance, offline/degraded behavior |

ISO 9241-11 defines usability in terms of effectiveness, efficiency, and satisfaction in a specified context of use. It is a paid standard and describes concepts rather than prescribing a complete method. WCAG is an accessibility standard; passing WCAG alone does not show that a product is useful or satisfying.

## Audit workflow

### 1. Set the scope

- Name the product/version, release decision, audit owner, date, environments, supported platforms, and target audiences.
- Select one or more critical end-to-end journeys. Include new and returning users, key account states, and failure/recovery paths where relevant.
- State the standard/target level and applicable legal obligations. WCAG 2.2 AA is a common web target, not universal legal advice; verify jurisdiction and sector rules. For native apps, include the platform's own guidance and assistive technologies.
- Record what is not being evaluated. Never label a partial review “fully accessible” or “production-ready.”

### 2. Collect existing evidence safely

Review support contacts, complaints, survey responses, search/no-result data, funnel drop-offs, task analytics, performance/errors, prior studies, and feature requests. Check for selection bias and instrumentation gaps. Do not treat clickstream or session replay as a substitute for talking with users.

For research or in-product feedback, explain purpose and recording, obtain informed consent where required, collect the minimum data, restrict access, set retention/deletion rules, redact identifiers, and check vendor data terms. Do not record sensitive fields or expose raw user sessions in reports without a clear lawful need and safeguards.

### 3. Inspect the actual journey

Run the journey on the supported desktop/mobile/device configurations. Start from the user's real entry point and go through success, empty, loading, denied, error, cancellation, and recovery states. Record observable behavior, not just opinions about screenshots. Capture route/build/device/browser details and sanitize evidence.

Use a heuristic review as a fast inspection aid: visibility of system status, familiar language, user control, consistency, error prevention/recovery, recognition over recall, efficiency, focused design, help, and documentation. Heuristics find plausible risks; they are not proof that users fail. NN/g recommends independent evaluators where possible because one reviewer misses issues; treat group size as a resource-dependent tactic, not a release criterion.

### 4. Test with representative users

- Form a research question before writing tasks. Recruit actual or likely users, including people who use assistive technology or have access needs relevant to the audience.
- Use neutral, realistic, goal-based tasks. Ask participants to think aloud when appropriate; observe before helping, and distinguish problems in the interface from problems in the prototype/setup.
- Include assistive technology, keyboard-only, zoom/reflow, touch, and other relevant modalities. Participants' own devices and settings can reveal issues a lab configuration misses.
- Use enough sessions to expose recurring patterns for the decision at hand. Small formative samples help discover issues but are not statistically representative; report the sample and limits.
- Ask open questions about value, confidence, frustration, perceived control, trust, and whether users would choose to use the experience again. Do not prompt praise or equate a high NPS with good usability.

### 5. Evaluate accessibility with multiple methods

For web content, use WCAG 2.2 and the W3C WCAG-EM 2 process when a structured conformance evaluation is needed: scope the product, explore key views and functionality, select a representative sample when exhaustive review is infeasible, evaluate, and report. Include the entire critical process, not only the home page. WCAG-EM is a methodology, not an extra conformance standard.

Combine automated checks on rendered states with manual evaluation. At minimum for critical web flows, inspect keyboard order/visible focus/no traps, names/roles/states, labels and errors, screen-reader announcements, zoom/reflow, contrast, text resizing/spacing, motion preferences, pointer alternatives, target size, and authentication. For native apps, test platform accessibility APIs and platform screen readers (for example VoiceOver/TalkBack/Narrator) on representative devices.

Automated tools cannot judge every issue: they miss context, many content and cognitive barriers, task usability, and some assistive-technology interactions. Track “incomplete” results for human review. Do not silence a rule or exclude a region to make a dashboard green without a documented reason, owner, expiry, and compensating test.

### 6. Rate, assign, and retest findings

For each issue, record the affected task/user, reproducible steps, observed result, expected result, evidence, frequency/confidence, impact, affected platforms, accessibility criterion if applicable, and a fix hypothesis. Separate observed facts from interpretation.

Use a practical severity scale:

- **Blocker:** critical task cannot be completed, data/safety harm is plausible, or a broad group is excluded; block release until fixed or formally mitigated.
- **High:** major task failure, severe confusion, or a significant accessibility barrier on a core flow; fix before broad release or require named risk acceptance and a dated mitigation.
- **Medium:** meaningful friction with a workable route around it; prioritize and track to an owner/date.
- **Low:** minor polish or isolated annoyance; backlog with rationale.

Severity is based on impact to users and criticality of the task, not the evaluator's confidence or visual prominence alone. Do not average a blocker away with many passing checks.

### 7. Close the loop

Create a feedback record with source, date, permission/consent constraints, relevant product version, theme, affected journey, owner, status, planned response, and follow-up date. Acknowledge feedback when a channel promises a response. Tell the user what changed when possible, or explain why it did not. Convert recurring feedback into a verified product decision, not automatic feature work.

After changes, retest the affected task and accessibility states, check for regressions in other paths, and link evidence to the release. Report residual issues, accepted risks, owners, and review dates. Reopen the audit if the implementation, content, third-party widget, or supported platform changes materially.

## Production decision

An experience audit is decision support, not certification. A release owner may proceed only when critical journeys have evidence, blocker/high findings are resolved or explicitly risk-accepted with mitigation, accessibility scope and methods are disclosed, privacy/consent controls are reviewed, open issues have owners, and the production feedback/support route is staffed. The report must state tested platforms, versions, user sample, WCAG scope/target, methods, exclusions, and known limitations.