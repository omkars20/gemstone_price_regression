from src.data.load_data import load_data
from src.data.preprocess import preprocess
from src.models.train import train_model

print("Starting the training script...")
# Path to your dataset
data_path = '/home/os/kaggle-dataset/gemstone_prediction/src/data/gemstone.csv'
print(f"Loading data from {data_path}...")

# Load the data
data = load_data(data_path)
print("Data loaded successfully.")

# Preprocess the data
print("Preprocessing the data...")
data = preprocess(data)
print("Data after preprocessing:")
print(data.head())

# Train the model and log with MLflow with a custom run name
run_name = "Gemstone Price Regression"
print(f"Training the model with run name '{run_name}'...")
model, X_test, y_test = train_model(data, run_name)
print("Model training completed successfully.")

