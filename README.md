# Smart Expense Tracker API

A RESTful API built with **FastAPI** for managing personal expenses. The API supports creating, viewing, filtering, calculating totals, and deleting expenses. Data is stored in a local JSON file, and the project includes automated tests using Pytest.

## Features

- Add a new expense
- View all expenses
- Filter expenses by category
- Calculate total expenses
- Calculate total expenses by category
- Delete an expense
- Automatic request validation using Pydantic
- Interactive API documentation using Swagger/OpenAPI
- Automated test suite with Pytest

## Tech Stack

- Python 3.9
- FastAPI
- Pydantic
- Uvicorn
- Pytest
- JSON File Storage

## Project Structure

```text
expense-tracker-api/
│
├── README.md
├── AI_NOTES.md
├── requirements.txt
├── .gitignore
│
├── data/
│   └── expenses.json
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   └── storage.py
│
└── tests/
    ├── __init__.py
    ├── test_api.py
    └── test_expenses.json
```

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd expense-tracker-api
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Server

```bash
uvicorn src.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

## Run Tests

```bash
pytest
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/expenses` | Add a new expense |
| GET | `/expenses` | Retrieve all expenses |
| GET | `/expenses?category=Food` | Filter expenses by category |
| GET | `/expenses/total` | Get total expenses |
| GET | `/expenses/total?category=Food` | Get total expenses for a category |
| DELETE | `/expenses/{expense_id}` | Delete an expense |

## Example Request

```json
{
  "title": "Lunch",
  "amount": 250,
  "category": "Food",
  "date": "2026-08-01"
}
```

## Assumptions

- Expense IDs are generated automatically.
- Data is stored in a local JSON file.
- Amount must be greater than zero.
- Authentication is not required.

## Bonus Feature

This project includes **Swagger/OpenAPI documentation**, available at:

```
http://127.0.0.1:8000/docs
```

## Future Improvements

- Update existing expenses
- Search expenses
- User authentication
- Database integration
- Pagination