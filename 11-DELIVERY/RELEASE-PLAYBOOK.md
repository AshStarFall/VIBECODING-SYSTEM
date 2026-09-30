# Release and Operations Playbook

## Before deployment

- Confirm owner, supported environments, release scope, data migration plan, service limits, and expected cost.
- Separate development, preview/staging, and production configuration and credentials. Keep secrets out of commits; review public client variables.
- Require appropriate CI checks and a human approval gate for consequential production changes.
- Verify health checks, structured/redacted logs, error reporting, uptime alerts, backups, and restore procedure.
- Document migration sequencing, backward compatibility, rollback, and who can execute it.
- Review domain/TLS, security headers, access controls, privacy notice/consent needs, and legal review for the actual jurisdiction/product.

## Release

1. Build the release artifact from a known commit.
2. Apply migrations using the documented safe sequence; confirm backups first where data risk exists.
3. Deploy to the intended environment and smoke-test the critical path.
4. Monitor errors, latency, resource usage, and product signals. Roll back or mitigate when thresholds are crossed.
5. Record version, date, operator, checks, migration status, and follow-up issues.

Platform pricing, free-tier rules, quotas, and policies change. Verify current official terms before choosing a host; do not rely on stale comparisons in a resource list.