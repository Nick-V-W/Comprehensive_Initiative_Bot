# This example requires the 'message_content' intent.
from operator import truediv

import discord
import GetDiscordInfo
from Classes.Server import Server
from Config import TOKEN


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

servers = {}
global main_server

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    guild = message.channel.guild
    server_id = message.guild.id
    message_content = message.content
    server = servers.get(server_id)

    if message.author == client.user:
        return

    if message_content.startswith('$hello'):
        await message.channel.send('fuck you >:(')

    # configure the server name and read/load data channel for the bot
    if message_content.startswith('$divine '):
        global main_server
        msg = message.content
        channel_name = msg.replace('$divine ', '')

        # TODO comment better!

        # if the server id already exists, make sure to remove the existing value from the dictionary to start clean
        if server is not None:
            servers.pop(server_id)

        # add server the message is from to dictionary in a "server_id" : "server_object" pair
        main_server = Server(client.get_guild(server_id), channel_name, server_id)
        servers.update({server_id: main_server})

        # if the name of the channel isn't found,
        if main_server.get_channel() == -1:
            await message.channel.send('Channel named: `' + channel_name + "` not found!")
            await message.channel.send('Please $divine again with existing channel')
        else:
            await message.channel.send('Will read future PC info from the ' + channel_name + ' channel')
            await message.channel.send('Please $divine again if this is incorrect')

    if message_content.startswith('$gather party'):
        # make sure valid server and channel exists
        if server is not None and server.get_channel() != -1 :
            await message.channel.send('Gathering party...')
            # await GetDiscordInfo.getparty(guild, message.author.name, server.get_channel())
        else:
            await message.channel.send('Please configure me using $divine!')

client.run(TOKEN)