# Power BI build guide (beginner version)

## What is included
Import the CSVs in `data/` using **Home > Get data > Text/CSV**. Import all eight files.
Do not use the original Excel workbook for the final model; the CSVs are already split into model-ready tables.

## Relationships to create
In Model view, create these active relationships. The dimension side is `1`; the fact side is `*`.
Use **Single** cross-filter direction.

| One side | Many side |
|---|---|
| DimCustomer[Customer ID] | FactSales[CustomerID] |
| DimProduct[Product ID] | FactSales[ProductID] |
| DimGeography[GeographyKey] | FactSales[GeographyKey] |
| DimShipMode[Ship Mode] | FactSales[ShipMode] |
| DimRegion[Region] | FactSales[Region] |
| DimDate[Date] | FactSales[OrderDate] |
| DimRegion[Region] | FactTargets_Illustrative[Region] |
| DimDate[Date] | FactTargets_Illustrative[MonthStart] |

Important: the target table has one row per region/month and its MonthStart value is the first day of each month. The relationship to DimDate is intentional for month-level reporting. Use month/year fields from DimDate for target comparisons, not a day-level target interpretation.

## Date table
Select `DimDate` > Table tools > Mark as date table > choose `Date`.
Sort `DimDate[Month]` by `DimDate[Month Number]`.
Sort `DimDate[Year Month]` by `DimDate[MonthStart]`.

## Measures
Open `powerbi/Measures.dax`. Create each measure from **Modeling > New measure**, one at a time, pasting the expression after the equals sign. The file contains 21 measures. Set currency formatting for sales/profit/target measures, percentage formatting for margin/rates, and whole number formatting for orders/units.

## Three report pages
1. **Executive Overview**: cards for Total Sales, Total Profit, Profit Margin, Total Orders, Target Attainment %. Add a line chart with Year Month and Total Sales; clustered bar chart with Region and Total Sales; bar chart with Category and Total Profit.
2. **Sales Performance**: line chart Year Month vs Sales; bar charts Region, Category, Sub-Category; slicers for Year, Region, Segment and Ship Mode. Add Sales YoY % and Profit YoY % cards.
3. **Customer & Returns**: cards Total Orders, Returned Orders, Return Rate, Average Order Value. Bar chart Customer Name vs Total Sales (Top N 10); map using City/State or Postal Code and Total Sales; chart Segment vs Total Sales; table of customer, sales, profit.

## Drill-through
Create a `Product Detail` page. Add `DimProduct[Product Name]` to the Drill-through field well. Add cards for Total Sales, Total Profit, Units Sold and a monthly sales line chart. Repeat with a `Region Detail` page using `DimRegion[Region]` if time permits.

## Row-level security
Modeling > Manage roles > Create role `West` and add table filter on `DimRegion`:
`[Region] = "West"`
Repeat roles for `East`, `Central`, and `South`. In Modeling > View as, test each role. This is a simple region-based demonstration; it is not dynamic user-email security.

## Important checks
- Confirm every relationship is active, one-to-many, single direction.
- Confirm DimCustomer has unique Customer ID and DimProduct has unique Product ID.
- Confirm no FactSales rows were dropped.
- Check that the date table covers the maximum order and ship dates.
- Use OrderDate for sales time intelligence. If you later analyze shipping dates, create a separate inactive relationship or role-playing date table.
- The dataset includes orders dated after 17 Nov 2026. These are preserved; apply an as-of date filter if the supervisor expects reporting only through 17 Nov 2026.
- The target table is simulated, not an official budget. Replace it if the supervisor provides real targets.
