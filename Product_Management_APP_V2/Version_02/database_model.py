# -------------------------------
# database_model.py
# -------------------------------
# Defines SQLAlchemy ORM models (database tables).
# Each class represents one table in the database.
# -------------------------------

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

# Base class for all ORM models
Base = declarative_base()


class Product(Base):
    """SQLAlchemy ORM model for the 'product' table"""

    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
