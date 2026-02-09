# Python script to demonstrate various operations on pandas dataframes
# like filtering, grouping, merging and other dataframe operations

# Import the required modules
import pandas as pd
import numpy as np

# 1. Create a sample employee dataframe
print("---- 1. Create a sample employee dataframe ----")
employees = pd.DataFrame({
    'EmployeeID': [1001,1002,1003,1004,1005],
    'Name': ['Abigail', 'Kamau', 'Sharlene', 'Diana', 'Mueni'],
    'Department': ['HR', 'IT', 'IT', 'Marketing', 'Finance'],
    'Salary': [55000, 65000, 72000, 48000, 60000],
})

# Create a sales dataframe
sales = pd.DataFrame({
    'EmployeeID': [1001,1002,1003,1004,1005],
    'Q1_Sales': [15000, 22000, 18000, 12000, 25000],
    'Q2_Sales': [18000, 24000,21000, 14000, 28000],
    'Q3_Sales': [22000, 25000, 22500, 15500, 32000],
})

# Display the employee and sales dataframes
print("Employee Dataframe".center(55,'-'))
print(employees)
print()
print("Sales Dataframe".center(55,'-'))
print(sales)
print("=" *50 + '\n')

# 2. Merge the 2 dataframes (i.e. Employee & Sales on EmployeeID)
print("---- 2. Merge the 2 dataframes (i.e. Employee & Sales on EmployeeID) ----")
combined = pd.merge(employees, sales, on='EmployeeID')
print("Merged employee & sales dataframe".center(55,'-'))
print(combined)
print("=" *50 + '\n')

# 3. Adding calculated columns
print("---- 3. Adding calculated columns ----")
combined['Total_Sales'] = combined['Q1_Sales'] + combined['Q2_Sales'] + combined['Q3_Sales']
combined['Avg_Sales'] = combined['Total_Sales']/3.0
combined['Bonus'] = combined['Total_Sales'] * .02
print(f"Dataframe with calculated columns: \n{combined}")
print("=" *50 + '\n')

# 4. Filtering Employee data
print("---- 4. Filtering Employee data ----")
print("Employees in IT department:")
IT_employees = employees.loc[employees['Department'] == 'IT']
#it_employees = combined[combined['Department'] == 'IT']
print(IT_employees)
print("\nEmployees earning more than 60000:")
high_salary = employees.loc[employees['Salary'] > 60000]
print(high_salary)
print("=" *50 + '\n')

# 5. Grouping & aggregating data
print("---- 5. Grouping & aggregating data ----")
department_stats = combined.groupby(['Department']).agg({
    'Salary': ['mean', 'sum', 'min', 'max'],
    'Total_Sales':['mean','sum'],
    'EmployeeID': ['count']
}).round(2)
print("Department Statistics".center(55,'-'))
print(department_stats)
print("=" *50 + '\n')

# 6. Sorting data
print("----6. Sorting Data ----")
print("Sorted by Total Sales (descending):")
sorted_by_sales = combined.sort_values('Total_Sales', ascending=False)
print(sorted_by_sales[['Name', 'Department', 'Total_Sales', 'Salary']])
print("=" *50 + '\n')

# 7. Pivot tables
print("----7. Pivot Table ----")
# Create a longer format for pivot example
long_data = pd.DataFrame({
    'Name': ['Alice', 'Alice', 'Bob', 'Bob', 'Charlie', 'Charlie'],
    'Quarter': ['Q1', 'Q2', 'Q1', 'Q2', 'Q1', 'Q2'],
    'Sales': [15000, 18000, 22000, 24000, 18000, 21000]
})

print("Original long data:")
print(long_data)
print()
pivot_table = long_data.pivot_table(
    index='Name',
    columns='Quarter',
    values='Sales',
    aggfunc='sum'
)
print("Pivot table:")
print(pivot_table)
print("=" *50 + '\n')

# 8. Handling missing data
print("----8. Handling Missing Data ----")
df_with_na = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [5, None, None, 8],
    'C': [9, 10, 11, 12]
})

print("DataFrame with missing values:")
print(df_with_na)
print()

print("Fill missing values with column mean:")
filled_df = df_with_na.fillna(df_with_na.mean())
print(filled_df)
print("=" *50 + '\n')

# 9. Statistical summary
print("----9. Statistical Summary ----")
print("Summary statistics for combined DataFrame:")
print(combined.describe())
print("=" *50 + '\n')