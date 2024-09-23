import discord
from Classes.Party import *

class Server:
    def __init__(self, server, channel_name, server_id):

        self.server_id = server_id
        self.channel_id = -1

        for channel in server.channels:
            if channel.name == channel_name:
                print('made it')
                self.channel_id = channel
                break

        self.server_name = server.name
        self.channel_name = channel_name
        self.party = Party

    def get_channel(self):
        return self.channel_id

    def get_server(self):
        return self.server_id