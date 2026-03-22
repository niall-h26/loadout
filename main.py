from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api import loadouts  # this is app/api/loadouts.py

app = FastAPI()

app.include_router(loadouts.router, prefix="/loadouts", tags=["Loadouts"])

app.mount("/", StaticFiles(directory="static", html=True), name="static")
