# Backend and Data

## Plan before endpoints

- Define data ownership, entities, invariants, tenant boundaries, retention/deletion, and migration path.
- Specify API contracts, authentication, authorization, validation, idempotency, pagination, errors, and rate limits.
- Identify transaction boundaries, consistency needs, background work, backups, and recovery objectives.

## Implement

- Create schema and safe migration before dependent endpoints. Enforce invariants in the persistence/domain boundary, not only UI forms.
- Validate input at trust boundaries; apply object-level authorization on every sensitive action.
- Use parameterized queries and least-privilege credentials. Avoid logging credentials or sensitive payloads.
- Make retryable work idempotent where possible. Define timeouts, retries, and dead-letter/recovery behavior.

## Verify

Test permissions for allowed and denied actors, migration forward/rollback expectations, constraints, concurrency where material, API contracts, backup restore, and failure handling. Use synthetic data in non-production tests.

Candidate resources: PostgreSQL, Supabase, Prisma/Drizzle, FastAPI, Django, Express, Zod, SQLFluff. See [`../12-RESOURCES/README.md`](../12-RESOURCES/README.md).