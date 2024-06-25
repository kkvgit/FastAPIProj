import logging
from fastapi import FastAPI
from controllers import controller

logging.basicConfig(level=logging.INFO)

app = FastAPI()

app.include_router(controller.router)