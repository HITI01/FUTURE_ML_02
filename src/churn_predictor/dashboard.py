import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import xgboost as xgb
import os

output_folder = "screenshots/"
os.makedirs(output_folder, exist_ok=True)

print("Loading dataset...")
df = pd.read_csv("data/raw/telecom_churn.csv")
print("Dataset loaded.")

print("Creating churn distribution plot...")
plt.figure(figsize=(5,4))
sns.countplot(x='Churn', data=df)
plt.title('Churned vs Non-Churned')
plt.xticks([0, 1], ["No Churn", "Churn"])
plt.savefig(f"{output_folder}churn_distribution.jpg")
plt.close()
print("Saved churn_distribution.jpg")

print("Creating tenure vs churn plot...")
plt.figure(figsize=(6,4))
sns.boxplot(x='Churn', y='tenure', data=df)
plt.title('Tenure Comparison by Churn')
plt.xticks([0, 1], ["No Churn", "Churn"])
plt.savefig(f"{output_folder}tenure_vs_churn.jpg")
plt.close()
print("Saved tenure_vs_churn.jpg")

print("Creating monthly charges vs churn plot...")
plt.figure(figsize=(6,4))
sns.boxplot(x='Churn', y='MonthlyCharges', data=df)
plt.title('Monthly Charges Comparison by Churn')
plt.xticks([0, 1], ["No Churn", "Churn"])
plt.savefig(f"{output_folder}monthlycharges_vs_churn.jpg")
plt.close()
print("Saved monthlycharges_vs_churn.jpg")

print("Loading XGBoost model...")
model = pickle.load(open("models/xgboost_model.pkl", "rb"))
print("Plotting feature importance...")
xgb.plot_importance(model)
plt.title("Feature Importance (XGBoost)")
plt.savefig(f"{output_folder}xgb_feature_importance.jpg")
plt.close()
print("Saved xgb_feature_importance.jpg")

print("All plots created and saved successfully.")
