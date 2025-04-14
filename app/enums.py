from enum import Enum, IntEnum

class Status(str, Enum):
    RECIEVED = 'RECIEVED'
    PROCESSING = 'PROCESSING'
    BID = 'BID'
    DECLINED = 'DECLINED'
    USER_ACCEPTED = 'USER_ACCEPTED'
    USER_DECLINED = 'USER_DECLINED'
    EXPIRED = 'EXPIRED'
    ERROR = 'ERROR'

class EmploymentStatus(str, Enum):
    UNEMPLOYED = 'UNEMPLOYED'
    SELFEMPLOYED = 'SELF_EMPLOYED'
    EMPLOYEE = 'EMPLOYEE'

class LoanSpecification(Enum): # specifications used to make bidding decision
    loan_interest = '50%'
    max_maturity = '16M'
    setup_fee = 2500

class Rejections(Enum):
    company_founded = 'P6M'
    revenue = '10000'
