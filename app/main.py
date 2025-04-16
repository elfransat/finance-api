from fastapi import FastAPI
from app.routes import application_router

app = FastAPI()

app.include_router(application_router)
