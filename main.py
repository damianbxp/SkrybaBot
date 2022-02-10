from discord.ext import commands
from settings import *


bot = commands.Bot(command_prefix="!")

bot.load_extension(f'Commands.quoteCommand')
bot.load_extension(f'Commands.randomizeCommand')

bot.run(DISCORD_BOT_TOKEN)