# For categorical variables
for col in df.columns:
    if df[col].dtype == 'object':
        print(f"{col} - Unique values: {df[col].unique()}")
