from fastapi import APIRouter
from app.enums import LoanSpecification

router = APIRouter()

@router.get('/test/{name}')
def test(name: str):
    return {'message': f'hello {name}'}

@router.get('/values/{value}')
def get_enum(value: str):
    if value == 'loan_interest':
        return LoanSpecification.loan_interest
    if value == 'max_maturity':
        return LoanSpecification.max_maturity
    if value == 'setup_fee':
        return LoanSpecification.setup_fee

@router.get('/values/all')
def get_values():
    return list(LoanSpecification)
