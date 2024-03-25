
'''
Use case: 
Financial Analysis: Using GenAI to automate financial analysis. Quickly analyze financial data, identify trends and patterns,
and provide insights into the financial health of the organization. This can save time and reduce costs associated with financial analysis

In this code snippet, the function AnalyzeFinancials takes a pandas DataFrame called 'data' as input and generates a string
with financial insights such as metrics, trends, and actionable opportunities and threats based on the given data.

The function first prints out the key financial metrics including total sales, average quarterly sales, total cost, net income (Q4), 
and return on investment (ROI).

Next, it categorizes various financial metrics into increasing trends, decreasing trends, and stable metrics. 
It compares the most recent value of each metric to its previous value and determines whether the trend is increasing, decreasing, or stable.
The results are stored in separate lists for further reference.

Then, the function provides an output string that summarizes the trends and patterns observed in the financial data. 
It provides the detailed analysis of each metric based on its trend, such as if a metric is increasing, decreasing, or stable.

Finally, the function generates two more lists: 'opportunities' and 'threats'. Based on the trends observed in the data, 
it suggests potential actions that can be taken to improve the business. For example, if there have been decreasing trends in revenue 
or profit margin, it provides suggestions such as introducing new products or services to boost sales or exploring cost reduction 
strategies to maintain profitability.

These opportunities and threats are stored in separate lists and then used to create a summary of actionable recommendations
for improvement. The function ultimately returns the output string containing all the financial insights gained from the analysis. 
Through this analysis, users can gain a better understanding of their current financial situation and possible steps to take for 
future growth and success.

'''
# Import necessary libraries and package
import pandas as pd
import pygal

def generate_financial_analysis(data: pd.DataFrame, business_name: str):
    output = ""

    # Create bar graph of income statement over time
    data.plot(x="Quarter", y='Revenue', kind="bar")
    output += f"Financial Analysis for {business_name}\n" \
              f"\nIncome Statement:\n" \
              f"{data.plot(x='Quarter', y='Revenue', kind='bar').figure}\n"

    # Create line chart of profit margin over time
    data['Profit Margin'] = data['Revenue'] / (data['Cost of sales'] + data['Operating expenses'])
    data.plot(x="Quarter", y='Profit Margin', kind="line")
    output += "\n\nProfit Margin:\n"
    output += f"{data.plot(x='Quarter', y='Profit Margin', kind='line').figure}\n"

    # Calculate and display key financial metrics
    total_sales = data['Revenue'].sum()
    avg_sales = data['Revenue'].mean()
    total_cost = data['Cost of sales'].sum()
    net_income = data[data['Quarter'] == 'Q4']['Net Income'].values[0]
    roi = net_income / total_sales * 100

    output += "\n\nKeyMetrics:\n" \
              f"Total Sales: {total_sales},\n" \
              f"Average Quarterly Sales: {avg_sales},\n" \
              f"Total Cost: {total_cost},\n" \
              f"Net Income (Q4): ${net_income},\n" \
              f"Return on Investment (ROI): {roi}%\n"

    # Identify trends and patterns in financial data
    increasing_trends = ["Revenue", "Profit Margin"]
    decreasing_trends = []
    stable_metrics = []

    for metric in increasing_trends:
        current_value = data[metric].iloc[-1]
        comparison_value = data[metric].iloc[-2]
        if current_value > comparison_value:
            output += f"\n\nTrends and Patterns:\n" \
                      f"{metric} has been increasing over time and is currently at ${current_value} (from ${comparison_value})\n"
        else:
            decreasing_trends.append(metric)

    for metric in decreasing_trends:
        current_value = data[metric].iloc[-1]
        comparison_value = data[metric].iloc[-2]
        if current_value < comparison_value:
            output += f"\n{metric} has been decreasing over time and is currently at ${current_value} (from ${comparison_value})\n"
        else:
            stable_metrics.append(metric)

    for metric in stable_metrics:
        output += f"\n{metric} has remained relatively stable, with values hovering around ${data[metric].mean()}\n"

    # Provide actionable insights based on the analysis
    opportunities = []
    threats = []

    if "Revenue" in decreasing_trends:
        opportunities.append("Consider introducing new products or services to boost sales.")
        threats.append("Lower sales may lead to reduced profits and potentially affect business sustainability.")
    if "Profit Margin" in stable_metrics:
        opportunities.append("Explore new markets or pricing strategies to maintain profit margins while driving growth.")

    if len(opportunities) > 0:
        output += "\n\nOpportunities for Improvement:\n"
        for opportunity in opportunities:
            output += f"- {opportunity}\n"

    if len(threats) > 0:
        output += "\nThreats and Challenges:\n"
        for threat in threats:
            output += f"- {threat}\n"

    return output



