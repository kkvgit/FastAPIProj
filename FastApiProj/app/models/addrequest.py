from pydantic import BaseModel
from typing import List

class AddRequest(BaseModel):
    batchID: str
    payload: List[List[int]]