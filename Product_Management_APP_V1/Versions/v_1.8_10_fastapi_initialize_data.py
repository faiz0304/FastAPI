from fastapi import FastAPI
from models import Product
from database import session, engine
import database_model

database_model.Base.metadata.create_all(bind=engine)

app = FastAPI()

products = [
    Product(id=1, name="phone", description="budget phone", price=99, quantity=10),
    Product(id=2, name="laptop", description="gaming laptop", price=999, quantity=6),
    Product(id=3, name="Ipad", description="Tablet", price=59.9, quantity=15),
    Product(id=4, name="Air pod", description="Ear Bud", price=15.5, quantity=20),
]


def init_db():
    db = session()
    count = db.query(database_model.Product).count()
    if count == 0:
        for product in products:
            db.add(database_model.Product(**product.model_dump()))
        db.commit()


init_db()


@app.get("/")
def greet():
    return "Welcome to FastAPI Project"


@app.get("/products")
def get_all_products():
    db = session()
    db.query()
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


@app.put("/product")
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product Updated Successfully"

    return "Product Not Found"


@app.delete("/product")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product Deleted Sccessfully"

    return "Product Not Found"
