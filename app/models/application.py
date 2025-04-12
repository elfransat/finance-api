from pydantic import BaseModel, Field
from .applicant import Applicant
from ..enums import Status

class Application(BaseModel):
    applicant: Applicant = Field(...)
    requested_amount: int = Field(default=1000)
    requested_maturity: int = Field(...)
    purpose: str = Field(...)
    status: Status = Field(...)
