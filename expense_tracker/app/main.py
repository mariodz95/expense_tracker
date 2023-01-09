from typing import Union
from fastapi import FastAPI

from app.routers.router import router

app = FastAPI()
app.include_router(router)
