import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess(data: pd.DataFrame) -> pd.DataFrame:
    """Preprocess the data by removing NaNs and encoding categorical columns."""
    data = data.dropna()
    
    # Encode categorical columns
    for col in data.select_dtypes(include='object').columns:
        encoder = LabelEncoder()
        data[col] = encoder.fit_transform(data[col])
    
    # Standardize numerical columns
    for col in data.select_dtypes(include='number').columns:
        data[col] = (data[col] - data[col].mean()) / data[col].std()

    print("Data after preprocessing:")
    print(data.head())
    
    return data


