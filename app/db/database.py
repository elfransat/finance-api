from sqlmodel import Session, SQLModel, create_engine
from dotenv import load_dotenv
from fastapi import HTTPException
from app.db.models import Applicant, Application
import os
from app.enums import Status

load_dotenv()
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')
DB_NAME = os.getenv('DB_NAME')


DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)
SQLModel.metadata.create_all(engine)


# Dependency: Get the session
def get_session():
    with Session(engine) as session:
        yield session

#### application operations ####

def save_application(application: Application):
    with Session(engine) as session:
        session.add(application)
        session.commit()
        session.refresh(application)
        return application


def update_application(application_id: int, application_data: Application):
    with Session(engine) as session:
        application = session.get(Application, application_id)
        if not application:
            raise HTTPException(status_code=404, detail="Application not found")

    # Update the Application attributes
        for field, value in application_data.model_dump().items():
            setattr(application, field, value)
        session.commit()
        session.refresh(application)
        return application
    
def update_status(application_id: int, new_status: Status):
    with Session(engine) as session:
        application = session.get(Application, application_id)
        if not application:
            raise HTTPException(status_code=404, detail="Application not found")
        
        application.status = new_status
        session.add(application)
        session.commit()
        session.refresh(application)
        return application
    
def get_application(applicant_id: int):
    with Session(engine) as session:
        application = session.get(Application, applicant_id)
        if not application:
            raise HTTPException(status_code=404, detail="Application not found")
        return application


#### applicant operations ####

def save_applicant(applicant: Applicant):
    with Session(engine) as session:
        session.add(applicant)
        session.commit()
        session.refresh(applicant)
        return applicant

def get_applicant(applicant_id: int):
    with Session(engine) as session:
        applicant = session.get(Applicant, applicant_id)
        if not applicant:
            raise HTTPException(status_code=404, detail="Applicant not found")
        return applicant
