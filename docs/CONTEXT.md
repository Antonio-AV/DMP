# Project Context

## Product

DMP is an offline-first sales and management application for a stationery store.
It is intended to replace, after validation, an old system used by four
employees on one Windows computer.

The first release is a functional MVP with simulated data. It exists to
demonstrate the minimum useful workflows to the store owners and collect their
feedback before any production migration.

## Architecture

- Streamlit provides the local web interface opened in the store's browser.
- Python domain and application modules contain business rules and use cases.
- SQLite is the local persistence layer and requires no external server.
- Repositories isolate SQLite persistence from the domain and application rules.
- PyInstaller is the intended Windows packaging path.
- The application is a modular monolith. Do not add a remote API, cloud service,
  or distributed architecture without a concrete requirement.

## Domain Vocabulary

- `Product`: an item sold by the stationery store, with a code, description,
  current sale price, and stock balance.
- `Supplier`: a company that supplies products to the store.
- `ProductSupplier`: the relationship between a product and a supplier. A
  product has one primary supplier and may have alternative suppliers.
- `Sale`: a sale with items, a total, a type, and a lifecycle status.
- `SaleItem`: a product, quantity, and the price practiced when the sale was
  made.
- `Customer`: a customer registered for purchases made on credit.
- `Installment`: one amount and due date belonging to a credit sale.
- `Receipt`: a payment recorded for an immediate sale or an existing debt.
- `DailyCash`: the daily summary of sales and receipts.
- `StockMovement`: an immutable record of stock entry, sale, cancellation, or
  manual adjustment.

## Sale Rules

- A sale starts as `open`, becomes `completed`, or becomes `cancelled`.
- Products can be found by code or description.
- Adding the same product more than once sums its quantity.
- The current product price is copied to the sale item when added.
- An employee may edit the practiced item price during the sale.
- Historical sale prices never change when the product catalog changes.
- An immediate sale uses one payment method in the MVP: cash, Pix, debit, or
  credit card.
- A credit sale requires a customer and creates one debt or multiple
  installments.
- Every credit debt has a due date. Installments have their own due dates.
- Installments may be calculated automatically or edited manually.
- Payments may be partial and are applied to the selected credit purchase.

## Stock Rules

- Finalizing a sale decreases stock.
- A sale that would make stock negative is blocked.
- Cancelling an unpaid sale restores its stock.
- Entries and inventory adjustments are recorded as stock movements.
- Every stock movement remains available for audit and explanation.
- A stock entry may identify its supplier.

## Supplier Rules

- A supplier can provide many products.
- A product has one primary supplier and may have alternative suppliers.
- Suppliers may be archived instead of physically deleted when historical
  records refer to them.
- Supplier registration and product relationships are part of the MVP.
- Purchase orders, quotations, and advanced supplier reports are not part of
  the MVP.

## Customer Debt Rules

- Customers are registered only when needed for a credit sale.
- The customer view shows each credit purchase separately.
- The customer view also shows installment values, due dates, paid amounts, and
  total outstanding debt.
- A payment is linked to the credit purchase selected by the employee.
- Cancelling a partially paid sale is deliberately deferred until its refund or
  credit behavior is validated with the store owners.

## Cash Rules

- There is one daily cash record.
- The daily summary separates immediate sales, credit sales, customer receipts,
  and total received.
- Immediate receipts are grouped by payment method.
- The employee can enter physical counted amounts at closing for comparison.
- Closing the cash requires a separate password.
- The MVP does not model opening balance, withdrawals, supplies, or expenses.
- There are no individual employee permissions in the MVP.

## Technology And Data Rules

- The application must work without internet access.
- SQLite data stays on the Windows computer and is not committed to Git.
- Money uses integer cents.
- Changes involving a sale, stock, debt, receipt, or daily cash must use a
  transaction so related state cannot be partially persisted.
- The Streamlit session may hold only transient UI state such as the active cart.
- Persisted business state belongs in SQLite.
- AI, online synchronization, automatic migration, fiscal documents, and device
  integrations are future concerns.

## Testing Boundaries

- The primary test seam is the public application/use-case boundary backed by a
  temporary SQLite database.
- Tests should exercise real sale, stock, debt, receipt, supplier, and cash rules
  with deterministic fixtures.
- Streamlit tests should cover only minimal user journeys and integration with
  the application layer.
- Ranking-like calculations do not exist in this project; business behavior
  belongs in use-case tests rather than widget tests.
- Windows packaging should have a smoke test when packaging changes.
