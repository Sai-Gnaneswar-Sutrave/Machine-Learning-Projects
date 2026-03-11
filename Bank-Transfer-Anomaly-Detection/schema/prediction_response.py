from pydantic import BaseModel, Field
from typing import Dict

class PredictionResponse(BaseModel):

    '''
    This class defines the structure of the response returned by the API after making a prediction.
    '''
    
    prediction: str = Field(..., description="The predicted class label for the transaction.")
    anomaly_score: float = Field(..., description="The anomaly score for the transaction.")