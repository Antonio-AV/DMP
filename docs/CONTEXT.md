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
- `Sale`: a sale with items, a total, a type, a lifecycle status, and the local
  date and time when it was completed.
- `SaleItem`: a product, quantity, and the price practiced when the sale was
  made.
- `Customer`: a customer record that can be created independently and later
  associated with purchases made on credit.
- `Installment`: one amount and due date belonging to a credit sale.
- `Receipt`: a payment recorded for an immediate sale or an existing debt.
- `DailyCash`: the daily summary of sales and receipts.
- `StockMovement`: an immutable record of stock entry, sale, cancellation, or
  manual adjustment.

## Sale Rules

- A sale starts as `open`, becomes `completed`, or becomes `cancelled`.
- A completed sale stores the local date and time when confirmation finished.
- The completion timestamp remains part of the sale history after cancellation.
- Sale searches may use the sale number or a selected local date and hour; the
  selected hour includes minutes `HH:00` through `HH:59` and all seconds in
  that range on the selected date, including the final hour `23:00`-`23:59`.
- Products can be found by code or description.
- Adding the same product more than once sums its quantity.
- The current product price is copied to the sale item when added.
- An employee may edit the practiced item price during the sale.
- Product prices, practiced prices, installment amounts, and payments must be
  greater than zero; negative values are rejected.
- Historical sale prices never change when the product catalog changes.
- An immediate sale uses one payment method in the MVP: cash, Pix, debit, or
  credit card.
- A credit sale requires a customer and starts with one debt by default.
- The employee may change the installment count to one or more; one keeps the
  single-debt flow, while two or more create installments.
- A single-debt sale stores no separate installment record; the debt stores the
  total value and its due date.
- Every credit debt has a due date. Installments have their own due dates.
- A credit sale with installments cannot be completed until every installment
  has a due date.
- Installment amounts and monthly due dates are calculated automatically from
  the sale date; the employee may edit both before confirmation.
- Remainder cents are distributed across the first installments so their sum
  equals the sale total exactly.
- The installment count cannot exceed the sale total in cents.
- Payments may be partial and are applied to the selected credit purchase.
- A payment for a single-debt purchase reduces the debt balance directly.
- A payment for a purchase with multiple installments is applied first to the
  oldest open installment, then to subsequent installments if there is a
  remaining amount.

## Stock Rules

- Finalizing a sale decreases stock.
- Editing product data does not change stock; stock changes use entries or
  inventory adjustments.
- Stock is revalidated for every cart item immediately before finalization.
- A sale that would make stock negative is blocked.
- Cancelling an unpaid sale restores its stock.
- Entries and inventory adjustments are recorded as stock movements.
- Every stock movement remains available for audit and explanation.
- A stock entry may identify its supplier.
- The initial product stock movement may have quantity zero; all other stock
  movements require a positive quantity.

## Supplier Rules

- A supplier can provide many products.
- A product must have one primary supplier and may have alternative suppliers.
- The primary supplier cannot also be listed as an alternative supplier for the
  same product.
- Suppliers may be archived instead of physically deleted when historical
  records refer to them.
- Supplier registration and product relationships are part of the MVP.
- Purchase orders, quotations, and advanced supplier reports are not part of
  the MVP.

## Customer Debt Rules

- Customers may be registered at any time, independently of an active credit
  sale.
- The customer view shows each credit purchase separately.
- The customer view also shows installment values, due dates, paid amounts, and
  total outstanding debt.
- A payment is linked to the credit purchase selected by the employee.
- Cancelling a partially paid sale is deliberately deferred until its refund or
  credit behavior is validated with the store owners.

## Cash Rules

- There is one daily cash record.
- The daily cash record is created automatically on the first access for the
  day, with zero totals and no opening step or opening balance.
- The daily summary separates immediate sales, credit sales, debt receipts, and
  total received.
- Immediate sales and debt receipts are grouped by payment method.
- Total received equals immediate sales receipts plus debt receipts; unpaid
  credit sales are excluded until payment.
- Cash difference is calculated as counted total minus expected total: negative
  means shortage, positive means surplus, and zero means no difference.
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
