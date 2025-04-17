import validators
from app.enums import EmploymentStatus, Purpose
from app.db.models import Application, Applicant
from typing import List

def validate_application(application: Application, applicant: Applicant) -> List[str]:
    """Return a list of reasons why an application should be rejected, or empty list if valid"""
    rejection_reasons = []
    
    if application.requested_amount <= 1000:
        rejection_reasons.append('Request amount < 1000')
    
    if not validators.fi_ssn(applicant.ssn):
        rejection_reasons.append('Invalid SSN')
    
    if application.requested_maturity <= 6:
        rejection_reasons.append('Maturity < 6 months')
    
    if applicant.employment_status == EmploymentStatus.UNEMPLOYED:
        rejection_reasons.append('Applicant is unemployed')
    
    if applicant.income < 20000:
        rejection_reasons.append('Applicant income < 20000')
    
    if applicant.age < 18:
        rejection_reasons.append('Applicant Age < 18')
    
    if application.purpose == Purpose.AVOID_BANKRUPTCY:
        rejection_reasons.append('Loan Purpose = AVOID_BANKRUPTCY')
        
    return rejection_reasons