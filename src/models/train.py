import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import mlflow
import mlflow.sklearn

def train_model(data: pd.DataFrame, run_name: str):
    print("Setting MLflow tracking URI...")
    # Set MLflow tracking URI to a local directory
    mlflow.set_tracking_uri("file:///tmp/mlruns")

    print("Splitting data into training and test sets...")
    X = data.drop('price', axis=1)
    y = data['price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("Initializing Linear Regression model...")
    model = LinearRegression()

    with mlflow.start_run() as run:
        print(f"Starting MLflow run with ID: {run.info.run_id} and name: {run_name}...")
        mlflow.set_tag("mlflow.runName", run_name)

        print("Training the model...")
        model.fit(X_train, y_train)

        print("Logging parameters to MLflow...")
        mlflow.log_param("random_state", 42)
        mlflow.log_param("test_size", 0.2)

        # Provide input example for model signature
        input_example = X_train.head(1)
        print("Logging the model to MLflow...")
        mlflow.sklearn.log_model(model, "model", input_example=input_example)

        score = model.score(X_test, y_test)
        print(f"Model score: {score}")
        print("Logging metrics to MLflow...")
        mlflow.log_metric("score", score)

    print("MLflow run completed.")
    return model, X_test, y_test




