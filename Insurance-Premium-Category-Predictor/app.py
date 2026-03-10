from fastapi import FastAPI
from fastapi.responses import JSONResponse

import warnings
warnings.filterwarnings("ignore")

from schema.user_input import UserInput
from schema.prediction_response import PredictionResponse
from model.predict import predict_premium_category, model, MODEL_VERSION


app = FastAPI()


# Home endpoint to check if the API is working
@app.get('/', include_in_schema=False, summary="Home Endpoint", description="This endpoint is used to check if the API is working. It returns a welcome message.")
def home():
    return JSONResponse(status_code=200, content={'message': 'Welcome to the Insurance Premium Category Predictor API!'})


# Health check endpoint to check if the API is healthy (For services like AWS, Azure, GCP, etc. to monitor the health of the API)
@app.get('/health', include_in_schema=False, summary="Health Check Endpoint", description="This endpoint is used to check the health of the API. It returns the status of the API along with the model version and whether the model is loaded successfully.")
def health_check():
    return JSONResponse(status_code=200, content={'status': 'OK', 'version': '1.0.0', 'model_loaded': model is not None})


# API endpoint to predict the insurance premium category
@app.post('/predict', response_model=PredictionResponse, summary="Predict Insurance Premium Category", description="This endpoint takes the input data and returns the predicted insurance premium category along with confidence scores.")
def predict(data: UserInput) -> PredictionResponse:
    
    '''
    This endpoint takes the input data, processes it, and returns the predicted insurance premium category.
    '''
    
    user_input = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }

    try:
        # Predict the insurance premium category using the loaded model
        prediction = predict_premium_category(user_input)
        return JSONResponse(status_code=200, content={'response': prediction})
    except Exception as e:
        return JSONResponse(status_code=500, content={'error': str(e)})