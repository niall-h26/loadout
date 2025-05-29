import os.path
from typing import Dict, List

from app.models import Loadout
from app.storage import LoadoutStorage
from app.item import Item


def main() -> None:
    # Equipped items: mapping of slot name to Item instance
    equipped: Dict[str, Item] = {
        "head": Item(name="Iron Full Helm", slot="head"),
        "body": Item(name="Steel Platebody", slot="body"),
        "legs": Item(name="Steel Platelegs", slot="legs"),
        "weapon": Item(name="Rune Sword", slot="weapon"),
        "shield": Item(name="Dragon Square Shield", slot="shield"),
        "cape": Item(name="Fire Cape", slot="cape"),
        "neck": Item(name="Amulet of Power", slot="neck"),
        "gloves": Item(name="Barrows Gloves", slot="gloves"),
        "boots": Item(name="Dragon Boots", slot="boots"),
        "ring": Item(name="Ring of Wealth", slot="ring")
    }

    # Inventory is a list of Item instances
    inventory: List[Item] = [
        Item(name="Super Restore Potion", quantity=4),
        Item(name="Shark", quantity=10),
        Item(name="Antidote++", quantity=2),
        Item(name="Prayer Potion", quantity=5)
    ]

    # Create storage instance
    storage: LoadoutStorage = LoadoutStorage()

    while True:
        print("What would you like to do?")
        print("1. Create a new loadout")
        print("2. Load an existing loadout")
        print("3. List all loadouts")
        print("4. Delete a loadout")
        print("5. Exit")
        choice: str = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            try:
                loadout_name: str = input("Enter the name of the loadout: ").strip()
                my_loadout: Loadout = Loadout(name=loadout_name, equipped=equipped, inventory=inventory)
                my_loadout.validate()

                overwrite: bool = False
                if os.path.exists(os.path.join("loadouts", my_loadout.name + '.json')):
                    overwrite_input: str = input("Loadout already exists. Overwrite? (yes/no): ").strip().lower()
                    overwrite = (overwrite_input == 'yes')

                storage.save(my_loadout, overwrite=overwrite)
                print(f"Loadout '{my_loadout.name}' saved successfully.")

            except Exception as e:
                print(f"Failed to save loadout: {e}")

        elif choice == '2':
            try:
                name_to_load: str = input("Enter the name of the loadout to load: ")
                loaded_loadout: Loadout = storage.load(name_to_load)
                print(f"Loadout '{loaded_loadout.name}' loaded successfully.")
                print("Equipped items:")
                for slot, item in loaded_loadout.equipped.items():
                    print(f"  {slot.title()}: {item.name}")
                print("Inventory items:")
                for item in loaded_loadout.inventory:
                    print(f"  {item.name} (Quantity: {item.quantity})")

            except Exception as e:
                print(f"Failed to load loadout: {e}")

        elif choice == '3':
            try:
                loadouts: List[str] = storage.list_loadouts()
                print("Available loadouts:")
                for l in loadouts:
                    print(f" - {l}")

            except Exception as e:
                print(f"Failed to list loadouts: {e}")

        elif choice == '4':
            try:
                delete_name: str = input("Enter the name of the loadout to delete: ")
                storage.delete(delete_name)
                print(f"Loadout '{delete_name}' deleted successfully.")

            except ValueError as ve:
                print(ve)
            except Exception as e:
                print(f"Failed to delete loadout: {e}")

        elif choice == '5':
            print("Exiting the program.")
            break


if __name__ == "__main__":
    main()