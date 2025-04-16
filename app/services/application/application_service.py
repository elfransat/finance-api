import validators
from app.enums import Status
from app.services.bidding import bidding_service 
from app.db.models import Application, Applicant
from app.db.database import update_application

async def handle_application(application: Application):

    ##TODO: retrieve applicant also if needed

    data = application.model_dump()
    data["status"] = Status.PROCESSING
    application = Application(**data)

    # updated status to processing TODO: update to DB
    application.status = Status.PROCESSING


    def reject(reason: str): #current implementation only gives one rejection reason
        application.status = Status.REJECTED
        application.rejection = reason
        update_application(application.id, application)
        return application
    
    # Check all rejection conditions
    if application.requested_amount <= 100:
        return reject('Rejected due to requested_amount being too small')
    
    if not validators.fi_ssn(application.applicant.ssn):
        return reject('Invalid SSN')
    
    if application.requested_maturity <= 6:
        return reject('Rejected due to requested_maturity being less than 6 months')
    
    if application.applicant.employment_status.value == 'UNEMPLOYED':
        return reject('Rejected due to applicant employment_status being unemployed')
    
    if application.applicant.income <= 20000:
        return reject('Applicant rejected due applicant.income being less than 20000')
    
    if application.applicant.age < 18:
        return reject('Applicant rejected due to applicant.age being less than 18')

        #TODO loan_purpose - only allow specific enums and approve / reject these

    # if no rejection go forward with bidding
    bidding_result = bidding_service.execute_bidding(application)

    return  bidding_result
