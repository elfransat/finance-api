from sqlmodel import SQLModel
from app.db.database import engine

def reset_database():
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)

reset_database()