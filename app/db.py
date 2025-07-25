from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# Creăm engine-ul SQLite; check_same_thread=False permite folosirea din mai multe thread-uri
engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db():
    # Creează toate tabelele declarate în models.py
    Base.metadata.create_all(bind=engine)
