import discord
from discord.ext import commands

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['clr'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx):
        await ctx.channel.purge()


def setup(bot):
    bot.add_cog(Mod(bot))