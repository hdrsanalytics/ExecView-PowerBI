import pandas as pd
import numpy as np
from pathlib import Path

source = Path("Superstore.xlsx")  # save the original workbook beside this script
out = Path("data")
out.mkdir(exist_ok=True)

orders = pd.read_excel(source, sheet_name="Orders")
people = pd.read_excel(source, sheet_name="People")
returns = pd.read_excel(source, sheet_name="Returns")
orders["Order Date"] = pd.to_datetime(orders["Order Date"])
orders["Ship Date"] = pd.to_datetime(orders["Ship Date"])
for c in ["Postal Code"]:
    orders[c] = orders[c].astype("string").fillna("Unknown").str.strip()
for c in ["Country/Region","State/Province","City"]:
    orders[c] = orders[c].fillna("Unknown").astype(str).str.strip()

geo_cols = ["Country/Region","State/Province","City","Postal Code"]
geo = orders[geo_cols].drop_duplicates().sort_values(geo_cols).reset_index(drop=True)
geo.insert(0, "GeographyKey", np.arange(1, len(geo)+1))
orders = orders.merge(geo, on=geo_cols, how="left", validate="many_to_one")

dim_customer = orders[["Customer ID","Customer Name","Segment"]].drop_duplicates("Customer ID")
dim_product = orders[["Product ID","Product Name","Category","Sub-Category"]].drop_duplicates("Product ID")
dim_ship = pd.DataFrame({"Ship Mode": sorted(orders["Ship Mode"].dropna().unique())})
dim_region = people[["Region","Regional Manager"]].drop_duplicates("Region")
dmin = min(orders["Order Date"].min(), orders["Ship Date"].min()).normalize()
dmax = max(orders["Order Date"].max(), orders["Ship Date"].max()).normalize()
dates = pd.DataFrame({"Date": pd.date_range(dmin, dmax, freq="D")})
dates["Year"] = dates.Date.dt.year
dates["Quarter"] = "Q" + dates.Date.dt.quarter.astype(str)
dates["Month Number"] = dates.Date.dt.month
dates["Month"] = dates.Date.dt.strftime("%B")
dates["Year Month"] = dates.Date.dt.strftime("%Y-%m")
dates["MonthStart"] = dates.Date.dt.to_period("M").dt.to_timestamp()
dates["Day"] = dates.Date.dt.day
dates["Day Name"] = dates.Date.dt.strftime("%A")

returned = set(returns.loc[returns.Returned.astype(str).str.lower().eq("yes"), "Order ID"])
fact = orders[["Row ID","Order ID","Order Date","Ship Date","Ship Mode","Customer ID","Region",
               "Product ID","GeographyKey","Sales","Quantity","Discount","Profit"]].copy()
fact["Returned"] = fact["Order ID"].isin(returned)
fact.rename(columns={"Row ID":"RowID","Order ID":"OrderID","Order Date":"OrderDate",
                     "Ship Date":"ShipDate","Ship Mode":"ShipMode","Customer ID":"CustomerID",
                     "Product ID":"ProductID"}, inplace=True)

monthly = orders.assign(MonthStart=orders["Order Date"].dt.to_period("M").dt.to_timestamp()) \
    .groupby(["Region","MonthStart"], as_index=False).Sales.sum()
targets = monthly.rename(columns={"Sales":"ActualSalesReference"})
targets["TargetSales"] = (targets["ActualSalesReference"] * 1.05).round(2)
targets = targets[["Region","MonthStart","TargetSales"]]

tables = {"FactSales":fact, "DimCustomer":dim_customer, "DimProduct":dim_product,
          "DimGeography":geo, "DimShipMode":dim_ship, "DimRegion":dim_region,
          "DimDate":dates, "FactTargets_Illustrative":targets}
for name, df in tables.items():
    df.to_csv(out/f"{name}.csv", index=False, encoding="utf-8-sig")
