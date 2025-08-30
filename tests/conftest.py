import pytest
import pandas as pd

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'gender': ['Male', 'Female'],
        'Partner': ['Yes', 'No'],
        'Contract': ['Month-to-month', 'One year'],
        'tenure': [10, 24],
        'MonthlyCharges': [29.85, 56.95],
        'TotalCharges': [350.5, 1889.5],
        'Churn': [0, 1]
    })
