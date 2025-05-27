class Item:
    def __init__(self, name, slot=None, quantity=1):
        """
        Represents an item in the game.

        :param name: Name of the item (e.g., "Abyssal Whip").
        :param slot: Slot this item is equipped in (e.g., "weapon", "head"), or None if in inventory.
        :param quantity: Quantity for stackable items (e.g., potions, food).
        """
        self.name = name              # The name of the item (e.g., "Shark", "Iron Full Helm")
        self.slot = slot              # The slot it's equipped in (e.g., "head"), or None if in inventory
        self.quantity = quantity      # How many of this item (for stackables)

    def is_equipped(self):
        """
        Returns True if the item is equipped (i.e., has a slot assigned), otherwise False.
        """
        return self.slot is not None

    def to_dict(self):
        """
        Converts the Item instance into a dictionary format for saving to JSON.
        """
        return {
            "name": self.name,
            "slot": self.slot,
            "quantity": self.quantity
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        Creates an Item instance from a dictionary (when loading from JSON).

        :param data: A dictionary with keys 'name', 'slot', and 'quantity'.
        :return: An Item instance created from the dictionary data.
        """
        return cls(
            name=data["name"],
            slot=data.get("slot"),               # slot may be missing if item is in inventory
            quantity=data.get("quantity", 1)     # default to 1 if quantity is not specified
        )