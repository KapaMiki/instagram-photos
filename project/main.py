from typing import Union

from fastapi import FastAPI
from fastapi.routing import APIRouter

from apps.pictures.contollers import router as pictures_router

app = FastAPI()

app.include_router(pictures_router, prefix='/pictures')
