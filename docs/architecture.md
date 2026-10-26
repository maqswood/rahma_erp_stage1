# Architecture

Rahma ERP is a modular Django monolith using Django Templates and Bootstrap 5. PostgreSQL is the system of record. Domain services will own posting workflows; views should validate requests and delegate business operations to those services.

## Core invariants
- Every operational document has an explicit branch/warehouse.
- Branch access must be enforced in querysets and service methods, not only in templates.
- Draft documents may be edited; posted documents are corrected by reversal/credit workflows.
- Inventory movements and accounting journals are posted atomically with their source documents.
- Never use floats for money; use Decimal.
- Do not display fabricated metrics in production dashboards.
