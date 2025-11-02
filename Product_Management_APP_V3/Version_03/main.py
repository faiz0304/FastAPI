from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from models import Product
from database import session, engine
import database_model
from sqlalchemy.orm import Session
from typing import Generator, List

# -------------------------------------------
# Database Initialization
# -------------------------------------------
# Create database tables from SQLAlchemy models
database_model.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(title="FastAPI Product Management API", version="3.0")

# Allow frontend requests (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend origin (React app)
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# -------------------------------------------
# Default data (for first database population)
# -------------------------------------------
products = [
    Product(id=1, name="phone", description="budget phone", price=99, quantity=10),
    Product(id=2, name="laptop", description="gaming laptop", price=999, quantity=6),
    Product(id=3, name="Ipad", description="Tablet", price=59.9, quantity=15),
    Product(id=4, name="Air pod", description="Ear Bud", price=15.5, quantity=20),
]


# -------------------------------------------
# Database session dependency
# -------------------------------------------
def get_db() -> Generator[Session, None, None]:
    """Dependency that provides a SQLAlchemy session and closes it automatically."""
    db = session()
    try:
        yield db
    finally:
        db.close()


# -------------------------------------------
# Initialize DB with default data (only once)
# -------------------------------------------
def init_db() -> None:
    """Insert default products if database is empty."""
    db = session()
    count = db.query(database_model.Product).count()
    if count == 0:
        for product in products:
            db.add(database_model.Product(**product.model_dump()))
        db.commit()
    db.close()


init_db()  # Run initialization once when server starts


# -------------------------------------------
# Routes
# -------------------------------------------


@app.get("/", response_class=JSONResponse)
def greet() -> dict:
    """Root endpoint showing welcome message."""
    return {"message": "Welcome to FastAPI Project (PRODUCT MANAGEMENT APP)"}


@app.get("/products", response_model=List[Product], status_code=status.HTTP_200_OK)
def get_all_products(db: Session = Depends(get_db)) -> List[Product]:
    """Fetch all products from the database."""
    db_products = db.query(database_model.Product).all()
    if not db_products:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No products found in the database",
        )
    return db_products


@app.get("/product/{id}", response_model=Product, status_code=status.HTTP_200_OK)
def get_product_by_id(id: int, db: Session = Depends(get_db)) -> Product:
    """Fetch a single product by its ID."""
    db_product = (
        db.query(database_model.Product).filter(database_model.Product.id == id).first()
    )
    if not db_product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with id {id} not found",
        )
    return db_product


@app.post(
    "/products",
    response_model=Product,
    status_code=status.HTTP_201_CREATED,
    responses={400: {"description": "Product already exists"}},
)
def add_product(product: Product, db: Session = Depends(get_db)) -> Product:
    """Add a new product to the database."""
    # Check if a product with the same ID already exists
    existing_product = (
        db.query(database_model.Product)
        .filter(database_model.Product.id == product.id)
        .first()
    )
    if existing_product:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Product with id {product.id} already exists",
        )

    new_product = database_model.Product(**product.model_dump())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


@app.put(
    "/products/{id}",
    response_model=Product,
    status_code=status.HTTP_200_OK,
    responses={404: {"description": "Product not found"}},
)
def update_product(id: int, product: Product, db: Session = Depends(get_db)) -> Product:
    """Update an existing product's details."""
    db_product = (
        db.query(database_model.Product).filter(database_model.Product.id == id).first()
    )
    if not db_product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with id {id} not found",
        )

    # Update product fields
    db_product.name = product.name
    db_product.description = product.description
    db_product.price = product.price
    db_product.quantity = product.quantity

    db.commit()
    db.refresh(db_product)
    return db_product


@app.delete(
    "/products/{id}",
    response_class=JSONResponse,
    status_code=status.HTTP_200_OK,
    responses={404: {"description": "Product not found"}},
)
def delete_product(id: int, db: Session = Depends(get_db)) -> dict:
    """Delete a product from the database."""
    db_product = (
        db.query(database_model.Product).filter(database_model.Product.id == id).first()
    )
    if not db_product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with id {id} not found",
        )

    db.delete(db_product)
    db.commit()
    return {"message": "Product deleted successfully", "deleted_id": id}
