from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from src.query import search
from src.llm import answer_question

app = FastAPI()

class SearchRequest(BaseModel):
    query: str

class SearchResult(BaseModel):
    document: str
    distance: float

class SearchResponse(BaseModel):
    results: List[SearchResult]

class AnswerRequest(BaseModel):
    query: str
    docs: List[str]

class AnswerResponse(BaseModel):
    answer: str

@app.post("/search", response_model=SearchResponse)
def search_endpoint(request: SearchRequest):
    results = search(request.query)
    return {"results": [{"document": doc, "distance": dist} for doc, dist in results]}

@app.post("/answer", response_model=AnswerResponse)
def answer_endpoint(request: AnswerRequest):
    answer = answer_question(request.query, request.docs)
    return {"answer": answer}