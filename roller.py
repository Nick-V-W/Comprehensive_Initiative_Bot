import random
from tabulate import tabulate

def roll_d20(advantage_state=None):
    roll1 = random.randint(1, 20)
    roll2 = random.randint(1, 20)

    if advantage_state == "advantage":
        return max(roll1, roll2)  
    elif advantage_state == "disadvantage":
        return min(roll1, roll2)  
    else:
        return roll1  

def roll_initiative(characters):
    initiative_results = []

    for character in characters:
        name = character['name']
        dex_mod = character['dexterity_modifier']
        advantage_state = character.get('advantage_state', None)
        gift_of_alacrity = character.get('gift_of_alacrity', False)
        roll = roll_d20(advantage_state)
        initiative = roll + dex_mod 
        if gift_of_alacrity:
            alacrity_bonus = random.randint(1, 8)
            initiative += alacrity_bonus
        initiative_results.append({'name': name, 'roll': initiative, 'raw_roll': roll})

    initiative_results.sort(key=lambda x: x['roll'], reverse=True)

    return initiative_results

# Example list of characters with Dexterity modifiers
characters = [
    {'name': 'Aragorn', 'dexterity_modifier': 3},
    {'name': 'Legolas', 'dexterity_modifier': 5},
    {'name': 'Gimli', 'dexterity_modifier': -1},
    {'name': 'Frodo', 'dexterity_modifier': 4},
    {'name': 'Gandalf', 'dexterity_modifier': 2, 
     'gift_of_alacrity': True}
    
]
monsters = [
    {'name': 'Goblin', 'dexterity_modifier': 2}
]
# Roll initiative for all characters
initiative_order = roll_initiative(characters + monsters)

# Print out the initiative order


sorted_initiative = sorted(initiative_order, key=lambda x: x['roll'], reverse=True)

# Prepare data for tabulation
table_data = []
for result in sorted_initiative:
    row = [result['name'], result['raw_roll'], result['roll']]
    table_data.append(row)
    
headers = ["Name", "Raw Roll", "Initiative"]

    # Print table using tabulate
table_init = tabulate(table_data, headers=headers, tablefmt="pretty")
print(f"```ansi\n{table_init}\n```")
