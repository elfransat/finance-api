from enum import Enum, IntEnum

class Status(IntEnum):
    APPLIED = 0
    PROCESSING = 1
    BID = 2
    DECLINED = 3
    USER_ACCEPTED = 4
    USER_DECLINED = 5
    EXPIRED = 6
    ERROR = 7

class EmploymentStatus(str, Enum):
    UNEMPLOYED = 'UNEMPLOYED'
    SELFEMPLOYED = 'SELF_EMPLOYED'
    EMPLOYEE = 'EMPLOYEE'

class LoanSpecification(Enum): 
    loan_interest = '50%'
    max_maturity = '16M'
    setup_fee = 2500

class Rejections(Enum):
    company_founded = 'P6M'
    revenue = '10000'
