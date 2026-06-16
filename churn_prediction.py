import pandas as pd
from sklearn.linear_model import LogisticRegression

# Load Dataset
df = pd.read_csv("customer_data.csv")

# Features
X = df[["Age", "Tenure", "Balance"]]

# Target
y = df["Churn"]

# Train Model
model = LogisticRegression()

model.fit(X, y)

# Sample Customer
sample = [[30, 3, 20000]]

prediction = model.predict(sample)

if prediction[0] == 1:
    print("Customer Will Leave")
else:
    print("Customer Will Stay")