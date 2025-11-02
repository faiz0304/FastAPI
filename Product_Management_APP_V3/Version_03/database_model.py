"""
database_model.py
-----------------
Defines SQLAlchemy ORM models (tables) for the FastAPI project.
Each class represents a database table.
"""

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

# -------------------------------------------
# Base class for all SQLAlchemy ORM models
# -------------------------------------------
Base = declarative_base()


class Product(Base):
    """
    SQLAlchemy ORM model for 'product' table.
    Stores product details like name, price, and quantity.
    """

    __tablename__ = "product"  # Table name in PostgreSQL

    # Columns
    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String(100), nullable=False)  # Max length added for safety
    description: str = Column(String(255))  # Short description
    price: float = Column(Float, nullable=False)
    quantity: int = Column(Integer, nullable=False)

    def __repr__(self) -> str:
        """Readable string representation for debugging and logs."""
        return f"<Product(id={self.id}, name='{self.name}', price={self.price}, quantity={self.quantity})>"
