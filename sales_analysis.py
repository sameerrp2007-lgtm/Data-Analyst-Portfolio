import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DATA = Path(__file__).with_name("retail_sales.csv")
OUT = Path(__file__).with_name("outputs")
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA, parse_dates=["Order_Date"])
df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)

print("DATA OVERVIEW")
print(df.head())
print("\nRows, columns:", df.shape)
print("\nMissing values:\n", df.isna().sum())
print("\nKPI SUMMARY")
print(f"Total revenue: ₹{df['Revenue'].sum():,.2f}")
print(f"Total profit: ₹{df['Profit'].sum():,.2f}")
print(f"Orders: {df['Order_ID'].nunique():,}")
print(f"Units sold: {df['Quantity'].sum():,}")
print(f"Profit margin: {df['Profit'].sum()/df['Revenue'].sum():.1%}")

monthly = df.groupby("Month", as_index=False)[["Revenue", "Profit"]].sum()
category = df.groupby("Category", as_index=False)[["Revenue", "Profit"]].sum().sort_values("Revenue", ascending=False)
city = df.groupby("City", as_index=False)[["Revenue", "Profit"]].sum().sort_values("Revenue", ascending=False)
product = df.groupby("Product", as_index=False)[["Quantity", "Revenue", "Profit"]].sum().sort_values("Revenue", ascending=False)

monthly.to_csv(OUT / "monthly_summary.csv", index=False)
category.to_csv(OUT / "category_summary.csv", index=False)
city.to_csv(OUT / "city_summary.csv", index=False)
product.to_csv(OUT / "product_summary.csv", index=False)

plt.figure(figsize=(10, 5))
plt.plot(monthly["Month"], monthly["Revenue"], marker="o", label="Revenue")
plt.xticks(rotation=60, ha="right")
plt.title("Monthly Revenue Trend")
plt.ylabel("Revenue (₹)")
plt.tight_layout()
plt.savefig(OUT / "monthly_revenue.png", dpi=160)
plt.close()

plt.figure(figsize=(8, 5))
plt.bar(category["Category"], category["Revenue"])
plt.title("Revenue by Category")
plt.ylabel("Revenue (₹)")
plt.xticks(rotation=25, ha="right")
plt.tight_layout()
plt.savefig(OUT / "revenue_by_category.png", dpi=160)
plt.close()

print("\nTOP CATEGORIES\n", category.to_string(index=False))
print("\nTOP CITIES\n", city.head(5).to_string(index=False))
print("\nTOP PRODUCTS\n", product.head(5).to_string(index=False))
print(f"\nReports and charts saved to: {OUT}")
