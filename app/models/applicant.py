from pydantic import BaseModel, Field
from ..enums import EmploymentStatus

class Applicant(BaseModel):
    age: int = Field(..., description='Age of the applicant')
    first_name: str = Field(..., description='Applicant’s first name')
    last_name: str = Field(..., description='Applicant’s last name')
    employment_status: EmploymentStatus = Field(default=EmploymentStatus.UNEMPLOYED)
    address: str = Field(..., min_length=5, max_length=128)
    postcode: int = Field(..., description='5-digit Finnish postcode')
    phone_number: int = Field(..., description='10-digit Finnish phone number')
    income: int = Field(..., description='Income from the last 12 months')