# Database design — Stage 1

Implemented foundation models:
- Organization: legal entity-level settings and default currency.
- Branch: configurable operational location, unique code within an organization.
- User: Django user with an initial role classification.
- UserBranchAccess: explicit per-user branch access and action capabilities.
- AuditEvent: append-oriented record of consequential actions.

Planned domain entities are listed in the project specification and will be introduced alongside their services and migrations in later stages. Posted journal and stock ledgers must preserve history. Constraints and row locks will be used where appropriate for concurrency.
