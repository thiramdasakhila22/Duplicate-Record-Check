# Task 13 – Duplicate Record Check

## Dataset
`superstore_cleaned.csv`

## Objective
Identify duplicate records, assess whether repeated records are true duplicates,
and produce a cleaned copy without removing legitimate transactions.

## Methodology
1. Checked complete rows for exact duplicates using Pandas `duplicated()`.
2. Screened a composite set of business columns for repeated combinations.
3. Because the supplied dataset does not contain a unique transaction identifier
   such as Order ID, Row ID, or Product ID, key-column repeats were treated as
   potential candidates rather than automatically deleted.
4. Only confirmed exact full-row duplicates were eligible for removal.
5. Created a separate cleaned copy and retained the original data unchanged.

## Results
- Original records: 9977
- Original columns: 13
- Missing values: 0
- Exact duplicate rows to remove: 0
- Exact duplicate groups: 0
- Potential key-column duplicate groups: 55
- Records in potential key-column duplicate groups: 114
- Records removed: 0
- Final cleaned records: 9977

## Key Finding
No exact full-row duplicates were found. Therefore, no records were removed
from the cleaned dataset.

Repeated combinations of business attributes were identified as potential
duplicate candidates. These were retained because the dataset lacks a unique
transaction ID, and repeated sales characteristics can represent legitimate
separate transactions.

## Business Impact
Uncontrolled duplicates can inflate sales, profit, transaction counts,
customer counts, and other KPIs. Duplicate handling should therefore be based
on a valid business key rather than deleting every repeated value.

## Audit Decision
**Status: PASS – No confirmed exact duplicates found.**
Potential key-column repeats are documented for review rather than deleted.
