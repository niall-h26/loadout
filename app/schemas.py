from pydantic import BaseModel, field_validator
from typing import Dict, List, Optional


class ItemSchema(BaseModel):
    name: str
    slot: Optional[str] = None
    quantity: int = 1


class LoadoutSchema(BaseModel):
    name: str
    equipped: Dict[str, ItemSchema] = {}
    inventory: List[ItemSchema] = []

    @field_validator("name")
    @classmethod
    def name_must_not_be_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Loadout name cannot be empty")
        return v

    @field_validator("inventory")
    @classmethod
    def inventory_max_28(cls, v: List[ItemSchema]) -> List[ItemSchema]:
        if len(v) > 28:
            raise ValueError("Inventory cannot exceed 28 items")
        return v

    @field_validator("equipped")
    @classmethod
    def slots_must_be_valid(cls, v: Dict[str, ItemSchema]) -> Dict[str, ItemSchema]:
        valid_slots = {
            "head", "body", "legs", "weapon", "shield",
            "cape", "neck", "gloves", "boots", "ring"
        }
        for slot in v:
            if slot not in valid_slots:
                raise ValueError(f"Invalid slot: {slot}")
        return v


class LoadoutSummary(BaseModel):
    name: str


class MessageResponse(BaseModel):
    message: str
