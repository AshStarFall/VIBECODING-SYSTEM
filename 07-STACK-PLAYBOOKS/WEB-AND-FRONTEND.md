# Web and Frontend

## Plan

- Distinguish a static/content site from an authenticated application; choose rendering/hosting accordingly.
- Define routes, user journeys, data loading, URL state, error/loading/empty states, metadata, and browser support.
- Reuse established project components and tokens. Define design direction before creating new UI.

## Build

- Keep form validation and shared schemas consistent across client/server; server-side checks remain authoritative.
- Make semantic HTML, keyboard support, visible focus, responsive layouts, and reduced-motion support part of implementation.
- Add third-party scripts only when needed; understand privacy, performance, and CSP implications.
- Avoid shipping secrets in browser bundles. Treat all client input and client-side permission state as untrusted.

## Verify

Run project lint/type/build and behavior tests. Exercise critical flows in a real browser at mobile and desktop sizes. Check navigation, refresh/deep links, forms, accessibility, console/network failures, metadata, and performance budgets appropriate to the product.

Candidate resources: React/Next.js/Vite/Astro, Playwright, axe-core, Lighthouse, Web Vitals. See [`../12-RESOURCES/README.md`](../12-RESOURCES/README.md).