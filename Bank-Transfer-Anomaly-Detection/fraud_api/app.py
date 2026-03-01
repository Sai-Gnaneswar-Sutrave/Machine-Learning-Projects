from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# Initialize app
app = FastAPI(title="Fraud Detection API")

# Load model at startup
model = joblib.load("model/fraud_isolation_forest_pipeline.pkl")


# Define request schema
class Transaction(BaseModel):
    AccountBalance: float
    CustomerAge: int
    LoginAttempts: int
    TransactionAmount: float
    TransactionDuration: float
    time_since_last_transaction_days: float
    Channel: str
    CustomerOccupation: str
    Location: str
    TransactionType: str


@app.get("/")
def home():
    return {"message": "Fraud Detection API is running"}


@app.post("/predict")
def predict(transaction: Transaction):

    # Convert input to DataFrame
    input_df = pd.DataFrame([transaction.dict()])

    # Prediction
    anomaly_label = model.predict(input_df)[0]
    anomaly_score = model.decision_function(input_df)[0]

    return {
        "anomaly_label": int(anomaly_label),   # -1 or 1
        "anomaly_score": float(anomaly_score),
        "interpretation": "Anomalous Transaction"
        if anomaly_label == -1
        else "Normal Transaction"
    }