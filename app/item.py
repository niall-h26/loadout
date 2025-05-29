from typing import Optional, Dict, Any

class Item:
    def __init__(self, name: str, slot: Optional[str] = None, quantity: int = 1) -> None:
        """
        Represents an item in the game.

        :param name: Name of the item (e.g., "Abyssal Whip").
        :param slot: Slot this item is equipped in (e.g., "weapon", "head"), or None if in inventory.
        :param quantity: Quantity for stackable items (e.g., potions, food).
        """
        self.name: str = name
        self.slot: Optional[str] = slot
        self.quantity: int = quantity

    def is_equipped(self) -> bool:
        """
        Returns True if the item is equipped (i.e., has a slot assigned), otherwise False.
        """
        return self.slot is not None

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the Item instance into a dictionary format for saving to JSON.
        """
        return {
            "name": self.name,
            "slot": self.slot,
            "quantity": self.quantity
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Item":
        """
        Creates an Item instance from a dictionary (when loading from JSON).

        :param data: A dictionary with keys 'name', 'slot', and 'quantity'.
        :return: An Item instance created from the dictionary data.
        """
        return cls(
            name=data["name"],
            slot=data.get("slot"),
            quantity=data.get("quantity", 1)
        )
