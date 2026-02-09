# Python script to demonstrate outlier detection and handling using IQR(Interquartile Range)

# Import the required modules
import pandas as pd
import numpy as np

# 1. Create a sample dataset
data = {
   'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
   'Age': [5, 35, 32, 39, 45, 120, 28 ],  # '120' & 5 are outliers
   'Salary': [50000, 2500, 54000, 52000, 110000, 47000, 51000]  # '2500' & '110000' are outliers
}

# 2. Conver the above dictionary into a pandas dataframe
df = pd.DataFrame(data)

# 3. Display the original dataframe
print(f"\nOriginal DataFrame:\n{df}")

# 4. Detect outliers using IQR method for the 'Age' column
Q1 = df['Age'].quantile(0.25) # First quartile (Q1)
Q3 = df['Age'].quantile(0.75) # Third quartile (Q3)
IQR = Q3 - Q1 # Get the interquartile
lower_bound = Q1 - 1.5*IQR
upper_bound = Q3 + 1.5*IQR

# TODO: Detect outliers using the IQR method for 'Salary' column

# Identify and display the outliers for the 'Age' column
outliers  = df[(df['Age'] < lower_bound) | (df['Age'] > upper_bound)]
print(f"Detected Outliers for the 'Age' column:\n{outliers}")

# 5. Handle the outliers -> method (i) Remove/drop the outliers
df_no_age_outliers = df[(df['Age'] >= lower_bound) & (df['Age'] <= upper_bound)]
# Display the dataset after removing the outliers for the 'Age' column
print(f"\nDataset after removing outliers for the 'Age' column:\n{df_no_age_outliers}")

# 6. Handle the outliers -> method (ii) Cap the outliers
df['Age'] = np.where(df['Age'] < lower_bound,lower_bound,np.where(df['Age'] > upper_bound,upper_bound,df['Age']))
# Display the dataset after capping outliers for the 'Age' column
print(f"\nDataset after capping outliers for the 'Age' column:\n{df}")