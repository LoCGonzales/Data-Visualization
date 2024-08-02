print("Financial Analysis")
print("-----------------")

import os
import csv
import pandas as pd

# Define the path to the CSV file
budget_csv = os.path.join('PyBank', 'Resources', 'budget_data.csv')

# Read the CSV file into a DataFrame
df = pd.read_csv(budget_csv)

# Calculate the number of months
number_of_months = len(df)
print(f"Total months: {number_of_months}")

# Calculate the total amount of Profit/Losses
total_amount = df["Profit/Losses"].sum()
print(f"Total: ${total_amount:,.0f}")

# Calculate the monthly change in Profit/Losses
df['Change'] = df['Profit/Losses'].diff()

# Calculate the average change
average_change = df['Change'].mean()
print(f"Average Change: ${average_change:.2f}")

# Find the greatest increase in profits
max_increase = df.loc[df['Change'].idxmax()]
print(f"Greatest Increase in Profits: {max_increase['Date']} (${max_increase['Change']:,.0f})")

# Find the greatest decrease in profits
max_decrease = df.loc[df['Change'].idxmin()]
print(f"Greatest Decrease in Profits: {max_decrease['Date']} (${max_decrease['Change']:,.0f})")