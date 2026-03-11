import pickle
import pandas as pd
from pathlib import Path


MODEL_PATH = Path(__file__).parent / "fraud_isolation_forest_pipeline.pkl"

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

MODEL_VERSION = "1.0.0"

# Class labels for anomaly detection
class_labels = {-1: "Anomalous", 1: "Normal"}


def predict_anomaly(user_input: dict) -> dict:
    
    '''
    This function prepares the input data, sends it to the trained model,
    and returns whether the transaction is normal or anomalous.
    '''

    # Convert input dictionary to DataFrame
    input_data = pd.DataFrame([user_input])

    # Predict anomaly class
    predicted_class = model.predict(input_data)[0]

    # Get anomaly score
    anomaly_score = model.decision_function(input_data)[0]

    # Map numeric prediction to readable label
    prediction_label = class_labels[predicted_class]

    return {
        "prediction": prediction_label,
        "anomaly_score": round(float(anomaly_score), 4)
    }
