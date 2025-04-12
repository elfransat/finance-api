from fastapi import FastAPI
from .routes.application_routes import router as application_router

app = FastAPI()

app.include_router(application_router)
