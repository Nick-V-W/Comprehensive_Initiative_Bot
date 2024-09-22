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

global main_server
configured = False

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    guild = message.channel.guild

    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('fuck you >:(')

    # configure the server name and read/load data channel for the bot
    if message.content.startswith('$divine'):
        global main_server
        global configured
        msg = message.content
        info = msg.replace('$divine$', '').split('$')
        if len(info) != 2:
            await message.channel.send('I can\'t read that silly!! Please $divine using the following form:')
            await message.channel.send('$divine$Name Of Server$Name of PC Channel')
        else:
            server, channel = info.pop(0), info.pop(0)
            main_server = Server(server, channel)
            await message.channel.send('Will read future PC info from the ' + channel + ' channel in the ' + server + ' server')
            await message.channel.send('Please $divine again if this is incorrect')
            configured = True


    if message.content.startswith('$gather party'):
        if configured:
            await GetDiscordInfo.getparty(guild, message.author.name, main_server.get_channel())
        else:
            await message.channel.send('Please configure me using $divine!')


client.run(TOKEN)