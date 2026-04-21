#create class individual using pydantic
from models.customer import Customer
from models.gender import Gender
from pydantic import BaseModel, Field
from pydantic import validator as FieldValidator
from datetime import date 

class Individual(BaseModel):
    gender: Gender
    dob: date = Field(..., description="The date of birth of the individual")

    @FieldValidator('dob')
    def validate_dob(cls, value):
        if value > date.today():
            raise ValueError('Date of birth cannot be in the future')
        return value
        age=(date.today()-value).days//365
        if age<18:
            raise ValueError('Individual must be at least 18 years old')
        return value
    
    
