from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv


load_dotenv()


DATABASE_URL = os.getenv('DATABASE_URL') or 'sqlite:///./test.db'


connect_args = {"check_same_thread": False} if DATABASE_URL.startswith('sqlite') else {}
engine = create_engine(DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# created tables for prototype
def init_db():
    from models import room as room_model 
    Base.metadata.create_all(bind=engine)




from typing import Generator

# Dependency for database session of Fastapi routes
def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


