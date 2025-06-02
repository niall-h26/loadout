from app.item import Item

def test_equipped_item_creation():
    item = Item(name="Iron Full Helm", slot="head", quantity=1)
    assert item.name == "Iron Full Helm"
    assert item.slot == "head"
    assert item.quantity == 1

def test_inventory_item_creation():
    item = Item(name="Shark", slot=None, quantity=5)
    assert item.name == "Shark"
    assert item.slot is None
    assert item.quantity == 5

def test_item_dict_roundtrip():
    item = Item(name="Whip", slot="weapon", quantity=1)
    data = item.to_dict()
    item2 = Item.from_dict(data)
    assert item2.name == "Whip"
    assert item2.slot == "weapon"
    assert item2.quantity == 1