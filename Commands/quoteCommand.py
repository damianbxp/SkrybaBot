from discord.ext import commands
from random import randrange
import json

TEXTQUOTESFILE = "textquotes.json"

def setup(bot):
    bot.add_cog(QuoteCommands(bot))

def get_quote(quote_id=None):
    f = open(TEXTQUOTESFILE, encoding="utf-8")
    quotes = json.load(f)
    f.close()
    if quote_id is None:
        quote_id = randrange(0, len(quotes))
    return quotes[quote_id]

class QuoteCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Zacytuj")
    async def q(self, ctx, *args):
        if len(args) > 0:
            quote_id = int(args[0])
        else:
            quote_id = None

        await ctx.send(get_quote(quote_id)["text"])