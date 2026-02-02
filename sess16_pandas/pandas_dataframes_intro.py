# Python script/file to introduce Pandas Dataframes by demonstrating how to
# create, display and explore them.

# Import the required modules
import pandas as pd
#import numpy as np

# 1. Create a Data frame from a dictionary
print("----1. Create a Data frame from a dictionary ----")
data = {
    'Name': ['Abigail','Kamau','Sharlene','Diana','Mueni'],
    'Age': [25,30,35,28,32],
    'City': ['Nakuru','Limuru','Kisumu','Homabay','Makueni'],
    'Salary': [55000,65000,72000,48000,60000],
    'Department': ['HR','IT','IT','Marketing','Finance']
}

df = pd.DataFrame(data)
print(f"Employees Details dataframe created from dictionary:\n{df}")
print("=" * 50 + "\n")

# 2. Create a Dataframe with custom index
print("----2. Create a Dataframe with custom index ----")
df_indexed = pd.DataFrame(data,index=['Emp1','Emp2','Emp3','Emp4','Emp5'])
print(f"Employees Details dataframe with custom index:\n{df_indexed}")
print("=" * 50 + "\n")

# 3. Dataframe attributes and information
print("----3. Dataframe attributes and information ----")
print(f"Shape: {df.shape}") # rows, columns
print(f"Columns: {df.columns.tolist()}")
print(f"Index: {df.index.tolist()}")
print(f"Data types: {df.dtypes}")
print("=" * 50 + "\n")

# 4. Display methods 'head()' & 'tail()'
print("----4. Display methods 'head()' & 'tail()' ----")
print(f"First 3 rows of employee details using 'head()'\n{df.head(3)}")
print(f"Last 2 rows of employee details using 'tail()'\n{df.tail(2)}")
print("=" * 50 + "\n")

# 5. Accessing Date from a Dataframe
print("----5. Accessing Date from a Dataframe ----")
print("Single column (Series):")
print(f"{df['Name']}\n")
print(f"Multiple columns:\n{df[['Name','Age','Department']]}")
print(f"\nAccess by index position (iloc):")
print(f"First row: \n{df.iloc[0]}")
print(f"Specific cell (row 2, column 'Age'):\n{df.iloc[1,1]}")
print(f"Access by label (loc):\nEmployee with index 2:\n{df.loc[2]}")
print("=" * 50 + "\n")

# 6. Create a Dataframe from a list of lists
print("----6. Create a Dataframe from a list of lists ----")
product_data = [
    ['Laptop', 99999.5, 'Electronics', 50],
    ['Mouse', 250.0, 'Electronics', 200],
    ['Notebook', 599.0, 'Stationary', 150],
    ['Pen', 199.0, 'Stationary', 500]
]
product_columns = ['Product', 'Price', 'Category', 'Stock']
product_df = pd.DataFrame(product_data, columns=product_columns)
print(f"Product DataFrame:\n{product_df}")
print("=" * 50 + "\n")