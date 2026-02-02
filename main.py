from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Expense(BaseModel):
    id: int
    title: str
    amount: float
    category: str
    date: str

db_expenses = [
    {"id": 1, "title": "Suscripción Netflix", "amount": 12.99, "category": "Ocio", "date": "01/02"},
    {"id": 2, "title": "Kebab", "amount": 15.50, "category": "Comida", "date": "02/02"}
]

@app.get("/")
def home():
    return {"status": "Servidor funcionando correctamente"}

@app.get("/expenses", response_model=List[Expense])
def get_expenses():
    return db_expenses

@app.post("/expenses")
def add_expense(expense: Expense):
    db_expenses.append(expense.dict())
    return {"message": "Gasto guardado con éxito", "data": expense}