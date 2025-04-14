from enum import Enum, IntEnum

MAX_BID = 50000

class Status(str, Enum):
    RECIEVED = 'RECIEVED'
    PROCESSING = 'PROCESSING'
    BID = 'BID'
    USER_ACCEPTED = 'USER_ACCEPTED'
    USER_DECLINED = 'USER_DECLINED'
    EXPIRED = 'EXPIRED'
    ERROR = 'ERROR'
    REJECTED = 'REJECTED'

class EmploymentStatus(str, Enum):
    UNEMPLOYED = 'UNEMPLOYED'
    SELF_EMPLOYED = 'SELF_EMPLOYED'
    EMPLOYED = 'EMPLOYED'

class LoanSpecification(Enum): # specifications used to make bidding decision
    loan_interest = '50%'
    max_maturity = '16M'
    setup_fee = 2500

class Rejections(Enum):
    company_founded = 'P6M'
    revenue = '10000'
