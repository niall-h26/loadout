import os
import json
from typing import List
from .models import Loadout

class LoadoutStorage:
    def __init__(self, directory: str = "loadouts") -> None:
        self.directory = directory
        if not os.path.exists(directory):
            os.makedirs(directory)

    def save(self, loadout: Loadout, overwrite: bool = False) -> None:
        """
        Save the loadout to a file.
        """
        filename = os.path.join(self.directory, loadout.name + '.json')
        
        if not overwrite and os.path.exists(filename):
            raise ValueError(f"Loadout '{loadout.name}' already exists.")

        try:
            with open(filename, 'w') as file:
                json.dump(loadout.to_dict(), file)
        
        except Exception as e:
            raise ValueError(f"Failed to save loadout '{loadout.name}': {e}")

    def load(self, name: str) -> Loadout:
        """
        Load the loadout from a file.
        """
        try:
            filename = os.path.join(self.directory, f"{name}.json")
            with open(filename, 'r') as file:
                data = json.load(file)
                return Loadout.from_dict(data)
        
        except FileNotFoundError:
            raise ValueError(f"Loadout file '{name}' not found.")
        
        except Exception as e:
            raise ValueError(f"An error occurred while loading the loadout: {e}")
        
    def delete(self, name: str) -> None:
        """
        Delete the loadout file.
        """
        try:
            filename = os.path.join(self.directory, f"{name}.json")
            os.remove(filename)
        
        except FileNotFoundError:
            raise ValueError(f"Loadout file '{name}' not found.")
        
        except Exception as e:
            raise ValueError(f"An error occurred while deleting the loadout: {e}")
    
    def list_loadouts(self) -> List[str]:
        """
        List all loadouts in the storage directory.
        """
        try:
            files = [f for f in os.listdir(self.directory) if f.endswith('.json')]
            return [os.path.splitext(f)[0] for f in files]
        
        except Exception as e:
            raise ValueError(f"An error occurred while listing loadouts: {e}")
