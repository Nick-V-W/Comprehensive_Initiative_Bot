import random

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

# Roll initiative for all characters
initiative_order = roll_initiative(characters + monsters)

# Print out the initiative order
for i, result in enumerate(initiative_order, start=1):
    print(f"{i}. {result['name']} - Initiative Roll: {result['roll']} (Raw Roll: {result['raw_roll']})")
