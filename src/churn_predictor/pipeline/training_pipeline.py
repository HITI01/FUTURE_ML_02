from ..components.data_ingestion import ingest_data
from ..components.data_validation import validate_data
from ..components.data_transformation import transform_data
from ..components.model_trainer import train_model
from ..components.model_evaluator import evaluate_model

import pickle
import os

def run_training_pipeline():
    # Step 1: Data ingestion
    df = ingest_data('data/raw/telecom_churn.csv')
    
    # Step 2: Validate data
    validate_data(df)

    # Step 3: Transform data
    categorical_cols = ['gender', 'Partner', 'Contract']
    df = transform_data(df, categorical_cols)

    # Step 4: Prepare features and target
    X = df.drop('Churn', axis=1)
    y = df['Churn']

    # Step 5: Train model and get test set for evaluation
    model, X_test, y_test = train_model(X, y)

    # Step 6: Evaluate model on test set
    evaluate_model(model, X_test, y_test)

    # Step 7: Save trained model
    os.makedirs("models", exist_ok=True)
    with open("models/xgboost_model.pkl", "wb") as f:
        pickle.dump(model, f)
    print("Model saved successfully to models/xgboost_model.pkl")

if __name__ == "__main__":
    run_training_pipeline()
