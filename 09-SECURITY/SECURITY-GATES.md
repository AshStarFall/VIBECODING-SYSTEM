# Security Gates

Scale depth to exposed data and impact. For sensitive, regulated, financial, identity, child-directed, or AI-agent systems, involve a qualified human reviewer and applicable legal/compliance experts.

## Before implementation

- Inventory assets, user roles, trust boundaries, entry points, sensitive data, third parties, abuse cases, and likely impact.
- Define authentication, authorization, tenant isolation, retention, deletion, encryption, and incident contact expectations.

## Before merge/release

- No secrets in source, history, logs, client bundles, or build artifacts; use secret scanning and rotation procedures.
- Enforce server-side authorization and validated inputs; test denial paths as well as happy paths.
- Review injection, XSS/CSRF/CORS, SSRF, upload handling, rate limits, session/token handling, and security headers as applicable.
- Review dependency provenance, known vulnerabilities, permissions, transitive risk, and license.
- Protect production data; test restore and least-privilege access. Redact sensitive telemetry.
- For AI: test prompt injection, retrieval isolation, output validation, tool permissions, data leakage, and abuse/cost controls.
- For mobile/desktop: inspect permissions, local storage, deep links/IPC, update channels, and release signing.

Active penetration-testing tools such as [Strix](https://github.com/usestrix/strix) can send requests, attempt exploits, and validate findings. Run them only with explicit authorization and written target scope, preferably against isolated staging with synthetic data and bounded credentials. Review LLM/provider data handling and every finding or proposed fix. Never aim active scans at a production or third-party system without documented permission.

Use OWASP ASVS/Top 10, MASVS/MASTG, and GenAI guidance as scoped references, not proof of security. Record findings, evidence, mitigations, and accepted residual risks. Do not run intrusive scans without authorization.