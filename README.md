# ExecView — Executive Sales & Business Intelligence Dashboard

ExecView is an interactive business intelligence project built in **Microsoft Power BI** using the Superstore sales dataset. It is designed to give decision-makers a concise view of sales, profitability, regional performance, product categories, and customer activity, with additional drill-through and row-level security features.

## Project links

- **GitHub repository:** [hdrsanalytics/ExecView-PowerBI](https://github.com/hdrsanalytics/ExecView-PowerBI)
- **Demo video (Loom):** [Watch the ExecView walkthrough](https://www.loom.com/share/8c83746704b84d65825ee1b2f3b3235c)

## Dashboard pages

### 1. Executive Overview
A high-level performance summary featuring:
- Total Sales
- Total Profit
- Profit Margin
- Total Orders
- Sales Target
- Target Attainment %
- Annual sales trend
- Sales by region
- Sales by product category
- Sales by customer segment
- Region slicer for interactive filtering

### 2. Sales Deep Dive
A more detailed view of sales performance, including:
- Sales trend over time
- Sales by region and product category
- Sales by product sub-category
- Profit by region

### 3. Customer Analysis
A customer-focused page showing:
- Sales by customer segment
- Customer sales contribution
- Orders by region

### 4. Product Details
A drill-through destination that can be opened from the product sub-category chart. It displays the selected sub-category's sales, profit, and order metrics.

## Data model and technical features

The report uses a dimensional model with the following tables:

- `FactSales` — transaction-level sales data
- `FactTargets_Illustrative` — illustrative monthly regional targets
- `DimCustomer` — customer attributes
- `DimProduct` — product and category attributes
- `DimGeography` — geographic attributes
- `DimShipMode` — shipping methods
- `DimRegion` — sales regions and regional manager information
- `DimDate` — calendar/date dimension

The Power BI report includes **21 DAX measures** covering sales, profit, margin, order volume, discounts, returns, targets, year-over-year comparisons, shipping time, and unprofitable sales. The measures are provided in [`powerbi/Measures.dax`](powerbi/Measures.dax).

Additional implemented features:
- Date table marked as the model's date table
- Year-over-year sales and profit calculations
- Interactive region slicer
- Drill-through from product sub-category to Product Details
- Chart tooltips with additional profit information
- Four regional Row-Level Security roles: East, West, Central, and South
- RLS roles tested in Power BI Desktop using **View as**

## Repository structure

```text
ExecView_Submission_Pack/
├── data/
│   ├── FactSales.csv
│   ├── FactTargets_Illustrative.csv
│   ├── DimCustomer.csv
│   ├── DimDate.csv
│   ├── DimGeography.csv
│   ├── DimProduct.csv
│   ├── DimRegion.csv
│   └── DimShipMode.csv
├── documentation/
│   ├── Initial_Insights.md
│   ├── Model_and_Dashboard_Guide.md
│   └── Validation_Log.md
├── powerbi/
│   └── Measures.dax
├── scripts/
│   └── prepare_data.py
├── Superstore_Source.xlsx
└── README.md
```

The completed Power BI `.pbix` report and dashboard screenshots are also available in the GitHub repository. See the repository link above for the submitted files.

## Getting started

### View the dashboard

1. Open the GitHub repository and locate the submitted `.pbix` file.
2. Download it and open it using **Power BI Desktop**.
3. If Power BI prompts for data-source paths, point it to the CSV files in the repository's `data/` folder, or use the included source workbook and preparation files as appropriate.

### Reproduce the prepared data

1. Install Python 3 and the dependencies required by `scripts/prepare_data.py`.
2. Run the preparation script from the project directory:

   ```bash
   python scripts/prepare_data.py
   ```

3. The script prepares the model-ready CSV tables in `data/`. Review the script and the documentation before regenerating files.
4. In Power BI Desktop, import the CSV tables and follow [`documentation/Model_and_Dashboard_Guide.md`](documentation/Model_and_Dashboard_Guide.md) for the model relationships and report setup.
5. Use the DAX definitions in [`powerbi/Measures.dax`](powerbi/Measures.dax) to recreate the measures.

## Data notes and limitations

- The source workbook contains **10,194 order-line rows**, **4 regional managers**, and **296 returned-order records**.
- The prepared data retains **675 order-line rows with Order Dates after 17 November 2026**. These records have not been silently removed. Apply an explicit reporting cutoff if the analysis is intended to stop at 17 November 2026.
- **The monthly regional targets are illustrative, not official company budgets.** They were generated as 105% of actual sales for each region/month. Any target variance or attainment result should therefore be interpreted as a demonstration of the dashboard's target-analysis functionality, not as a genuine assessment against an approved business target.
- The included insights are descriptive observations from the supplied dataset; they should not be interpreted as causal findings.
- The GitHub repository and Loom recording are the project-sharing links. Power BI Service publication is not claimed here; access to publishing and sharing features depends on the Power BI account and workspace permissions.

## Documentation

- [Model and Dashboard Guide](documentation/Model_and_Dashboard_Guide.md)
- [Validation Log](documentation/Validation_Log.md)
- [Initial Insights](documentation/Initial_Insights.md)

---

**Project:** ExecView  
**Platform:** Microsoft Power BI  
**Repository:** [hdrsanalytics/ExecView-PowerBI](https://github.com/hdrsanalytics/ExecView-PowerBI)  
**Demo:** [Loom walkthrough](https://www.loom.com/share/8c83746704b84d65825ee1b2f3b3235c)

