# Sales Data Analysis Using Python
# BCA 6th Semester Project

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("dataset/sales.csv")

# Display first 5 records
print("First 5 Records:")
print(data.head())

# Data cleaning
data.drop_duplicates(inplace=True)

# Create Total_Sales column
data['Total_Sales'] = data['Quantity'] * data['Price']

# Total sales
total_sales = data['Total_Sales'].sum()
print("\nTotal Sales:", total_sales)

# Category-wise sales
category_sales = data.groupby('Category')['Total_Sales'].sum()
print("\nCategory-wise Sales:")
print(category_sales)

# Visualization
category_sales.plot(kind='bar')
plt.title("Category-wise Total Sales")
plt.xlabel("Category")
plt.ylabel("Sales Amount")
plt.show()
