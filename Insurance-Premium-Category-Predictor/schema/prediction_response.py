from pydantic import BaseModel, Field
from typing import Dict

class PredictionResponse(BaseModel):
    
    '''
    This class defines the schema for the response returned by the API after making a prediction.
    '''

    predicted_category: str = Field(..., description="The predicted insurance premium category", example='high')
    confidence: float = Field(..., description="The confidence score of the prediction", example=0.8432)
    class_probabilities: Dict[str, float] = Field(..., description="The probabilities for each insurance premium category", example={"Low": 0.01, "Medium": 0.15, "High": 0.84})