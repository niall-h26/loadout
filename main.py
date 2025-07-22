from fastapi import FastAPI
from app.api import loadouts  # this is app/api/loadouts.py

app = FastAPI()

app.include_router(loadouts.router, prefix="/loadouts", tags=["Loadouts"])