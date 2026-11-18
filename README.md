# ExecView — Superstore Executive Sales Dashboard

This package prepares the supplied Superstore workbook for a Power BI executive sales dashboard.

## Quick start
1. Open Power BI Desktop.
2. Home > Get data > Text/CSV.
3. Import every CSV in `data/`.
4. Follow `documentation/Model_and_Dashboard_Guide.md` to create relationships and report pages.
5. Add measures from `powerbi/Measures.dax`.

## Data model
- FactSales: transaction-level sales rows, with return flag and dimension keys.
- DimCustomer, DimProduct, DimGeography, DimShipMode, DimRegion, DimDate.
- FactTargets_Illustrative: synthetic monthly regional targets.

## Important transparency notes
- The original workbook has 10,194 order-line rows, 4 regional managers and 296 returned-order records.
- There are 675 order-line rows with Order Date after 17 Nov 2026. They are retained in the prepared data; filter them out if your reporting cutoff is 17 Nov 2026.
- The monthly regional targets are illustrative, calculated as 105% of the actual sales for each region/month. They are NOT official company targets.
- The prepared CSVs and DAX have not been imported or validated inside Power BI Desktop in this environment. The final `.pbix`, screenshots, and publication still need to be created/tested in Power BI Desktop and Power BI Service.

## Folders
- `data/`: model-ready CSV tables.
- `powerbi/`: DAX measures.
- `documentation/`: model and report build instructions, validation notes and insight summary.
- `scripts/`: reproducible preparation script.
