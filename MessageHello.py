# This example requires the 'message_content' intent.

import discord
import GetDiscordInfo
from Config import TOKEN


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    guild = message.channel.guild

    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('hiii <3')

    if message.content.startswith('$put party: '):
        await message.channel

    if message.content.startswith('$gather party'):
        await GetDiscordInfo.getparty(guild, message.author.name, message.channel)

client.run(TOKEN)