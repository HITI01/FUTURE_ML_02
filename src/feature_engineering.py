import pandas as pd

def create_features(df):
    df['tenure_group'] = pd.cut(df['tenure'], bins=[0,12,24,36,60,100], labels=['<1yr','1-2yr','2-3yr','3-5yr','5yr+'])
    df['monthly_avg'] = df['TotalCharges'] / (df['tenure'] + 1)
    return df
