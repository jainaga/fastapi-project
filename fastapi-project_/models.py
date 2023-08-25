from fastapi import FastAPI
from pydantic import BaseModel

class Todo(BaseModel):
    title: str
    id: int 
