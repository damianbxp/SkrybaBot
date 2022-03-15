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


async def get_quote(quote_id, source: str):
    with open(os.path.join(source["dir"], source["file"]), encoding="utf-8") as quotes_file:
        quotes = json.load(quotes_file)

    try:
        # get quote by id
        quote_id = int(quote_id)
        if 0 <= quote_id < len(quotes):
            return quotes[quote_id]
        else:
            return

    except ValueError:
        # get quote by tag
        matched_quotes = [q for q in quotes if q["tag"] == quote_id]
        return matched_quotes[0] if len(matched_quotes) > 0 else None

async def play_file(ctx, quote_id, quote_type):
    if ctx.author.voice:
        channel = ctx.message.author.voice.channel
        if not ctx.voice_client:
            await channel.connect()

        quote_file = await get_quote(quote_id, QUOTE_TYPES[quote_type])

        if quote_file is None:
            await ctx.send("Nie mogę znaleść tego cytatu w zbiorach")
            return

        quote_file = quote_file["audio"]

        if quote_file != "":
            ctx.voice_client.play(FFmpegPCMAudio("data/audio_quotes/" + quote_file))
        else:
            await ctx.send("Nie mogę wypowiedzieć tego cytatu")

    else:
        await ctx.send("Musisz być na kanale głosowym")




class QuoteCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author != self.bot.user:
            if message.content.lower().find("jak to jest być skrybą") != -1:
                quote = await get_quote(0, QUOTE_TYPES["skryba_text"])
                await message.channel.send(quote["text"])

    @commands.command(brief="Zacytuj wskazany lub losowy cytat")
    async def q(self, ctx, quote_id=None):
        quote = await get_quote(quote_id, QUOTE_TYPES["normal_text"])
        if quote is not None:
            await ctx.send(quote["text"])
        else:
            await ctx.send("Nie moge znaleść cytatu")

    @commands.command(brief="Zacytuj na głos. Muszisz być na kanale głosowym")
    async def t(self, ctx, quote_id=None):
        await play_file(ctx, quote_id, "normal_audio")

    @commands.command(brief="Obraź")
    async def i(self, ctx, quote_id=None):
        await play_file(ctx, quote_id, "insult_audio")

    @commands.command(brief="Opuść kanał głosowy")
    async def leave(self, ctx):
        if ctx.voice_client:
            await ctx.guild.voice_client.disconnect()
