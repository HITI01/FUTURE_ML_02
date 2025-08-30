import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
import xgboost as xgb

st.title("Telecom Churn Prediction Insights Dashboard")

# Load dataset
df = pd.read_csv("data/raw/telecom_churn.csv")

st.header("Churned vs Non-Churned Distribution")
fig1, ax1 = plt.subplots()
sns.countplot(x='Churn', data=df, ax=ax1)
ax1.set_xticklabels(["No Churn", "Churn"])
st.pyplot(fig1)

st.header("Tenure Comparison by Churn")
fig2, ax2 = plt.subplots()
sns.boxplot(x='Churn', y='tenure', data=df, ax=ax2)
ax2.set_xticklabels(["No Churn", "Churn"])
st.pyplot(fig2)

st.header("Monthly Charges Comparison by Churn")
fig3, ax3 = plt.subplots()
sns.boxplot(x='Churn', y='MonthlyCharges', data=df, ax=ax3)
ax3.set_xticklabels(["No Churn", "Churn"])
st.pyplot(fig3)

st.header("Feature Importance (XGBoost Model)")
model = pickle.load(open("models/xgboost_model.pkl", "rb"))
fig4, ax4 = plt.subplots(figsize=(8,6))
xgb.plot_importance(model, ax=ax4)
st.pyplot(fig4)
