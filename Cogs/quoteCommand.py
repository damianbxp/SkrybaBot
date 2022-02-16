import random
import time
from discord import FFmpegPCMAudio
from discord.ext import commands
from random import randrange
import json
import os
from settings import *


def setup(bot):
    bot.add_cog(QuoteCommands(bot))


async def get_quote(quote_category=None, quote_id=None):
    with open(os.path.join(TEXT_QUOTES, "textquotes.json"), encoding="utf-8") as quotes_file:
        quotes = json.load(quotes_file)

    if quote_category is None:
        print("Telling random category")
        quote_category = random.choice(list(quotes.keys()))

    try:
        quote_category_id = int(quote_category)
        print(f"Quote category id: {quote_category_id}")
        quotes = list(quotes.values())
        if quote_id is None:
            print("Telling random quote")
            quote_id = randrange(0, len(quotes[quote_category_id]))
        else:
            try:
                quote_id = int(quote_id)
            except ValueError:
                return
        if quote_id < 0 or quote_id >= len(quotes[quote_category_id]):
            return

        return quotes[quote_category_id][quote_id]


    except ValueError:
        print(f"Quote category: {quote_category}")
        if quote_id is None:
            print("Telling random quote")
            quote_id = randrange(0, len(quotes[quote_category]))
        else:
            try:
                quote_id = int(quote_id)
            except ValueError:
                return

        if quote_id < 0 or quote_id >= len(quotes[quote_category]):
            return

        return quotes[quote_category][quote_id]


class QuoteCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author != self.bot.user:
            if message.content.lower().find("jak to jest być skrybą") != -1:
                quote = await get_quote("other", 0)
                await message.channel.send(quote["text"])

    @commands.command(brief="Zacytuj wskazany lub losowy cytat")
    async def q(self, ctx, category=None, quote_id=None):
        quote = await get_quote(category, quote_id)
        await ctx.send(quote["text"])

    @commands.command(brief="Zacytuj na głos. Muszisz być na kanale głosowym")
    async def t(self, ctx, category=None, quote_id=None):
        if ctx.author.voice:
            channel = ctx.message.author.voice.channel
            if not ctx.voice_client:
                await channel.connect()

            quote_file = await get_quote(category, quote_id)
            if quote_file is None:
                await ctx.send("Nie moge znaleść cytatu")
                return

            quote_file = quote_file["audio"]
            if quote_file is None:
                await ctx.send("Nie mogę znaleść tego cytatu w zbiorach")
                return

            if quote_file != "":
                ctx.voice_client.play(FFmpegPCMAudio("data/audio_quotes/" + quote_file))
            else:
                await ctx.send("Nie mogę wypowiedzieć tego cytatu")


        else:
            await ctx.send("Musisz być na kanale głosowym")

    @commands.command(brief="Opuść kanał głosowy")
    async def leave(self, ctx):
        if ctx.voice_client:
            await ctx.guild.voice_client.disconnect()
