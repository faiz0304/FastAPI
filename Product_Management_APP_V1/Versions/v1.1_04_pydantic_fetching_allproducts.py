from fastapi import FastAPI

from models import Product

app = FastAPI()

products = [
    Product(id=1, name="phone", description="budget phone", price=99, quantity=10),
    Product(id=2, name="laptop", description="gaming laptop", price=999, quantity=6),
    Product(id=3, name="Ipad", description="Tablet", price=59.9, quantity=15),
    Product(id=4, name="Air pod", description="Ear Bud", price=15.5, quantity=20),
]


@app.get("/")
def greet():
    return "Welcome to FastAPI Project"


@app.get("/products")
def get_all_products():
    return products
