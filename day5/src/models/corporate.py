#create corporate class inherit from customer class
from pydantic import BaseModel, Field
from models.customer import Customer
from models.company_type import CompanyType
class Corporate(Customer):
    company_type: CompanyType = Field(..., description="The type of the company")
    registration_number: str = Field(..., description="The registration number of the company") 