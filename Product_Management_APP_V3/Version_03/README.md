# FastAPI Product Management Web App

A simple full-stack web application for managing products using **FastAPI** (backend) and a **modern JavaScript frontend**.

---

## Features
- Create, Read, Update, Delete (CRUD) operations for products.
- FastAPI backend with SQLAlchemy ORM.
- Frontend built using HTML, CSS, and JavaScript (npm-based build).
- RESTful API endpoints with automatic Swagger documentation.

---

## Tech Stack
**Backend:**
- FastAPI  
- SQLAlchemy  
- SQLite (default database)

**Frontend:**
- HTML / CSS / JavaScript  
- Node.js & npm for package management and build

---

## Project Structure

FastAPI_Project_Assignment/
│
├── main.py
├── models.py
├── database_models.py
├── requirements.txt
├── README.md
├── project.yml
├── output.txt
│
├── frontend/
│ ├── package.json
│ ├── index.html
│ ├── src/
│ ├── css/
│ └── js/
│
└── database/
└── product.db


---

## Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/faiz0304/FastAPI_Product_App.git
cd FastAPI_Project_Assignment
```

### 2️⃣ Backend Setup

Create and activate virtual environment:
python -m venv myenv
myenv\Scripts\activate   # for Windows

Install dependencies:
pip install -r requirements.txt

Run the FastAPI server:
uvicorn main:app --reload

Open your browser and visit:
http://127.0.0.1:8000/docs


### 3️⃣ Frontend Setup

Move to the frontend folder:
- cd frontend


Install npm dependencies:
- npm install


Run the frontend:
- npm start

## API Endpoints

| Method | Endpoint         | Description        |
| :----- | :--------------- | :----------------- |
| GET    | `/products`      | Get all products   |
| GET    | `/products/{id}` | Get single product |
| POST   | `/products`      | Add new product    |
| PUT    | `/products/{id}` | Update product     |
| DELETE | `/products/{id}` | Delete product     |


## Developer Info

Author: Faiz Ur Rehman Ashrafi
Role: Student – Electronics Engineering Technology
GitHub: faiz0304

