from fastapi import FastAPI

from .routes import router

app = FastAPI(
    title="Smart Expense Tracker API",
    description="""
A REST API for managing personal expenses.

## Features

- Add a new expense
- View all expenses
- Filter expenses by category
- Calculate total expenses
- Delete an expense

Built using FastAPI and local JSON storage.
""",
    version="1.0.0",
    contact={
        "name": "Pagadala Pooja",
        "email": "poojapagadala4245@gmail.com",
    },
    license_info={
        "name": "MIT"
    }
)

app.include_router(router)


@app.get(
    "/",
    tags=["Home"],
    summary="API Home",
    description="Returns a welcome message and Swagger documentation link."
)
def root():
    return {
        "message": "Welcome to the Smart Expense Tracker API!",
        "docs": "/docs"
    }