## Ecommerce FastAPI Backend

-Product CRUD
-Pagination
-user Authentication
-cart system 
-order management
-payment integration 
-Payment Status Tracking
-Payment History API
-PostgreSQL Database
-SQLAlchemy ORM
-Alembic Migrations

## Tech Stack
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Pydantic

## APIs
- Product APIs
- Cart APIs
- Order APIs
- Payment APIs
- Authentication APIs

## Project Structure
routes/
controllers/
models/
schemas/
database/


## Database
- PostgreSQL

## How to Run

```bash
uvicorn main:app --reload


 ## Setup Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment
### Windows
```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Alembic Migration

```bash
alembic revision --autogenerate -m "message"

alembic upgrade head
```