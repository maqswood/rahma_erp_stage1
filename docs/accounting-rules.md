# Accounting rules — planned implementation

- Use double-entry journal entries; total debits must equal total credits for each posted entry.
- A posted entry is immutable; correct it through a linked reversal and replacement.
- Inventory receipt debits inventory and credits GRNI or accounts payable depending on the matching workflow.
- Sales recognize revenue and VAT separately; inventory relief debits cost of goods sold and credits inventory using the cost snapshot at posting.
- Customer receipts and supplier payments must be allocated to open documents.
- Consolidated reporting must eliminate internal balances and internal profit where applicable.
- Saudi VAT and ZATCA behavior must be validated against current official requirements before compliance claims.
