import logging
from fastapi import FastAPI
from views import addview

logging.basicConfig(level=logging.INFO)

app = FastAPI()

app.include_router(addview.router)