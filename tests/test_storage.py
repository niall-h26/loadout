import pytest
from app.storage import LoadoutStorage
from app.models import Loadout
from app.item import Item
from typing import Dict, List
from pathlib import Path

@pytest.fixture
def temp_storage_dir(tmp_path: Path) -> Path:
    dir_path = tmp_path / "loadouts"
    dir_path.mkdir()
    return dir_path

def test_save_and_load_loadout(temp_storage_dir: Path):
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

    inventory: List[Item] = [
        Item(name="Super Restore Potion", quantity=4),
        Item(name="Shark", quantity=10),
        Item(name="Antidote++", quantity=2),
        Item(name="Prayer Potion", quantity=5)
    ]

    storage = LoadoutStorage(directory=str(temp_storage_dir))
    loadout_name = "test_loadout"
    my_loadout = Loadout(name=loadout_name, equipped=equipped, inventory=inventory)
    my_loadout.validate()

    storage.save(my_loadout, overwrite=True)
    loaded = storage.load(loadout_name)

    assert loaded.name == my_loadout.name
    assert loaded.equipped["head"].name == "Iron Full Helm"
    assert len(loaded.inventory) == 4

def test_delete_loadout(temp_storage_dir: Path):
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

    inventory: List[Item] = [
        Item(name="Super Restore Potion", quantity=4),
        Item(name="Shark", quantity=10),
        Item(name="Antidote++", quantity=2),
        Item(name="Prayer Potion", quantity=5)
    ]

    storage = LoadoutStorage(directory=str(temp_storage_dir))
    loadout_name = "test_loadout"
    my_loadout = Loadout(name=loadout_name, equipped=equipped, inventory=inventory)
    my_loadout.validate()
    storage.save(my_loadout, overwrite=True)

    loaded = storage.load(loadout_name)
    assert loaded.name == my_loadout.name

    storage.delete(my_loadout.name)

    with pytest.raises(ValueError, match="not found"):
        storage.load(my_loadout.name)

