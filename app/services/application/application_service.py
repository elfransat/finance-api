from ..applicant.applicant_validator import security_number_validator
from ...models.application import ApplicationInput, Application
from ...enums import Status
import validators
from ..bidding import bidding_service 

async def handle_application(application: ApplicationInput):

    #first update application to processing TODO: update to DB

    application = Application(**application.model_dump(), status=Status.PROCESSING)

    validators.fi_ssn(application.applicant.ssn)


    # TODO: work with these so that if there is an error then update status to reflect it
    bidding_service.execute_bidding(application)
