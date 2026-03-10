from fastapi import FastAPI
from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Annotated, Literal, Optional

from config.city_tier import tier_1_cities, tier_2_cities

class UserInput(BaseModel):

    '''
    This class defines the schema for the input data required to predict the insurance premium category.
    '''

    age: Annotated[int, Field(..., gt=0, lt=100, description="Age of the user")]
    weight: Annotated[float, Field(..., gt=0, description="Weight of the user")]
    height: Annotated[float, Field(..., gt=0, lt=2.5, description="Height of the user")]
    income_lpa: Annotated[float, Field(..., gt=0, description="Annual income of the user in LPA")]
    smoker: Annotated[bool, Field(..., description='Is the user smoker?')]
    city: Annotated[str, Field(..., description='City that the user belongs to')]
    occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'], Field(..., description='Occupation of the user')]
    

    @computed_field
    @property
    def bmi(self) -> float:
        '''
        This method calculates the BMI of the user based on the weight and height.
        '''
        return self.weight / (self.height ** 2)
    

    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 18:
            return 'young'
        elif self.age < 25:
            return 'young_adult'
        elif self.age < 45:
            return 'adult'
        elif self.age < 60:
            return 'middle_aged'
        else:
            return 'senior_citizen'
        
    
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker == True and self.bmi > 30:
            return 'high'
        elif self.smoker == True or self.bmi > 25:
            return 'medium'
        elif self.smoker == False and self.bmi < 25:
            return 'low'
        else:
            return 'medium'
        
    
    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3
        
    
    @field_validator('city')
    def normalize_city(cls, value: str) -> str:
        
        '''
        This method normalizes the city name by stripping leading/trailing whitespace and converting it to title case.
        '''
        
        return value.strip().title()