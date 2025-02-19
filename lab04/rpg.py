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
            return ""
        return f"{self.name} is used"

    def __str__(self):
        ownership_status = self._ownership if self._ownership else "No owner"
        return f"Item(name={self.name}, description={self.description}, rarity={self.rarity}, ownership={ownership_status})"


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
            return ""
        return f"{self.name} is used, dealing {int(self.damage * self.attack_modifier)} damage"


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
            return ""
        return f"{self.name} is used, blocking {self.defense * self.defense_modifier * self.broken_modifier} damage"


class Potion(Item):
    def __init__(self, name, description='', rarity='common', value=0, type='', effective_time=0):
        super().__init__(name, description, rarity)
        self.value = value
        self.type = type
        self.effective_time = effective_time
        self.used = False

    def use(self):
        if not self._ownership or self.used:
            return ""
        self.used = True
        return f"{self._ownership} used {self.name}, and {self.type} increase {self.value} for {self.effective_time}s"

    @classmethod
    def from_ability(cls, name, owner, type):
        potion = cls(name=name, description='', rarity='common', value=50, type=type, effective_time=30)
        potion._ownership = owner
        return potion

    def __str__(self):
        ownership_status = self._ownership if self._ownership else "No owner"
        return f"Potion(name={self.name}, description={self.description}, rarity={self.rarity}, value={self.value}, type={self.type}, effective_time={self.effective_time}, ownership={ownership_status})"