from fastapi import FastAPI, HTTPException
from pydantic import BaseModel



app = FastAPI()

# Fake in-memory DB
fake_db = []

# Schema
class User(BaseModel):
    id: int
    name: str
    email: str

@app.get("/users")
def get_users():
    return {"name":"John Doe", "age":3, "gender":"Male"}

