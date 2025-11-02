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


@app.get("/product/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
    return "product not found"


@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return f"{product}"
