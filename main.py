from discord.ext import commands
from apikeys import *

client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print("Bot initialized")
    print("---------------")


@client.command()
async def witam(ctx):
    await ctx.send("Witam")


client.run(BOTTOKEN)
