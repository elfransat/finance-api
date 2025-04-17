from app.db.models import Application, Applicant
from app.enums import EmploymentStatus, MAX_BID, Status
from app.db.database import update_application

def execute_bidding(application: Application, applicant: Applicant):
    """Calculate loan offer based on applicant and application data"""

    max_bid = determine_max_bid(application, applicant)
    loan_offer = round_bid(application.requested_amount, max_bid)
    
    # Update application
    application.status = Status.BID
    application.loan_offer = loan_offer
    update_application(application.id, application)
    
    return application

def determine_max_bid(application: Application, applicant: Applicant) -> int:
    """Determine maximum bid amount based on rules"""
    
    max_bid = MAX_BID  # default to the maximum bid in Enums
    
    if application.requested_maturity < 12:
        max_bid = min(max_bid, 20000)
        
    if applicant.employment_status == EmploymentStatus.SELF_EMPLOYED:
        max_bid = min(max_bid, 10000)
        
    if applicant.income < 40000:
        max_bid = min(max_bid, 10000)
        
    return max_bid

def round_bid(amount: int, max_bid: int, base: int = 5000) -> int:
    rounded = base * round(amount / base)
    if rounded > max_bid:
        return max_bid
    return rounded