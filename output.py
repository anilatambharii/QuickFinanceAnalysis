import pandas as pd
import matplotlib.pyplot as plt
from FinaneAnalysis import generate_financial_analysis

data = pd.DataFrame({
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
    'Revenue': [10000000, 10500000, 10550000, 10555000],
    'Cost of sales': [600000, 700000, 650000, 800000],
    'Operating expenses': [200000, 250000, 220000, 300000],
    'Net Income': [20000000, 30000000, 25000000, 40000000]
})

business_name = "ABC Corporation"  # your business name

# Generate financial analysis
analysis_output = generate_financial_analysis(data, business_name)

# Plot graphs in a single figure
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Bar chart for Revenue
axes[0, 0].bar(data['Quarter'], data['Revenue'])
axes[0, 0].set_title('Revenue')
axes[0, 0].set_xlabel('Quarter')
axes[0, 0].set_ylabel('Amount')

# Line chart for Profit Margin
profit_margin = data['Revenue'] / (data['Cost of sales'] + data['Operating expenses'])
axes[0, 1].plot(data['Quarter'], profit_margin)
axes[0, 1].set_title('Profit Margin')
axes[0, 1].set_xlabel('Quarter')
axes[0, 1].set_ylabel('Margin')

# Display financial analysis output
axes[1, 0].axis('off')
axes[1, 0].text(0.5, 0.5, analysis_output, horizontalalignment='center', verticalalignment='center', fontsize=12, wrap=True)

# Hide the unused subplot
axes[1, 1].axis('off')

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()
