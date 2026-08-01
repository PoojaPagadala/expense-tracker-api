import json
import os

from fastapi.testclient import TestClient

os.environ["EXPENSE_DATA_FILE"] = "tests/test_expenses.json"

from src.main import app

client = TestClient(app)


def setup_function():
    with open("tests/test_expenses.json", "w") as f:
        json.dump([], f)


def test_add_expense():
    response = client.post(
        "/expenses",
        json={
            "title": "Lunch",
            "amount": 250,
            "category": "Food",
            "date": "2026-08-01"
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["id"] == 1
    assert data["title"] == "Lunch"


def test_get_expenses():
    client.post(
        "/expenses",
        json={
            "title": "Lunch",
            "amount": 250,
            "category": "Food",
            "date": "2026-08-01"
        },
    )

    response = client.get("/expenses")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_filter_category():
    client.post(
        "/expenses",
        json={
            "title": "Lunch",
            "amount": 250,
            "category": "Food",
            "date": "2026-08-01"
        },
    )

    response = client.get("/expenses?category=Food")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_total():
    client.post(
        "/expenses",
        json={
            "title": "Lunch",
            "amount": 250,
            "category": "Food",
            "date": "2026-08-01"
        },
    )

    response = client.get("/expenses/total")

    assert response.status_code == 200
    assert response.json()["total"] == 250


def test_delete():
    client.post(
        "/expenses",
        json={
            "title": "Lunch",
            "amount": 250,
            "category": "Food",
            "date": "2026-08-01"
        },
    )

    response = client.delete("/expenses/1")

    assert response.status_code == 200
def test_invalid_amount():
    response = client.post(
        "/expenses",
        json={
            "title": "Lunch",
            "amount": -50,
            "category": "Food",
            "date": "2026-08-01"
        }
    )

    assert response.status_code == 422

def test_empty_title():
    response = client.post(
        "/expenses",
        json={
            "title": "",
            "amount": 100,
            "category": "Food",
            "date": "2026-08-01"
        }
    )

    assert response.status_code == 422

def test_invalid_date():
    response = client.post(
        "/expenses",
        json={
            "title": "Lunch",
            "amount": 100,
            "category": "Food",
            "date": "abc"
        }
    )

    assert response.status_code == 422

def test_delete_invalid():
    response = client.delete("/expenses/100")

    assert response.status_code == 404

def test_empty_list():
    response = client.get("/expenses")

    assert response.status_code == 200
    assert response.json() == []

def test_total_empty():
    response = client.get("/expenses/total")

    assert response.status_code == 200
    assert response.json()["total"] == 0

def test_category_total():
    client.post(
        "/expenses",
        json={
            "title":"Lunch",
            "amount":250,
            "category":"Food",
            "date":"2026-08-01"
        }
    )

    response = client.get("/expenses/total?category=Food")

    assert response.json()["total"] == 250
