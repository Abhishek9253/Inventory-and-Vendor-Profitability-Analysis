# Inventory and Vendor Profitability Analysis.

## 🧩 Business Problem:
Effective inventory and sales management are essential for maximizing profitability in the retail and wholesale industry. This analysis aims to uncover actionable insights that can help optimize inventory turnover, pricing strategies, and vendor performance.

## Objectives:
- Identify underperforming brands for potential promotional or pricing strategies.
- Determine top vendors contributing significantly to gross profit.
- Analyze the impact of bulk purchasing on unit costs.
- Evaluate inventory turnover to minimize holding costs.
- Examine profitability variance between high-performing and low-performing vendors.

## 🔍 Exploratory Data Analysis (EDA) Summary
### 📌 Summary Statistics:
- **Gross Profit: **Min value of -52,002.78, indicating significant losses potentially due to high costs or discounting strategies.
- **Profit Margin:** Contains values of -∞, pointing to instances of zero or negative revenue.
- **Total Sales Quantity / Sales Dollars:** Minimum values are 0, highlighting unsold or obsolete inventory.

### ⚠️ Outliers:
- **Purchase & Actual Price:** Max values (5,681.81 and 7,499.99) far exceed the means (24.39 and 35.64), indicating the presence of premium-priced items.
- **Freight Cost:** Ranges from 0.09 to 257,032, reflecting inconsistencies in logistics or large-volume shipments.
- **Stock Turnover:** Ranges from 0 to 274.5, suggesting uneven product movement—some sell out rapidly, others stagnate.

### 🧹 Data Filtering:
Filtered out transactions to improve data reliability:
- **Gross Profit** <= 0 (to exclude transactions leading to losses).
- **Profit Margin**<= 0 (to ensure analysis focuses on profitable transactions)
- **Sales Quantity** = 0 (to eliminate inventory that has never sold)


## ❓ Research Questions & Key Findings
### 1. 🚩 Underperforming Brands:
- 198 brands have low sales but high margins.
- **Opportunity:** Implement promotions or pricing adjustments to increase volume without reducing profitability.

### 2. 📦 Top Vendors:
- Top 10 vendors make up 65.69% of total purchases.
- **Risk:** Overdependence on few vendors → potential supply chain disruptions.
- **Action:** Diversify vendor base.

### 3. 📉 Bulk Purchasing:
- Bulk buyers get units at 72% lower cost ($10.78 vs higher unit prices in smaller orders).
- **Benefit:** Encourages high-volume purchases while maintaining profitability.

### 4. 📦 Slow Inventory Movement:
- Unsold Inventory Value: $2.71 million.
- **Problem:** Increases holding costs, reduces cash flow.
- **Action:** Identify low-performing vendors and optimize or liquidate slow-moving stock.

## ✅ Final Recommendations
- Re-evaluate pricing strategies for high-margin but low-sales brands to boost revenue.
- Diversify vendor relationships to mitigate supply chain risk.
- Maximize cost savings through bulk purchasing without overstocking.
- Reduce holding costs by identifying and acting on slow-moving inventory.
- Support underperforming vendors with better distribution and marketing strategies.

## Data Modeling:
![Screenshot 2025-05-30 152029](https://github.com/user-attachments/assets/9e811cc4-7b7a-49a0-be69-2d962be74bbd)


## Dashboard interface:
![Screenshot 2025-05-30 151859](https://github.com/user-attachments/assets/c7b9d9f6-d9a5-4d0e-85a8-211ea25c7908)
