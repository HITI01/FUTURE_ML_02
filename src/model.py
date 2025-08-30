import xgboost as xgb
from sklearn.model_selection import train_test_split, GridSearchCV

def train_xgb(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)
    params = {
        'max_depth': 6,
        'n_estimators': 200,
        'learning_rate': 0.1,
        'use_label_encoder': False,
        'eval_metric': 'logloss',
        'random_state': 42,
    }
    model = xgb.XGBClassifier(**params)
    model.fit(X_train, y_train)
    return model, X_test, y_test
