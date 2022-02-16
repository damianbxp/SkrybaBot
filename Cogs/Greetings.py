from discord.ext import commands


def setup(bot):
    bot.add_cog(Greetings(bot))


class Greetings(commands.Cog):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f"{member.mention} przybywa na zamek")
