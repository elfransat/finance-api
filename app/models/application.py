from pydantic import BaseModel, Field
from .applicant import Applicant
from typing import Optional
from ..enums import Status

class ApplicationInput(BaseModel):
    applicant: Applicant
    requested_amount: int = Field(default=1000)
    requested_maturity: int = Field(...)
    purpose: str = Field(...)

class Application(ApplicationInput):
    status: Status = Field(...)
    rejection: Optional[str] = Field(default=None)
    loan_offer: Optional[int] = Field(default=0)

