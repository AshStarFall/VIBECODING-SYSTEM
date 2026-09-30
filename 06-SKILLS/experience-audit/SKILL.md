---
name: experience-audit
description: Audit a product journey for desirability, usability, accessibility, trust, and production feedback readiness using evidence.
---

# Experience Audit

## Inputs

Target product/build, release or decision, user groups, critical task(s), supported platforms, available research/analytics/support feedback, applicable standards, and access constraints.

## Steps

1. Read [`../../08-PRODUCT-DESIGN/EXPERIENCE-AUDIT.md`](../../08-PRODUCT-DESIGN/EXPERIENCE-AUDIT.md). Copy [`../../13-TEMPLATES/EXPERIENCE-AUDIT.md`](../../13-TEMPLATES/EXPERIENCE-AUDIT.md) into the target project and define scope, audience, environment, and explicit exclusions.
2. Inspect the running product and walk the user journey. Record version/platform, task outcome, friction, failure/recovery states, and reproducible evidence.
3. Review existing user feedback and behavior data without treating either as representative by default. Check consent, data minimization, redaction, access, and retention before using recordings or analytics.
4. Run a focused heuristic review; label findings as hypotheses until supported by task observation or other evidence.
5. For meaningful user decisions, test realistic neutral tasks with likely users. Include relevant access needs and assistive technology; report sample and limits. Never claim statistical significance from a small formative sample.
6. For accessibility, select applicable WCAG/platform criteria and representative critical states. Use automated scans plus manual keyboard, screen-reader, zoom/reflow, and device checks. Record all incomplete results for human review.
7. Rate issues by impact, frequency/evidence confidence, and task criticality. Record owner, proposed fix, deadline, and retest evidence. Do not average a severe barrier away.
8. Complete the feedback handling and release decision sections. State unresolved risks, exclusions, support route, and exact checks performed.

## Output

A completed experience-audit report with findings prioritized by user impact, linked evidence, a remediation list, retest results, and a qualified release recommendation. Do not call the audit a certification or imply that automated tooling proves accessibility.