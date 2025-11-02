from pydantic import BaseModel, Field

# -------------------------------------------
# Product Schema (Pydantic Model)
# -------------------------------------------


class Product(BaseModel):
    """Schema for validating and serializing product data."""

    id: int = Field(..., description="Unique ID of the product", example=1)
    name: str = Field(..., description="Name of the product", example="Smartphone")
    description: str = Field(
        ...,
        description="Brief details about the product",
        example="Budget-friendly phone",
    )
    price: float = Field(..., description="Price of the product in USD", example=99.99)
    quantity: int = Field(..., description="Available stock quantity", example=10)

    class Config:
        orm_mode = True  # Enables compatibility with SQLAlchemy ORM models
