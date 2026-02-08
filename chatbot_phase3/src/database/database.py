from sqlmodel import create_engine, Session
from typing import Generator
import os
from dotenv import load_dotenv
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Database URL from environment variables
DATABASE_URL = os.getenv("NEON_DATABASE_URL", "sqlite:///./todoapp.db")

logger.info(f"Using database URL: {DATABASE_URL}")

# Create the engine
try:
    engine = create_engine(DATABASE_URL, echo=True)
    logger.info("Database engine created successfully")
except Exception as e:
    logger.error(f"Error creating database engine: {str(e)}")
    # Fallback to SQLite
    DATABASE_URL = "sqlite:///./todoapp.db"
    engine = create_engine(DATABASE_URL, echo=True)
    logger.info(f"Fallback to SQLite: {DATABASE_URL}")

def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session