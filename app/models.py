class Loadout:
    def __init__(self, name, equipped, inventory):
        self.name = name
        self.equipped = {}
        self.inventory = []
    
    def validate(self):
        valid_slots = {"head", "body", "legs", "weapon", "shield", "cape", "neck", "gloves", "boots", "ring"}
        if self.name is None or self.name == "":
            raise ValueError("Loadout name cannot be empty")
        if self.inventory.length > 28:
            raise ValueError("Inventory cannot exceed 28 items")
        for slot in self.equipped:
            if slot not in valid_slots:
                raise ValueError(f"Invalid slot: {slot}")
        
