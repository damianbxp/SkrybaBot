from discord.ext import commands
from settings import *


bot = commands.Bot(command_prefix="!")

bot.load_extension(f'Cogs.quoteCommand')
bot.load_extension(f'Cogs.randomizeCommand')
bot.load_extension(f'Cogs.Greetings')
bot.load_extension(f'Cogs.General')


@bot.event
async def on_ready():
    print("Skryba przybył")

bot.run(DISCORD_BOT_TOKEN)