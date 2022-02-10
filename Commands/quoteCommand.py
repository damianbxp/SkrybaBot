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
    else:
        if quote_id > len(quotes):
            return quotes[1]
    return quotes[quote_id]

class QuoteCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Zacytuj wskazany lub losowy cytat")
    async def q(self, ctx, *args):
        if len(args) > 0:
            try:
                quote_id = int(args[0])
            except ValueError:
                print("Wrong type parsed")
                await ctx.send("Musisz podać numer cytatu")
                return
        else:
            quote_id = None

        await ctx.send(get_quote(quote_id)["text"])