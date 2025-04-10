
from fastapi import FastAPI
from enum import Enum

app = FastAPI()


class LoanSpecification(Enum): 
    loan_interest = '50%',
    max_maturity = '16M',
    setup_fee = 2500,

class Rejections(Enum):
    company_founded = 'P6M',
    revenue = '10000'

@app.get('/')
async def root():
    return {'message' : 'hello sailor' }

@app.get('/test/{name}')
async def root(name: str):
    return {'message' : f'hello {name}' }

@app.get('values')

@app.get('/application')
async def root():
    return {'message' : 'hello sailor' }