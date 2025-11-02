# -------------------------------
# database.py
# -------------------------------
# Database configuration using SQLAlchemy.
# Establishes the PostgreSQL connection and session factory.
# -------------------------------

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# PostgreSQL database connection URL
db_url = "postgresql://postgres:123@localhost:5432/fastapi_todo"

# Create the SQLAlchemy engine (handles database connection)
engine = create_engine(db_url)

# Create a configured "Session" class
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
