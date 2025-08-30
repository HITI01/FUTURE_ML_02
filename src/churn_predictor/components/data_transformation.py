from sklearn.preprocessing import LabelEncoder

def transform_data(df, categorical_cols):
    le = LabelEncoder()
    for col in categorical_cols:
        df[col] = le.fit_transform(df[col])
    return df
