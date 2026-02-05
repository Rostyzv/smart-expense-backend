from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import sqlite3

app = FastAPI()

def init_db():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            amount REAL,
            category TEXT,
            date TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

class Expense(BaseModel):
    id: int = None
    title: str
    amount: float
    category: str
    date: str

@app.get("/expenses", response_model=List[Expense])
def get_expenses():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, amount, category, date FROM expenses")
    rows = cursor.fetchall()
    conn.close()
    
    return [
        {"id": r[0], "title": r[1], "amount": r[2], "category": r[3], "date": r[4]} 
        for r in rows
    ]

@app.post("/expenses")
def add_expense(expense: Expense):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO expenses (title, amount, category, date) VALUES (?, ?, ?, ?)",
        (expense.title, expense.amount, expense.category, expense.date)
    )
    conn.commit()
    conn.close()
    return {"message": "Gasto guardado correctamente"}