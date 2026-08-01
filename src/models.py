from datetime import date

from pydantic import BaseModel, Field


class ExpenseCreate(BaseModel):
    title: str = Field(
    ...,
    min_length=1,
    max_length=100,
    examples=["Lunch"]
)
    amount: float = Field(
    ...,
    gt=0,
    le=1000000,
    examples=[250]
)
    category: str = Field(
    ...,
    min_length=1,
    max_length=50,
    examples=["Food"]
)
    date: date


class Expense(ExpenseCreate):
    id: int