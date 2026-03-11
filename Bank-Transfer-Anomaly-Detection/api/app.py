from fastapi import FastAPI
from fastapi.responses import JSONResponse

import warnings
warnings.filterwarnings("ignore")

from schema.user_input import UserInput
from schema.prediction_response import PredictionResponse
from model.predict import predict_anomaly, model, MODEL_PATH, MODEL_VERSION

app = FastAPI()

@app.get('/', include_in_schema=False, summary="Home Endpoint", description="This is the home endpoint of the Bank Transfer Anomaly Detection API.")
def home():
    return JSONResponse(content={"message": "Welcome to the Bank Transfer Anomaly Detection API!"})


@app.get('/health', include_in_schema=False, summary="Health Check Endpoint", description="This endpoint checks the health status of the API.")
def health_check():
    return JSONResponse(status_code=200, 
                        content={'status': 'OK', 
                                 'version': MODEL_VERSION, 
                                 'model_loaded': model is not None, 
                                 'model_path': str(MODEL_PATH)})


@app.post('/predict', response_model=PredictionResponse, summary="Predict Anomaly Endpoint", description="This endpoint takes in transaction data and returns a prediction of whether the transaction is anomalous along with an anomaly score.")
def predict(user_input: UserInput) -> PredictionResponse:
    try:
        user_input = {
            "AccountBalance": user_input.accountBalance,
            "CustomerAge": user_input.customerAge,
            "LoginAttempts": user_input.loginAttempts,
            "TransactionAmount": user_input.transactionAmount,
            "TransactionDuration": user_input.transactionDuration,
            "time_since_last_transaction_days": user_input.time_since_last_transaction_days,
            "Channel": user_input.channel,
            "CustomerOccupation": user_input.customerOccupation,
            "Location": user_input.location,
            "TransactionType": user_input.transactionType,
        }

        result = predict_anomaly(user_input)

        return PredictionResponse(
            prediction=result["prediction"],
            anomaly_score=result["anomaly_score"]
        )
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})