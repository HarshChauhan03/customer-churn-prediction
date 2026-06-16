import pandas as pd

# Sample Dataset

data = {
    "Age": [25, 40, 35, 50, 28],
    "Tenure": [1, 8, 5, 10, 2],
    "Balance": [10000, 80000, 50000, 120000, 15000],
    "Churn": [1, 0, 0, 0, 1]
}

df = pd.DataFrame(data)

print(df)

df.to_csv(
    "customer_data.csv",
    index=False
)

print("Dataset Saved Successfully")