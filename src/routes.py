
from typing import Optional

from fastapi import APIRouter, HTTPException

from .models import Expense, ExpenseCreate
from .storage import (
    add_expense,
    calculate_total,
    delete_expense,
    filter_by_category,
    get_next_id,
    load_expenses,
)

router = APIRouter()


@router.post(
    "/expenses",
    response_model=Expense,
    status_code=201,
    tags=["Expenses"],
    summary="Create a new expense",
    description="Adds a new expense and automatically assigns a unique ID."
)
def create_expense(expense: ExpenseCreate):
    expenses = load_expenses()

    new_expense = Expense(
        id=get_next_id(expenses),
        **expense.model_dump()
    )

    return add_expense(new_expense)

@router.get(
    "/expenses",
    response_model=list[Expense],
    tags=["Expenses"],
    summary="Retrieve expenses",
    description="Returns all expenses or filters by category."
)
def get_expenses(category: Optional[str] = None):
    if category:
        return filter_by_category(category)

    return load_expenses()


@router.get(
    "/expenses/total",
    tags=["Analytics"],
    summary="Calculate total expenses",
    description="Calculates total expenses overall or for a specific category."
)
def get_total(category: Optional[str] = None):
    return {
        "category": category,
        "total": calculate_total(category)
    }


@router.delete(
    "/expenses/{expense_id}",
    tags=["Expenses"],
    summary="Delete an expense",
    description="Deletes an expense by its unique ID."
)
def remove_expense(expense_id: int):
    success = delete_expense(expense_id)

    if not success:
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    return {
        "message": "Expense deleted successfully"
    }