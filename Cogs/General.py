from discord.ext import commands


def setup(bot):
    bot.add_cog(General(bot))


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, ex):
        print(ex)
        await ctx.send("No nie poszło")
