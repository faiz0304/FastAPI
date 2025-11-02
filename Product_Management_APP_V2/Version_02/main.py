# -------------------------------
# main.py
# -------------------------------
# FastAPI application entry point.
# Handles all API endpoints (CRUD operations) for Product management.
# Uses SQLAlchemy for database ORM and Pydantic for data validation.
# -------------------------------

from fastapi import FastAPI, Depends
from models import Product
from database import session, engine
import database_model
from sqlalchemy.orm import Session

# Create all database tables (if not already created)
database_model.Base.metadata.create_all(bind=engine)

# Initialize FastAPI application
app = FastAPI()

# -------------------------------
# Sample products to preload into the database (if empty)
# -------------------------------
products = [
    Product(id=1, name="Phone", description="Budget phone", price=99, quantity=10),
    Product(id=2, name="Laptop", description="Gaming laptop", price=999, quantity=6),
    Product(id=3, name="iPad", description="Tablet", price=59.9, quantity=15),
    Product(id=4, name="AirPods", description="Earbuds", price=15.5, quantity=20),
]


# Dependency function: provides a database session for each request
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


# -------------------------------
# Initialize database with sample products if empty
# -------------------------------
def init_db():
    db = session()
    count = db.query(database_model.Product).count()
    if count == 0:
        for product in products:
            db.add(database_model.Product(**product.model_dump()))
        db.commit()


# Run the initialization at startup
init_db()


# -------------------------------
# Routes (Endpoints)
# -------------------------------


@app.get("/")
def greet():
    """Root endpoint - Welcome message"""
    return "Welcome to FastAPI Project"


@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    """Fetch all products from the database"""
    db_products = db.query(database_model.Product).all()
    return db_products


@app.get("/product/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    """Fetch a product by its ID"""
    db_product = (
        db.query(database_model.Product).filter(database_model.Product.id == id).first()
    )
    if db_product:
        return db_product
    return {"message": "Product not found"}


@app.post("/product")
def add_product(product: Product, db: Session = Depends(get_db)):
    """Add a new product to the database"""
    db.add(database_model.Product(**product.model_dump()))
    db.commit()
    return {"message": "Product added successfully", "product": product}


@app.put("/product")
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    """Update product details by ID"""
    db_product = (
        db.query(database_model.Product).filter(database_model.Product.id == id).first()
    )
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return {"message": "Product updated successfully"}
    else:
        return {"message": "Product not found"}


@app.delete("/product")
def delete_product(id: int, db: Session = Depends(get_db)):
    """Delete a product by its ID"""
    db_product = (
        db.query(database_model.Product).filter(database_model.Product.id == id).first()
    )
    if db_product:
        db.delete(db_product)
        db.commit()
        return {"message": "Product deleted successfully"}
    else:
        return {"message": "Product not found"}
