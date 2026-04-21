#design data validation for full name
from pydantic import BaseModel, Field, field_validator

class FullName(BaseModel):
    first_name: str = Field(..., pattern=r"^[a-zA-Z]+$", description="The first name of the person")
    last_name: str = Field(..., pattern=r"^[a-zA-Z]+$", description="The last name of the person")

    @field_validator('first_name', 'last_name')
    @classmethod
    def name_must_be_alpha(cls, v):
        if not v.isalpha():
            raise ValueError('must contain only letters')
        return v