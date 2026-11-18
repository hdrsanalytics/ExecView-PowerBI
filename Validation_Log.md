# Source data validation

Source workbook sheets: Orders, People, Returns.

## Row counts and coverage
- Orders: 10,194 rows.
- People: 4 rows.
- Returns: 296 rows.
- Distinct Order IDs: 5,111.
- Distinct customers: 804.
- Distinct products: 1,862.
- Order Date range: 2023-01-03 to 2026-12-30.
- Ship Date range: 2023-01-07 to 2027-01-05.
- Order lines after 17 Nov 2026: 675 (preserved, not silently removed).
- Blank values in the 21 source Orders columns: none detected.
- Row ID duplicates: 0.
- Returned orders listed: 296; all listed order IDs match the Orders sheet.

## Aggregate reconciliation (source workbook)
- Sales: $2,326,534.35.
- Profit: $292,296.81.
- Quantity: 38,654.
- Distinct orders: 5,111.

## Notes
- Repeated Order ID + Product ID combinations occur in the source; they were preserved because they are separate source rows and are not necessarily duplicates.
- Targets are not present in the source workbook. The supplied target CSV is explicitly illustrative and should not be represented as an official budget.
- These checks were run on the workbook after conversion from legacy `.xls` to `.xlsx`; the source rows and values were preserved by the conversion.
- The Power BI model itself still needs validation after import.
