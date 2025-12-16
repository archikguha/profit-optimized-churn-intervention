
def preprocess(df):
    df = df.copy()
    cat_cols = ["contract_type", "internet_service", "payment_method"]
    for c in cat_cols:
        df[c] = df[c].astype("category").cat.codes

    for col in df.columns:
        if df[col].isna().any():
            df[col] = df[col].fillna(df[col].median())
    return df
