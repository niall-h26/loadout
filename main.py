from app.models import Loadout
from app.storage import LoadoutStorage

def main():
    # Example equipped and inventory data (replace with your real items/structure)
    equipped = {
        "head": "Iron Full Helm",
        "body": "Steel Platebody",
        "legs": "Steel Platelegs",
        "weapon": "Rune Sword",
        "shield": "Dragon Square Shield",
        "cape": "Fire Cape",
        "neck": "Amulet of Power",
        "gloves": "Barrows Gloves",
        "boots": "Dragon Boots",
        "ring": "Ring of Wealth"
    }

    inventory = ["Prayer Potion(4)", "Shark"]

    # Create a Loadout instance
    my_loadout = Loadout(name="test_loadout", equipped=equipped, inventory=inventory)

    # Create storage instance
    storage = LoadoutStorage()

    # Save the loadout
    try:
        my_loadout.validate()
        storage.save(my_loadout)
        print(f"Loadout '{my_loadout.name}' saved successfully.")
    except Exception as e:
        print(f"Failed to save loadout: {e}")

if __name__ == "__main__":
    main()