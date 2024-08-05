import pandas as pd

def preprocess(data: pd.DataFrame) -> pd.DataFrame:
    """Preprocess the data by removing NaNs and standardizing numerical columns."""
    data = data.dropna()
    for col in data.select_dtypes(include='number').columns:
        data[col] = (data[col] - data[col].mean()) / data[col].std()
    return data

