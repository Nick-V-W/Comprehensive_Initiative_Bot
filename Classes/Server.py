import discord
import Party

class Server:
    def __init__(self, server, read_channel, server_party: Party):
            self.server = server
            self.read_channel = read_channel
            self.party = server_party