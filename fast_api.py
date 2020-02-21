from datetime import datetime
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel


class ExectuionItem(BaseModel):
    id: int = None
    status: str
    params: List[str]
    result: str
    error: str
    started_at: datetime
    finished_at: datetime = None


class Execution(BaseModel):
    id: int = None
    inputs: str
    outputs: str
    creation: datetime
    execution_items: List[ExectuionItem] = []


_executions = []
_executions_dict = {}

app = FastAPI()


@app.get("/executions/{page_number}/{items_per_page}")
async def get_executions(page_number: int, items_per_page: int):
    first_index = page_number * items_per_page
    last_index = (page_number + 1) * items_per_page
    return _executions[first_index:last_index]


@app.get("/executions/{execution_id}")
async def get(execution_id: int):
    return _executions_dict[execution_id]


@app.post("/executions")
async def post(execution: Execution):
    execution.id = len(_executions)
    _executions_dict[execution.id] = execution
    _executions.append(execution)
    return execution
