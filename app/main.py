from fastapi import FastAPI
from pydantic import BaseModel
import dspy, openai

app = FastAPI()

class Question(BaseModel):
    question: str

@app.post("/answer")
async def answer(q: Question):
    # Changed response message for the automated PR
    return {"answer": "this is the automated pull request test"}
