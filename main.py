import os.path
from app.models import Loadout
from app.storage import LoadoutStorage
from app.item import Item

def main():
    # Example equipped and inventory data (replace with your real items/structure)
    equipped = {
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

    inventory = [
        Item(name="Super Restore Potion", quantity=4),
        Item(name="Shark", quantity=10),
        Item(name="Antidote++", quantity=2),
        Item(name="Prayer Potion", quantity=5)
    ]

    # Create storage instance
    storage = LoadoutStorage()

    while True:
        print("What would you like to do?")
        print("1. Create a new loadout")
        print("2. Load an existing loadout")
        print("3. List all loadouts")
        print("4. Delete a loadout")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()
        if choice == '1':
            try:
                my_loadout = Loadout(name =input("Enter the name of the loadout: ").strip(), equipped=equipped, inventory=inventory)
                my_loadout.validate()
                
                overwrite = False
                if os.path.exists(os.path.join("loadouts", my_loadout.name + '.json')):
                    overwrite_input = input("Loadout already exists. Overwrite? (yes/no): ").strip().lower()
                    overwrite = (overwrite_input == 'yes')

                storage.save(my_loadout, overwrite=overwrite)
                print(f"Loadout '{my_loadout.name}' saved successfully.")

            except Exception as e:
                print(f"Failed to save loadout: {e}")
        elif choice == '2':
            try:
                loaded_loadout = storage.load(input("Enter the name of the loadout to load: "))
                print(f"Loadout '{loaded_loadout.name}' loaded successfully.")
                print("Equipped items:")

                for slot, item in loaded_loadout.equipped.items():
                    print(f"  {slot.title()}: {item}")
                print("Inventory items:", loaded_loadout.inventory)
            
            except Exception as e:
                print(f"Failed to load loadout: {e}")
        elif choice == '3':
            try:
                loadouts = storage.list_loadouts()
                print("Available loadouts:")
                for l in loadouts:
                    print(f" - {l}")
            
            except Exception as e:
                print(f"Failed to list loadouts: {e}")
        elif choice == '4':
            try:
                delete_name = input("Enter the name of the loadout to delete: ")
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