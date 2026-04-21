#create customer class using pydantic
from pydantic import BaseModel, Field
from .full_name import FullName

class Customer(BaseModel):
    customer_id: int=Field(...,gt=0, description="The unique identifier for the customer")
    name: FullName
    email: str=Field(..., pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', description="The email address of the customer")
    phone_no: int=Field(..., ge=1000000000,le=99999999999, description="The phone number of the customer")
