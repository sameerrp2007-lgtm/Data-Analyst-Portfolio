# Power BI Retail Sales Dashboard — Build Guide

This folder contains the data and DAX measures needed to build the dashboard in Power BI Desktop. A `.pbix` file is not included because it must be created/saved inside Power BI Desktop.

## 1. Import
- Open Power BI Desktop.
- Get Data → Text/CSV → select `retail_sales.csv`.
- Confirm `Order_Date` is Date, `Discount_Rate` is Decimal Number, and sales/cost/profit fields are Decimal Number.
- Load the data. Rename the table to `retail_sales` if needed.

## 2. Add measures
Copy measures from `PowerBI_DAX_Measures.txt` into Modeling → New measure.

## 3. Suggested one-page layout
Top row: Card visuals for Total Revenue, Total Profit, Total Orders, Units Sold, Profit Margin %.
Middle left: Line chart — Order_Date by month on X-axis, Total Revenue on Y-axis.
Middle right: Clustered bar chart — Category on Y-axis, Total Revenue on X-axis.
Bottom left: Bar chart — City and Total Revenue.
Bottom right: Donut chart — Sales_Channel and Total Revenue.
Add slicers for Order_Date, City, Category, and Sales_Channel.

## 4. Portfolio screenshots
After building, save the report as `Retail_Sales_Dashboard.pbix` and export a screenshot or PDF for your GitHub README.

Dataset is synthetic and for demonstration/learning only.
