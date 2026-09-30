---
name: security-review
description: Perform a scoped threat-model and security review before high-risk changes or release.
---

# Security Review

1. Identify assets, actors, entry points, trust boundaries, sensitive data, and abuse cases.
2. Trace authentication and authorization to the resource/action; do not rely on hidden UI controls.
3. Review validation, output encoding, injection, CSRF/CORS, rate limits, uploads, secrets, dependencies, and logs where applicable.
4. For AI features, include prompt injection, tool permissions, data exfiltration, unsafe output use, tenant isolation, and evaluation coverage.
5. For mobile/desktop, include local storage, permissions, deep links, updates, signing, and device compromise assumptions.
6. Prioritize findings by concrete impact and likelihood. Recommend a focused test and fix. Do not probe systems without authorization.