from sqlmodel import create_engine
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Database URL
DATABASE_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

# Create the database engine
engine = create_engine(DATABASE_URL)

# Test connection (will raise an error if unable to connect)
try:
    with engine.connect() as connection:
        print("Database connection successful!")
except Exception as e:
    print(f"Error connecting to the database: {e}")