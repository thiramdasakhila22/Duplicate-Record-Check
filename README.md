# Veda Technology – Day 13 | Task 13: Duplicate Record Check

## Objective
Identify duplicate records, document the findings, and create a cleaned copy of the Superstore dataset.

## Tools
- Python
- Pandas
- Excel
- GitHub

## Dataset
`superstore_cleaned.csv`

The supplied dataset contains **9,977 records and 13 columns**.

## Duplicate Detection Approach

### 1. Full-row duplicate check
Pandas `duplicated()` was used to compare complete records.

**Result:** 0 exact duplicate rows were found.

### 2. Key-column screening
A composite set of business attributes was checked:

- City
- State
- Postal Code
- Category
- Sub-Category
- Sales
- Quantity
- Discount
- Profit

This identified **55 potential duplicate groups involving 114 records**.

These were **not automatically deleted** because the dataset does not contain a unique transaction identifier such as Order ID, Row ID, or Product ID. Repeated business attributes can represent legitimate separate transactions.

### 3. Cleaning decision
Only confirmed exact full-row duplicates were eligible for removal.

**Records removed: 0**

**Final cleaned records: 9,977**

## Key Finding
No confirmed exact duplicates were present in the supplied dataset.

The potential key-column repeats were documented separately for review instead of being deleted blindly.

## Business Impact
Duplicates can inflate:
- Sales and revenue
- Profit
- Transaction counts
- Customer counts
- KPIs and reports

Therefore, duplicate removal should be based on a valid business key and business context.

## Deliverables
- `duplicate_report.csv` – summary of duplicate checks
- `duplicate_candidates.csv` – potential key-column duplicate records
- `superstore_cleaned_task13.csv` – cleaned dataset
- `Task13_Duplicate_Record_Check.xlsx` – Excel workbook with Summary, Potential Duplicates, Cleaned Data, and Audit Note
- `audit_note.md` – audit documentation
- `duplicate_record_check.py` – Pandas analysis script

## Conclusion
The dataset passed the exact duplicate check. No records required removal, and all potential duplicate candidates were documented for further business validation.
