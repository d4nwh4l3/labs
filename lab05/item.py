class Item:
    def __init__(self, name, description='', rarity='common'):
        self.name = name
        self.description = description
        self.rarity = rarity
        self._ownership = ''

    def pick_up(self, character):
        self._ownership = character
        return f"{self.name} is now owned by {character}"

    def throw_away(self):
        self._ownership = ''
        return f"{self.name} is thrown away"

    def use(self):
        if not self._ownership:
            return "This item has no owner"
        return f"{self.name} is used"

    def __str__(self):
        ownership_status = self._ownership if self._ownership else "No owner"
        if self.rarity == 'legendary':
            return (
                "\n" + "*" * 30 + "\n"
                f"LEGENDARY ITEM: {self.name}\n"
                f"Description: {self.description}\n"
                f"Owner: {ownership_status}\n" +
                "*" * 30
            )
        return (
            f"Item: {self.name}\n"
            f"Description: {self.description}\n"
            f"Rarity: {self.rarity}\n"
            f"Owner: {ownership_status}"
        )

class Weapon(Item):
    def __init__(self, name, description='', rarity='common', damage=0, type=''):
        super().__init__(name, description, rarity)
        self.damage = damage
        self.type = type
        self.active = False
        self.attack_modifier = 1.15 if rarity == 'legendary' else 1.0

    def equip(self):
        self.active = True
        return f"{self.name} is equipped by {self._ownership}"

    def use(self):
        if not self._ownership or not self.active:
            return "This weapon cannot be used"
        return f"{self.name} is used, dealing {int(self.damage * self.attack_modifier)} damage"

    def attack_move(self):
        pass

class SingleHandedWeapon(Weapon):
    def attack_move(self):
        return f"{self._ownership} slashes with {self.name}"

class DoubleHandedWeapon(Weapon):
    def attack_move(self):
        return f"{self._ownership} spins with {self.name}"

class Pike(Weapon):
    def attack_move(self):
        return f"{self._ownership} thrusts with {self.name}"

class RangedWeapon(Weapon):
    def attack_move(self):
        return f"{self._ownership} shoots with {self.name}"

class Shield(Item):
    def __init__(self, name, description='', rarity='common', defense=0, broken=False):
        super().__init__(name, description, rarity)
        self.defense = defense
        self.broken = broken
        self.active = False
        self.defense_modifier = 1.10 if rarity == 'legendary' else 1.0
        self.broken_modifier = 0.5 if broken else 1.0

    def equip(self):
        self.active = True
        return f"{self.name} is equipped by {self._ownership}"

    def use(self):
        if not self._ownership or not self.active:
            return "This shield cannot be used"
        return f"{self.name} blocks {self.defense * self.defense_modifier * self.broken_modifier} damage"

    def __str__(self):
        base_str = super().__str__()
        return (f"{base_str}\n"
                f"Defense: {self.defense}\n"
                f"Status: {'Broken' if self.broken else 'Intact'}")

class Potion(Item):
    def __init__(self, name, description='', rarity='common', value=0, type='', effective_time=0):
        super().__init__(name, description, rarity)
        self.value = value
        self.type = type
        self.effective_time = effective_time
        self.used = False

    def use(self):
        if not self._ownership or self.used:
            return "This potion cannot be used"
        self.used = True
        return f"{self._ownership} used {self.name}, {self.type} increased by {self.value} for {self.effective_time}s"

    def __str__(self):
        ownership_status = self._ownership if self._ownership else "No owner"
        return (
            f"Potion: {self.name}\n"
            f"Type: {self.type}\n"
            f"Value: {self.value}\n"
            f"Duration: {self.effective_time}s\n"
            f"Owner: {ownership_status}"
        )