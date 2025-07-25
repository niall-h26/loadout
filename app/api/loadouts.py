from fastapi import APIRouter, HTTPException
from app.storage import LoadoutStorage
from app.models import Loadout
from typing import Dict, Any

router = APIRouter()
storage = LoadoutStorage()

@router.get("/")
def list_loadouts():
    return storage.list_loadouts()

@router.get("/{name}")
def get_loadout(name: str):
    try:
        return storage.load(name).to_dict()
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/")
def create_loadout(loadout: Dict[str, Any]):
    try:
        obj = Loadout.from_dict(loadout)
        obj.validate()
        storage.save(obj)
        return {"message": f"Loadout '{obj.name}' saved."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{name}")
def update_loadout(name: str, loadout: Dict[str, Any]):
    try:
        obj = Loadout.from_dict(loadout)
        obj.validate()
        obj.name = name  # enforce URL name
        storage.save(obj, overwrite=True)
        return {"message": f"Loadout '{name}' updated."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{name}")
def delete_loadout(name: str):
    try:
        storage.delete(name)
        return {"message": f"Loadout '{name}' deleted."}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
