# app/services/application/application_service.py
from app.enums import Status
from app.db.models import Application, Applicant
from app.db.database import update_application, get_applicant, update_status
from app.services.bidding import bidding_service
from app.services.application.application_validator import validate_application
from typing import List

def handle_application(application: Application):
    applicant = get_applicant(application.applicant_id)
    
    # Update application status to PROCESSING
    application.status = Status.PROCESSING
    update_status(application.id, application.status)
    
    # Process application
    return process_application(application, applicant)

def reject(application: Application, reasons: List[str]):
    application.status = Status.REJECTED
    application.rejections = reasons
    update_application(application.id, application)
    return application

def process_application(application: Application, applicant: Applicant):
    # Validate application
    rejection_reasons = validate_application(application, applicant)
    
    # If there are rejection reasons, reject the application
    if rejection_reasons:
        return reject(application, rejection_reasons)
    
    # If no rejections, proceed with bidding
    return bidding_service.execute_bidding(application, applicant)