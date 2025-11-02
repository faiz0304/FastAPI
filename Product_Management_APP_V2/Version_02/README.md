# FastAPI Product Management App

This project is a **FastAPI CRUD (Create, Read, Update, Delete)** application for managing products using **PostgreSQL** and **SQLAlchemy ORM**.  
It demonstrates API design with database integration, dependency injection, and Pydantic validation.

---

## Features
- Add, update, delete, and view products.
- Uses **FastAPI** for the backend framework.
- **SQLAlchemy ORM** for database operations.
- **PostgreSQL** for data storage.
- Auto-creates the database table on first run.
- Preloads sample data if the database is empty.

---

## 📁 Project Structure

FastAPI_Project/
│
├── main.py # Main FastAPI app (all routes/endpoints)
├── models.py # Pydantic model for data validation
├── database.py # PostgreSQL database connection & session setup
├── database_model.py # SQLAlchemy ORM model for 'product' table
├── requirements.txt # Project dependencies
├── README.md # Documentation file
├── project.yml # Project metadata
└── output.txt # Example API outputs


---

## Installation & Setup

### 1️⃣ Clone or Download the Project
```bash
git clone <your-repo-url>
cd FastAPI_Project
```

2️⃣ Create a Virtual Environment
- python -m venv myenv

3️⃣ Activate the Environment

- Windows:
  - myenv\Scripts\activate


- Linux/Mac:
  - source myenv/bin/activate

4️⃣ Install Dependencies
- pip install -r requirements.txt

5️⃣ Configure PostgreSQL

- Make sure PostgreSQL is installed and running.
- Create a database named fastapi_todo (or update in database.py).

- CREATE DATABASE fastapi_todo;
- You can change credentials in:

# database.py
- db_url = "postgresql://postgres:123@localhost:5432/fastapi_todo"

▶️ Run the Application
- uvicorn main:app --reload


- The app will start at:
  - http://127.0.0.1:8000

## API Docs available at:

- Swagger UI → http://127.0.0.1:8000/docs

- Redoc → http://127.0.0.1:8000/redoc

## API Endpoints

| Method | Endpoint           | Description             |
| ------ | ------------------ | ----------------------- |
| GET    | `/`                | Welcome message         |
| GET    | `/products`        | Get all products        |
| GET    | `/product/{id}`    | Get product by ID       |
| POST   | `/product`         | Add a new product       |
| PUT    | `/product?id={id}` | Update existing product |
| DELETE | `/product?id={id}` | Delete product by ID    |


## Example Product JSON
{
  "id": 5,
  "name": "Smart Watch",
  "description": "Fitness tracking wearable",
  "price": 49.99,
  "quantity": 25
}

## Tech Stack

- FastAPI (Web Framework)
- SQLAlchemy (ORM)
- PostgreSQL (Database)
- Uvicorn (ASGI Server)
- Pydantic (Data Validation)

## Author

Faiz Ur Rehman Ashrafi
Student | Agentic AI
Karachi, Pakistan

License

This project is licensed under the SMIT License — you are free to use, modify, and distribute with attribution.