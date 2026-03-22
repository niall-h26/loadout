from fastapi import APIRouter, HTTPException
from app.storage import LoadoutStorage
from app.models import Loadout
from app.schemas import LoadoutSchema, LoadoutSummary, MessageResponse
from app.item import Item
from typing import List

router = APIRouter()
storage = LoadoutStorage()


def schema_to_loadout(schema: LoadoutSchema) -> Loadout:
    equipped = {slot: Item(**item.model_dump()) for slot, item in schema.equipped.items()}
    inventory = [Item(**item.model_dump()) for item in schema.inventory]
    return Loadout(name=schema.name, equipped=equipped, inventory=inventory)


@router.get("/", response_model=List[str])
def list_loadouts():
    return storage.list_loadouts()


@router.get("/{name}", response_model=LoadoutSchema)
def get_loadout(name: str):
    try:
        return storage.load(name).to_dict()
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/", response_model=MessageResponse, status_code=201)
def create_loadout(loadout: LoadoutSchema):
    try:
        obj = schema_to_loadout(loadout)
        storage.save(obj)
        return {"message": f"Loadout '{obj.name}' saved."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{name}", response_model=MessageResponse)
def update_loadout(name: str, loadout: LoadoutSchema):
    try:
        if name not in storage.list_loadouts():
            raise HTTPException(status_code=404, detail=f"Loadout '{name}' not found.")
        obj = schema_to_loadout(loadout)
        obj.name = name
        storage.save(obj, overwrite=True)
        return {"message": f"Loadout '{name}' updated."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{name}", response_model=MessageResponse)
def delete_loadout(name: str):
    try:
        storage.delete(name)
        return {"message": f"Loadout '{name}' deleted."}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
