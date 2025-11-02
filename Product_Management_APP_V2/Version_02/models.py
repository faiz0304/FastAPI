# -------------------------------
# models.py
# -------------------------------
# Defines Pydantic model(s) for request and response validation.
# Used to ensure data consistency between client and server.
# -------------------------------

from pydantic import BaseModel


class Product(BaseModel):
    """Pydantic model representing a product"""

    id: int
    name: str
    description: str
    price: float
    quantity: int

    # Note: The custom __init__ method below is not needed.
    # Pydantic automatically handles initialization and validation.
    #
    # def __init__(self, id: int, name: str, description: str, price: float, quantity: int):
    #     self.id = id
    #     self.name = name
    #     self.description = description
    #     self.price = price
    #     self.quantity = quantity
