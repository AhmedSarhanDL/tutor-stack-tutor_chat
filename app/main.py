from fastapi import FastAPI
from pydantic import BaseModel
import dspy, openai
from typing import Dict

app = FastAPI()


class Question(BaseModel):
    question: str


class Answer(BaseModel):
    answer: str


@app.get("/health")
async def health_check() -> Dict[str, str]:
    return {"status": "healthy"}


@app.post("/answer")
async def answer(q: Question) -> Answer:
    # Changed response message for the automated PR
    return Answer(answer="this is the automated pull request test")
