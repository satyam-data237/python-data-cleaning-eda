import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data.csv")

# Data Cleaning
df.drop_duplicates(inplace=True)
df.fillna(0, inplace=True)

# Basic Analysis
print(df.describe())

# Visualization
df['loan_amount'].hist()
plt.title("Loan Amount Distribution")
plt.xlabel("Loan Amount")
plt.ylabel("Frequency")
plt.show()
