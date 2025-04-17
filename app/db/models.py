from app.enums import EmploymentStatus, Status, Purpose
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, JSON

class ApplicantInput(SQLModel):
    first_name: str = Field(description='Applicant first name')
    last_name: str = Field(description='Applicant last name')
    age: int = Field(description='Age of the applicant')
    employment_status: EmploymentStatus = Field(default=EmploymentStatus.UNEMPLOYED, description='Applicants Employment Status')
    address: str = Field(..., min_length=5, max_length=128)
    postcode: str = Field(..., description='5-digit Finnish postcode')
    phone_number: str = Field(..., description='10-digit Finnish phone number')
    income: int = Field(..., description='Income from the last 12 months')
    ssn: str = Field(..., description='SSN in the format DDMMYY-CZZZQ')

class Applicant(ApplicantInput, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    applications: List["Application"] = Relationship(back_populates="applicant")

class ApplicationInput(SQLModel):
    requested_amount: int
    requested_maturity: int
    purpose: Purpose = Field()

class Application(ApplicationInput, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    applicant_id: Optional[int] = Field(default=None, foreign_key="applicant.id")
    status: Status = Field(default=Status.PROCESSING)
    rejections: Optional[List[str]] = Field(default=None, sa_column=Column(JSON))
    loan_offer: Optional[int] = Field(default=0)
    applicant: Applicant = Relationship(back_populates="applications")

class CompleteApplicationInput(SQLModel):
    applicant: ApplicantInput
    application: ApplicationInput