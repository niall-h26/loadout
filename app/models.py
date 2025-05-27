from .item import Item

class Loadout:
    def __init__(self, name, equipped : dict, inventory: list):
        """
        Represents a character's loadout with equipped gear and inventory.

        :param name: Name of the loadout (e.g., "Vorkath Melee").
        :param equipped: Dictionary mapping equipment slots to Item instances.
        :param inventory: List of Item instances representing inventory contents.
        """
        self.name = name
        self.equipped = equipped      # Dictionary: slot name (str) -> Item instance
        self.inventory = inventory    # List of Item instances
    
    def validate(self):
        """
        Validates the loadout:
        - Name must not be empty.
        - Inventory must not exceed 28 items.
        - All equipped slots must be valid.
        """
        valid_slots = {"head", "body", "legs", "weapon", "shield", "cape", "neck", "gloves", "boots", "ring"}
        if self.name is None or self.name == "":
            raise ValueError("Loadout name cannot be empty")
        if len(self.inventory) > 28:
            raise ValueError("Inventory cannot exceed 28 items")
        for slot in self.equipped:
            if slot not in valid_slots:
                raise ValueError(f"Invalid slot: {slot}")
        
    def to_dict(self):
        """
        Serializes the Loadout into a dictionary (e.g., for saving to JSON).

        :return: A dictionary representation of the Loadout.
        """
        return {
            "name": self.name,
            "equipped": {slot: item.to_dict() for slot, item in self.equipped.items()},
            # Convert each equipped Item to a dictionary, preserving slot
            "inventory": [item.to_dict() for item in self.inventory]
            # Convert each inventory Item to a dictionary
        }
    
    @classmethod
    def from_dict(cls, data):
            """
            Creates a Loadout instance from a dictionary (e.g., when loading from JSON).

            :param data: Dictionary with keys 'name', 'equipped', and 'inventory'.
            :return: A Loadout instance.
            """
            equipped_data = data.get("equipped", {})
            inventory_data = data.get("inventory", [])

            # Reconstruct equipped dict by converting each slot's item dict back into an Item object
            equipped = {slot: Item.from_dict(item_data) for slot, item_data in equipped_data.items()}
            
            # Reconstruct inventory list of Item objects from dictionaries
            inventory = [Item.from_dict(item_data) for item_data in inventory_data]

            return cls(
                name=data.get("name"),
                equipped=equipped,
                inventory=inventory
            )
    
    def __str__(self):
        return f"Loadout: {self.name} (Equipped: {len(self.equipped)} slots, Inventory: {len(self.inventory)} items)"
    
    def __repr__(self):
        return f"Loadout(name={self.name}, equipped={self.equipped}, inventory={self.inventory})"