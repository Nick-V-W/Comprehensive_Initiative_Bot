import discord
from Classes.Party import *

class Server:
    def __init__(self, server, read_channel):
        # TODO add logic for obtaining server/channel id here!
        self.server = server
        self.read_channel = read_channel
        self.party = Party

    def get_channel(self):
        return self.read_channel