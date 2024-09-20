import discord

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

async def getmsg(ctx, channel: discord.TextChannel, member: discord.Member):
    msg = discord.utils.get(await channel.history(limit=100).flatten, author=member)
    print(msg + '<--- LMAO' )


# collect users in server
async def getparty(guild, author, channel):
    async for member in guild.fetch_members(limit=150):
        if author == member.name:
            await getmsg(channel, member)
            print(member.name)




