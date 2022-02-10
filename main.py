import random
import skryba_bot as s
from apikeys import *
import json
from discord.ext import commands



bot = commands.Bot(command_prefix="!")

bot.load_extension(f'Commands.quoteCommand')

bot.run(BOTTOKEN)