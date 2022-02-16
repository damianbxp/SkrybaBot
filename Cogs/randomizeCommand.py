from discord.ext import commands
from random import randrange


def setup(bot):
    bot.add_cog(RandomCommands(bot))


class RandomCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Losuje wartość w podamym zakresie")
    async def random(self, ctx, min_number, max_number):
        try:
            await ctx.send(randrange(int(min_number), int(max_number) + 1))
        except ValueError:
            await ctx.send("Nie mogę tego zrobić")

    @commands.command(brief="Rzuca kością")
    async def dice(self, ctx):
        await ctx.send(randrange(1, 7))

    @commands.command(brief="Wybierz jedną z podanych opcji")
    async def pick_one(self, ctx, *args):
        n = randrange(0, len(args))
        await ctx.send(args[n])

    @commands.command(brief="Rzuca monetą")
    async def coin_flip(self, ctx):
        n = randrange(0, 2)
        await ctx.send("Orzeł" if n == 0 else "Reszka")
