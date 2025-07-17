import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV
df = pd.read_csv(r'D:\internship\Retail.csv')

# Preview
print("🔹 First 5 rows:\n", df.head())

# Drop rows with missing CustomerID
df.dropna(subset=['CustomerID'], inplace=True)

# Convert InvoiceDate to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Add TotalAmount column
df['TotalAmount'] = df['Quantity'] * df['UnitPrice']

# ✅ Insight 1: Top 5 countries by total sales
print("\n🌍 Top 5 Countries by Sales:")
print(df.groupby('Country')['TotalAmount'].sum().sort_values(ascending=False).head())

# ✅ Insight 2: Monthly Sales Trend
df['Month'] = df['InvoiceDate'].dt.month
monthly_sales = df.groupby('Month')['TotalAmount'].sum()

print("\n📆 Monthly Sales Trend:")
print(monthly_sales)

# ✅ Insight 3: Most sold products
top_products = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head()
print("\n📦 Top 5 Most Sold Products:")
print(top_products)

# Optional: Plot Monthly Sales Trend
plt.figure(figsize=(10, 5))
sns.lineplot(x=monthly_sales.index, y=monthly_sales.values, marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.grid()
plt.tight_layout()
plt.savefig("monthly_sales_trend.png")
plt.show()
