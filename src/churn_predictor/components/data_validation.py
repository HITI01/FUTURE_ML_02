def validate_data(df):
    if df.empty:
        raise ValueError("Dataframe is empty")
    if df.isnull().sum().sum() > 0:
        raise ValueError("Missing values present in dataframe")
    return True
