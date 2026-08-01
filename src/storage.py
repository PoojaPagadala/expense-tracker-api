import json

# DATA_FILE = Path("data/expenses.json")
import os
from pathlib import Path
from typing import Optional

from .models import Expense

DATA_FILE = Path(
    os.getenv("EXPENSE_DATA_FILE", "data/expenses.json")
)

def load_expenses() -> list[Expense]:
    """Load all expenses from the JSON file."""
    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r") as file:
        data = json.load(file)

    return [Expense(**expense) for expense in data]


def save_expenses(expenses: list[Expense]) -> None:
    """Save all expenses to the JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(
            [expense.model_dump(mode="json") for expense in expenses],
            file,
            indent=4
        )


def get_next_id(expenses: list[Expense]) -> int:
    """Generate the next expense ID."""
    if not expenses:
        return 1

    return max(expense.id for expense in expenses) + 1


def add_expense(expense: Expense) -> Expense:
    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)
    return expense


def delete_expense(expense_id: int) -> bool:
    expenses = load_expenses()

    updated = [e for e in expenses if e.id != expense_id]

    if len(updated) == len(expenses):
        return False

    save_expenses(updated)
    return True


def filter_by_category(category: str) -> list[Expense]:
    expenses = load_expenses()
    return [
        expense
        for expense in expenses
        if expense.category.lower() == category.lower()
    ]


def calculate_total(category: Optional[str] = None) -> float:
    expenses = load_expenses()

    if category:
        expenses = [
            expense
            for expense in expenses
            if expense.category.lower() == category.lower()
        ]

    return sum(expense.amount for expense in expenses)