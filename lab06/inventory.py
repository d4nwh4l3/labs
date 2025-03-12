import json

from item import DoubleHandedWeapon, Pike, Potion, RangedWeapon, Shield, SingleHandedWeapon

class InventoryJSONEncoder(json.JSONEncoder):
    """Custom JSON encoder for Inventory and Item objects"""
    def default(self, obj):
        if hasattr(obj, 'to_json'):
            return obj.to_json()
        return super().default(obj)

class Inventory:
    def __init__(self, owner=None):
        self.owner = owner
        self.items = []

    def add_item(self, item):
        item.pick_up(self.owner)
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            item.throw_away()
            self.items.remove(item)

    def view(self, type=None):
        if type:
            items_of_type = [item for item in self.items if isinstance(item, type)]
            items_list = [str(item) for item in items_of_type]
        else:
            items_list = [str(item) for item in self.items]
    
        output = "\n=== INVENTORY CONTENTS ===\n"
        for item in items_list:
            output += f"{item}\n\n"
        output += "======================="
        return output

    def __iter__(self):
        return iter(self.items)

    def __contains__(self, item):
        return item in self.items

    def to_json(self):
        inventory_dict = {
            'type': self.__class__.__name__,
            'owner': self.owner,
            'items': [item.to_json() for item in self.items]
        }
        return inventory_dict

    @staticmethod
    def get_encoder():
        """Returns the custom JSON encoder for Inventory objects"""
        return InventoryJSONEncoder

    @classmethod
    def from_json(cls, json_data):
        """
        Creates an Inventory instance from JSON data.
        
        Args:
            json_data (dict): Dictionary containing inventory data
                Required keys: 'owner', 'items'
                Each item in 'items' must have a 'type' key indicating the item class
        
        Returns:
            Inventory: New inventory instance with all items restored
        """
        instance = cls(owner=json_data['owner'])
        
        item_classes = {
            'SingleHandedWeapon': SingleHandedWeapon,
            'DoubleHandedWeapon': DoubleHandedWeapon,
            'Pike': Pike,
            'RangedWeapon': RangedWeapon,
            'Shield': Shield,
            'Potion': Potion
        }
        
        for item_data in json_data['items']:
            item_class = item_classes[item_data['type']]
            item = item_class.from_json(item_data)
            instance.items.append(item)
            
        return instance