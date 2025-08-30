class Config:
    RAW_DATA_PATH = "data/raw/telecom_churn.csv"
    PROCESSED_DATA_PATH = "data/processed/telecom_churn_clean.csv"
    MODEL_SAVE_PATH = "models/xgboost_model.pkl"
    RANDOM_STATE = 42
    TEST_SIZE = 0.2
    XGB_PARAMS = {
        'use_label_encoder': False,
        'eval_metric': 'logloss',
        'max_depth': 6,
        'n_estimators': 200,
        'learning_rate': 0.1,
        'random_state': 42,
    }
