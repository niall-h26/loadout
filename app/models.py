class Loadout:
    def __init__(self, name, equipped, inventory):
        self.name = name
        self.equipped = equipped
        self.inventory = inventory
    
    def validate(self):
        valid_slots = {"head", "body", "legs", "weapon", "shield", "cape", "neck", "gloves", "boots", "ring"}
        if self.name is None or self.name == "":
            raise ValueError("Loadout name cannot be empty")
        if len(self.inventory) > 28:
            raise ValueError("Inventory cannot exceed 28 items")
        for slot in self.equipped:
            if slot not in valid_slots:
                raise ValueError(f"Invalid slot: {slot}")
        
    def to_dict(self):
        return {
            "name": self.name,
            "equipped": self.equipped,
            "inventory": self.inventory
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get("name"),
            equipped=data.get("equipped", []),
            inventory=data.get("inventory", [])
        )
    
    def __str__(self):
        return f"Loadout: {self.name} (Equipped: {len(self.equipped)} slots, Inventory: {len(self.inventory)} items)"
    
    def __repr__(self):
        return f"Loadout(name={self.name}, equipped={self.equipped}, inventory={self.inventory})"