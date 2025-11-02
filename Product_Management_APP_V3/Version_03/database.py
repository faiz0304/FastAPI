"""
database.py
------------
This module handles the database connection setup using SQLAlchemy.
It creates the engine and session factory for PostgreSQL database access.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# -------------------------------------------
# Database Configuration
# -------------------------------------------

# Use your own PostgreSQL credentials and DB name
# url_example: postgresql://<user>:<password>@<host>:<port>/<database_name>
DATABASE_URL: str = "postgresql://postgres:123@localhost:5432/fastapi_todo"

# Create SQLAlchemy engine (connection interface to the database)
# echo=True helps log SQL queries in the console — useful for debugging (turn off in production)
engine = create_engine(DATABASE_URL, echo=False)

# Create a configured "Session" class
# autocommit=False → explicit commit required
# autoflush=False → better manual control of transactions
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# -------------------------------------------
# Optional: Connection Test Function
# -------------------------------------------
def test_connection() -> None:
    """
    Optional helper to verify database connectivity.
    You can call this once at startup to confirm connection success.
    """
    try:
        with engine.connect() as connection:
            print("Database connection successful!")
    except SQLAlchemyError as e:
        print("Database connection failed:", str(e))
