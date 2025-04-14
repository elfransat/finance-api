from ..applicant.applicant_validator import security_number_validator
from ...models.application import ApplicationInput, Application
from ...enums import Status
import validators
from ..bidding import bidding_service 

async def handle_application(application: ApplicationInput):

    #first map ApplicatiponInput onto Application
    application = Application(**application.model_dump(), status=Status.PROCESSING)

    # updated status to processing TODO: update to DB
    application.status = Status.PROCESSING


    def reject(reason: str): #current implementation only gives one rejection reason
        application.status = Status.REJECTED
        application.rejection = reason
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
