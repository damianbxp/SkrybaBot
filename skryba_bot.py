import random

import discord
import json
COMMANDPREFIX = "!"
TEXTQUOTESFILE = "textquotes.json"


def get_quote(quote_id=None):
    f = open(TEXTQUOTESFILE, encoding="utf-8")
    quotes = json.load(f)
    f.close()
    if quote_id is None:
        quote_id = random.randrange(0, len(quotes))
    return quotes[quote_id]


class Skryba(discord.Client):
    async def on_ready(self):
        print("Initialized bot")
        print("===================")

    async def on_message(self, message):
        if message.author.bot:
            return
        if message.content[0] == COMMANDPREFIX:
            command = message.content[1:].split(" ")

            if command[0] == "q":
                if len(command) > 1:
                    quote_id = int(command[1])
                else:
                    quote_id = None

                await message.channel.send(get_quote(quote_id)["text"])

        if message.content.lower().find("jak to jest być skrybą") != -1:
            f = open(TEXTQUOTESFILE, encoding="utf-8")
            quote = json.load(f)[0]["text"]
            await message.channel.send(quote)
            f.close()
