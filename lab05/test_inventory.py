from item import SingleHandedWeapon, DoubleHandedWeapon, Pike, RangedWeapon, Shield, Potion
from inventory import Inventory

def main():
    print("\n=== Creating Test Items ===")

    master_sword = SingleHandedWeapon(
        name='Master Sword', 
        description='A legendary sword', 
        rarity='legendary', 
        damage=300, 
        type='sword'
    )
    
    muramasa = DoubleHandedWeapon(
        name='Muramasa', 
        description='A legendary katana', 
        rarity='legendary', 
        damage=580, 
        type='katana'
    )
    
    gungnir = Pike(
        name='Gungnir', 
        description='A legendary spear', 
        rarity='legendary', 
        damage=290, 
        type='spear'
    )
    
    belthronding = RangedWeapon(
        name='Belthronding', 
        description='A legendary bow', 
        rarity='legendary', 
        damage=500, 
        type='bow'
    )


    hp_potion = Potion(
        name='Health Potion', 
        description='Restores health', 
        rarity='common', 
        value=50, 
        type='health', 
        effective_time=30
    )
    
    broken_pot_lid = Shield(
        name='Broken Pot Lid', 
        description='A broken shield', 
        rarity='common', 
        defense=10, 
        broken=True
    )
    
    round_shield = Shield(
        name='Round Shield', 
        description='A sturdy shield', 
        rarity='common', 
        defense=50
    )

    print("\n=== Testing Inventory System ===")

    beleg_backpack = Inventory(owner='Beleg')
    

    print("\nAdding items to inventory...")
    items_to_add = [belthronding, hp_potion, master_sword, 
                    broken_pot_lid, muramasa, gungnir, round_shield]
    for item in items_to_add:
        beleg_backpack.add_item(item)


    print("\n=== Viewing All Items ===")
    print(beleg_backpack.view())


    print("\n=== Viewing Shields Only ===")
    print(beleg_backpack.view(type=Shield))


    print("\n=== Testing Weapon Functionality ===")
    if master_sword in beleg_backpack:
        master_sword.equip()
        print(f"\nTesting Master Sword:")
        print(master_sword)
        print(f"Attack Move: {master_sword.attack_move()}")
        print(f"Use Result: {master_sword.use()}")


    print("\n=== Testing All Weapon Attack Moves ===")
    for item in beleg_backpack:
        if isinstance(item, SingleHandedWeapon):
            print(f"\nSingle-Handed Weapon: {item.attack_move()}")
        elif isinstance(item, DoubleHandedWeapon):
            print(f"\nDouble-Handed Weapon: {item.attack_move()}")
        elif isinstance(item, Pike):
            print(f"\nPike: {item.attack_move()}")
        elif isinstance(item, RangedWeapon):
            print(f"\nRanged Weapon: {item.attack_move()}")


    print("\n=== Testing Item Removal ===")
    print(f"Removing {broken_pot_lid.name}...")
    beleg_backpack.remove_item(broken_pot_lid)
    print("\nUpdated inventory after removal:")
    print(beleg_backpack.view())

if __name__ == "__main__":
    main()