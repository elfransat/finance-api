from app.db.models import Application, Applicant
from app.enums import EmploymentStatus, MAX_BID, Status
from app.db.database import update_status


def execute_bidding(application: Application, applicant: Applicant):

    max_bid = MAX_BID #default to the maximum bid allowed

    if application.requested_maturity < 12: #max 20000 for loans less than 12 months
        max_bid = 20000 

    if applicant.employment_status == EmploymentStatus.SELF_EMPLOYED: #max 10000 for self employed applicants
        max_bid = 10000

    if applicant.income < 40000:
        max_bid = 10000 

    application.status = Status.BID

    application.loan_offer = round_bid(application.requested_amount, max_bid)


    update_status(application.id, application.status)



    return application
    

def round_bid(amount, max_bid, base=5000):
    rounded = base * round(amount / base)
    if max_bid is not None and rounded > max_bid:
        return max_bid
    return rounded