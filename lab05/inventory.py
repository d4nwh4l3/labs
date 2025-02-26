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