from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Annotated, Literal

from datetime import datetime

class UserInput(BaseModel):

    '''
    This class defines the structure of the user input for the bank transfer anomaly detection model. It includes various fields that capture relevant information about the transaction and the customer. Each field is annotated with its type and includes validation rules to ensure that the input data is in the correct format and meets certain criteria. The class also includes a computed field to calculate the time since the last transaction in days, and a validator to normalize the location input.
    '''

    accountBalance: Annotated[float, Field(..., description='The current balance of the user\'s bank account.')]
    customerAge: Annotated[int, Field(..., ge=0, description='The age of the customer. Must be a non-negative integer.')]
    loginAttempts: Annotated[int, Field(..., ge=0, description='The number of login attempts made by the user. Must be a non-negative integer.')]
    transactionAmount: Annotated[int, Field(..., gt=0, description='The amount of the transaction. Must be a positive integer.')]
    transactionDuration: Annotated[int, Field(..., ge=0, description='The duration of the transaction in seconds. Must be a non-negative integer.')]
    transactionDate: Annotated[datetime, Field(..., description='The date and time when the transaction occurred. Must be in ISO 8601 format (YYYY-MM-DDTHH:MM:SS).')]
    recentTransactionDate: Annotated[datetime, Field(..., description='The date and time of the previous transaction. Must be in ISO 8601 format (YYYY-MM-DDTHH:MM:SS).')]
    channel: Annotated[Literal['ATM', 'Branch', 'Online'], Field(..., description='The channel through which the transaction was made. Must be one of "ATM", "Branch", or "Online".')]
    customerOccupation: Annotated[Literal['Doctor', 'Engineer', 'Retired', 'Student'], Field(..., description='The occupation of the customer. Must be one of "Doctor", "Engineer", "Retired", or "Student".')]
    location: Annotated[str, Field(..., description='The location from which the transaction was made.')]
    transactionType: Annotated[Literal['Credit', 'Debit'], Field(..., description='The type of the transaction. Must be one of "Credit", "Debit".')]


    @computed_field
    @property
    def time_since_last_transaction_days(self) -> int:

        '''
        This computed field calculates the time since the last transaction in days. It takes the difference between the recentTransactionDate and the transactionDate, and returns the number of days as an integer.
        '''

        try:
            delta = self.recentTransactionDate - self.transactionDate
            return max(delta.days, 0)
        except ValueError:
            raise ValueError("Invalid date format. Dates must be in ISO 8601 format (YYYY-MM-DDTHH:MM:SS).")
        
    
    @field_validator('location')
    def normalize_location(cls, value: str) -> str:

        '''
        This validator normalizes the location input by stripping whitespace and capitalizing the first letter of each word.
        '''

        return value.strip().title()