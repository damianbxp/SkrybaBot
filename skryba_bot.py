import random
import discord
import json
from discord.ext import commands

TEXTQUOTESFILE = "textquotes.json"

bot = commands.Bot(command_prefix="!")




async def on_ready(self):
    print("Initialized bot")
    print("===================")

@commands.command(description = "Zacytuj")
async def q(ctx, *args):
    if len(args) > 0:
        quote_id = args[0]
    else:
        quote_id = None

    await ctx.send(get_quote(quote_id)["text"])

async def on_message(message):
    if message.author.bot:
        return

    if message.content.lower().find("jak to jest być skrybą") != -1:
        f = open(TEXTQUOTESFILE, encoding="utf-8")
        quote = json.load(f)[0]["text"]
        await message.channel.send(quote)
        f.close()
