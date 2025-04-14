from fastapi import APIRouter
from app.models.application import Application, ApplicationInput
from app.services.bidding import bidding_service
from app.services.application.application_service import handle_application

router = APIRouter()

@router.post('/application/create')
async def create_application(application: ApplicationInput):

    processedApplication = await handle_application(application)
    return processedApplication