from fastapi import FastAPI
from pydantic import BaseModel
from routes.alumno import router

app = FastAPI()

app.include_router(router)

