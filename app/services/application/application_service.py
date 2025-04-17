import validators
from app.enums import Status, Purpose, EmploymentStatus
from app.services.bidding import bidding_service 
from app.db.models import Application, Applicant
from app.db.database import update_application, get_applicant, update_status
from typing import List

async def handle_application(application: Application):
    # Get applicant data
    applicant = get_applicant(application.applicant_id)
    
    # Update application status to PROCESSING in the database
    application.status = Status.PROCESSING
    update_status(application.id, application.status)
    
    # Process possible rejection reasons or proceed with bidding
    return process_application(application, applicant)

def reject(application: Application, reasons: List[str]):
    application.status = Status.REJECTED
    application.rejections = reasons
    update_application(application.id, application)
    return application

def process_application(application: Application, applicant: Applicant):
    rejection_reasons = []
    
    # Check all rejection conditions and append to rejection_reasons list
    if application.requested_amount <= 1000:
        rejection_reasons.append('Requet amount < 1000')
    
    if not validators.fi_ssn(applicant.ssn):
        rejection_reasons.append('Invalid SSN')
    
    if application.requested_maturity <= 6:
        rejection_reasons.append('Maturity < 6 months')
    
    if applicant.employment_status.value == EmploymentStatus.UNEMPLOYED:
        rejection_reasons.append('Applicant is unemployed')
    
    if applicant.income < 20000:
        rejection_reasons.append('Applicant income < 20000')
    
    if applicant.age < 18:
        rejection_reasons.append('Applicant Age < 18')
    
    if application.purpose.value == Purpose.AVOID_BANKRUPTCY:
        rejection_reasons.append('Loan Purpose = AVOID_BANKRUPTCY')
        
    # If there are rejection reasons, reject the application and return it
    if rejection_reasons:
        return reject(application, rejection_reasons)
    
    # If no rejections, proceed with bidding
    bidding_result = bidding_service.execute_bidding(application, applicant)
    return bidding_result