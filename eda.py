import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r"D:\new\books.csv")  # <-- full path

# Show first few rows
print("\n📌 FIRST 5 ROWS:")
print(df.head())

# Basic info
print("\n📌 DATA INFO:")
print(df.info())

# Summary statistics
print("\n📌 SUMMARY STATISTICS:")
print(df.describe())

# Check for missing values
print("\n📌 MISSING VALUES:")
print(df.isnull().sum())

# Price distribution
plt.figure(figsize=(8,5))
sns.histplot(df["price"], bins=15, kde=True)
plt.title("Book Price Distribution")
plt.xlabel("Price (£)")
plt.ylabel("Count")
plt.show()

# Boxplot for outliers
plt.figure(figsize=(6,4))
sns.boxplot(x=df["price"])
plt.title("Price Outlier Detection")
plt.show()

# Top 5 most expensive books
print("\n📌 TOP 5 MOST EXPENSIVE BOOKS:")
print(df.sort_values("price", ascending=False).head())

# Cheapest 5 books
print("\n📌 TOP 5 CHEAPEST BOOKS:")
print(df.sort_values("price", ascending=True).head())
