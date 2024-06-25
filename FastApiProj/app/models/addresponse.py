from pydantic import BaseModel
from typing import List

class AddResponse(BaseModel):
    batchid: str
    response: List[int]
    status: str
    started_at: str
    completed_at: str