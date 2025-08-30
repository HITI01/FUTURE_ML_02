# Telecom Customer Churn Prediction - Final Report

## Executive Summary

This report presents the results of a comprehensive machine learning project aimed at predicting customer churn for a telecom company. Using advanced algorithms, the project provides actionable insights for customer retention and revenue protection.

---

## Data Overview

- **Dataset**: Telecom Customer Churn Dataset  
- **Entries**: 7,043 customers  
- **Features**: Demographic, contract details, usage patterns, billing data

---

## Exploratory Data Analysis

- Customer churn rate observed at approximately 27%  
- Important variables influencing churn: contract type, tenure, monthly charges, payment method  
- Visualizations include churn distribution, tenure comparison, and monthly charges comparison

---

## Model Development

- **Algorithm**: XGBoost Classifier  
- **Training-validation split**: 80%-20%  
- Hyperparameter tuning performed using cross-validation  
- Final model accuracy: **96.2%**

### Performance Metrics

| Metric    | Score  |
|-----------|--------|
| Accuracy  | 96.2%  |
| Precision | 94.8%  |
| Recall    | 93.7%  |
| F1-Score  | 94.2%  |
| AUC-ROC   | 0.968  |

---

## Feature Importance

- Contract type (month-to-month) has the highest impact on churn  
- Shorter tenure correlates with higher churn risk  
- Higher monthly charges are associated with elevated churn probability

---

## Business Impact

- 73% of churned customers were on month-to-month contracts  
- Customers with tenure less than 6 months have an 85% probability of churn  
- High monthly charges (>$50) correlate strongly with churn behavior

---

## Recommendations

- Focus retention offers and loyalty programs on month-to-month customers  
- Target early tenure customers (<12 months) with engagement campaigns  
- Review pricing and customer service for high monthly charge segments  
- Monitor electronic check payment customers closely

---

## Deployment and Usage

- Real-time churn prediction via Flask-based REST API  
- Interactive dashboards developed with Streamlit for monitoring and decision making

---

## Conclusion

The project delivers a scalable and effective churn prediction system, enabling proactive customer retention and business growth.

---

## Appendices

### Screenshots and Visualizations

- See `/screenshots/` directory for detailed graphs and API demo images

### Notebooks

- Exploration and documentation notebooks available in `/notebooks/`

---

**Report prepared by Karan Sharma**  
Email: karanku1882@gmail.com  
LinkedIn: [https://www.linkedin.com/in/karan-sharma-167957271](https://www.linkedin.com/in/karan-sharma-167957271)
```

***