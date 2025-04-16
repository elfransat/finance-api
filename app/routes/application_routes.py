from fastapi import APIRouter, Depends
from app.db import Application, Applicant, get_session, CompleteApplicationInput, save_application, save_applicant, get_application
from app.services.application.application_service import handle_application
from sqlmodel import Session
from app.enums import Status

router = APIRouter()

@router.post('/application/create')
async def create_application(input_data: CompleteApplicationInput):
    
    # create and save the applicant
    applicant = save_applicant(Applicant(**input_data.applicant.model_dump()))


    # create and save the application using applicant ID
    application = Application(
        **input_data.application.model_dump(),
        applicant_id=applicant.id,
        status=Status.RECIEVED
        )
    
    save_application(application)

    #Process application using application and applicant
    processed_application = await handle_application(application)

    return processed_application

@router.get('/application/{application_id}', response_model=Application)
async def retrieve_application(application_id: str):
    return get_application(application_id)
    