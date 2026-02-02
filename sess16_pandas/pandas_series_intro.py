# Python script/file to demonstrate how to create, display and access data using pandas series

# Import the required modules
import pandas as pd
#import numpy as np

# 1. Create a series from a list
print("-----1. Create a Pandas Series from a list------")
temperatures = [72,68,75,79,83,77,70]
temp_series = pd.Series(temperatures,name='Daily Temperatures')
print(temp_series)
print(f"Series Name: {temp_series.name}")
print(f"Series Type: {type(temp_series)}")
print(f"Series Data Type (dtype): {type(temp_series.dtype)}")
print("=" *50)

# 2. Create a series with a custom index
print("\n----2. Create a Pandas Series with a custom index ----")
days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
temp_series_indexed = pd.Series(temperatures,index=days, name="Temperature by Day")
print(temp_series_indexed)
print(f"Index values: {temp_series_indexed.index.tolist()}")
print("=" *50)

# 3. Create a series from a dictionary
print("\n----3. Create a Pandas Series from a dictionary ----")
stock_prices = {"Kakuzi":175.25, "Sasini":138.45,"ABSA":327.85,"Equity":145.18}
stock_series = pd.Series(stock_prices, name="Stock Prices")
print(stock_series)
print("=" *50)

# 4. Access the series data
print("\n----4. Accessing Series Data ----")
print(f"Using the index location 'iloc()' function")
print(f"First temperature: {temp_series_indexed.iloc[0]}")
print(f"Last temperature: {temp_series_indexed.iloc[-1]})")
print()
print(f"Using the label index 'loc()' function")
print(f"Monday's temperature: {temp_series_indexed.loc['Mon']}")
print(f"Friday's temperature: {temp_series_indexed.loc['Fri']})")
print("=" *50)

# 5. Series Attributes
print("\n----5. Series Attributes ----")
print(f"Shape: {temp_series.shape}")
print(f"Size: {temp_series.size}")
print(f"Values: {temp_series.values}")
print(f"Index: {temp_series.index}")
print("=" *50)