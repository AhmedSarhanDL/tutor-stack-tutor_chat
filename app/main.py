from fastapi import FastAPI
from pydantic import BaseModel
import dspy, openai

app = FastAPI()

class Question(BaseModel):
    question: str

@app.post("/answer")
async def answer(q: Question):
    # Changed response message
    return {"answer": "this is a good question"} 