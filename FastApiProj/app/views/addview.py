import logging
from fastapi import APIRouter, HTTPException
from models.addrequest import AddRequest
from models.addresponse import AddResponse
from multiprocessing import Pool
import datetime
from controllers.controller import add_list

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get('/')
def index():
    return 'Welcome'

@router.post("/add/", response_model=AddResponse)
async def perform_addition(request: AddRequest):
    try:
        
        started_at = datetime.datetime.now()
        with Pool() as pool:
            result = pool.map(add_list, request.payload)        
        completed_at = datetime.datetime.now()

        response_data = {"batchid":request.batchID,
                         "response":result,
                         "status":"complete",
                         "started_at": str(started_at), 
                         "completed_at": str(completed_at)}
        return response_data
    except Exception as e:
        logger.exception(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")