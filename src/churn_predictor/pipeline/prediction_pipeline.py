from churn_predictor.components.data_transformation import transform_data
import pickle
import pandas as pd

def predict_single(sample_dict):
    model = pickle.load(open("models/xgboost_model.pkl", "rb"))  # update path if needed
    sample_df = pd.DataFrame([sample_dict])
    # Perform necessary transformation if required
    sample_df = transform_data(sample_df, ['gender', 'Partner', 'Contract'])
    pred = model.predict(sample_df)
    return int(pred[0])

if __name__ == "__main__":
    # Example usage
    test_data = {
        "gender": "Male",
        "Partner": "Yes",
        "Contract": "Month-to-month",
        "tenure": 12,
        "MonthlyCharges": 29.85,
        "TotalCharges": 350.5
    }
    print("Prediction:", predict_single(test_data))
