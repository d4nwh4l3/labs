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

    def to_json(self):
        """Converts item data into a JSON-encodable dictionary"""
        return {
            'type': self.__class__.__name__,
            'name': self.name,
            'description': self.description,
            'rarity': self.rarity,
            'ownership': self._ownership
        }

    @classmethod
    def from_json(cls, json_data):
        """
        Creates an Item instance from JSON data.
        
        Args:
            json_data (dict): Dictionary containing item data
                Required keys: 'name', 'description', 'rarity', 'ownership'
        
        Returns:
            Item: New instance of the appropriate item class
        """
        instance = cls(
            name=json_data['name'],
            description=json_data['description'],
            rarity=json_data['rarity']
        )
        if json_data['ownership']:
            instance.pick_up(json_data['ownership'])
        return instance


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

    def to_json(self):
        json_data = super().to_json()
        json_data.update({
            'damage': self.damage,
            'weapon_type': self.type,
            'active': self.active,
            'attack_modifier': self.attack_modifier
        })
        return json_data
    
    @classmethod
    def from_json(cls, json_data):
        """
        Creates a Weapon instance from JSON data.
        
        Args:
            json_data (dict): Dictionary containing weapon data
                Additional required keys: 'damage', 'weapon_type', 'active', 'attack_modifier'
        
        Returns:
            Weapon: New instance of the appropriate weapon class
        """
        instance = super().from_json(json_data)
        instance.damage = json_data['damage']
        instance.type = json_data['weapon_type']
        instance.active = json_data['active']
        instance.attack_modifier = json_data['attack_modifier']
        return instance

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

    def to_json(self):
        json_data = super().to_json()
        json_data.update({
            'defense': self.defense,
            'broken': self.broken,
            'active': self.active,
            'defense_modifier': self.defense_modifier,
            'broken_modifier': self.broken_modifier
        })
        return json_data

    @classmethod
    def from_json(cls, json_data):
        """
        Creates a Shield instance from JSON data.
        
        Args:
            json_data (dict): Dictionary containing shield data
                Additional required keys: 'defense', 'broken', 'active',
                'defense_modifier', 'broken_modifier'
        
        Returns:
            Shield: New shield instance
        """
        instance = cls(
            name=json_data['name'],
            description=json_data['description'],
            rarity=json_data['rarity'],
            defense=json_data['defense'],
            broken=json_data['broken']
        )
        if json_data['ownership']:
            instance.pick_up(json_data['ownership'])
        instance.active = json_data['active']
        instance.defense_modifier = json_data['defense_modifier']
        instance.broken_modifier = json_data['broken_modifier']
        return instance

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

    def to_json(self):
        json_data = super().to_json()
        json_data.update({
            'value': self.value,
            'potion_type': self.type,
            'effective_time': self.effective_time,
            'used': self.used
        })
        return json_data

    @classmethod
    def from_json(cls, json_data):
        """
        Creates a Potion instance from JSON data.
        
        Args:
            json_data (dict): Dictionary containing potion data
                Additional required keys: 'value', 'potion_type',
                'effective_time', 'used'
        
        Returns:
            Potion: New potion instance
        """
        instance = cls(
            name=json_data['name'],
            description=json_data['description'],
            rarity=json_data['rarity'],
            value=json_data['value'],
            type=json_data['potion_type'],
            effective_time=json_data['effective_time']
        )
        if json_data['ownership']:
            instance.pick_up(json_data['ownership'])
        instance.used = json_data['used']
        return instance