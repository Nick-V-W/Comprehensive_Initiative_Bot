import discord
import random

class PlayerCharacter:
    def __init__(self, char_name, dex_mod, con_mod):
            self.name = char_name
            self.dex_mod = dex_mod
            self.con_mod = con_mod

    def roll_standard(self):
            d20 = random.randint(1, 20) + self.dex_mod
            return d20
