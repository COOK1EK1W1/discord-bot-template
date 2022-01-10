"""cog for bot (section for commands)"""
import discord
from discord.ext import commands

class ExampleCog(commands.Cog, name='Example'):
    """template cog"""

    @commands.command()
    async def lol(self, ctx, *_):
        """template command"""
        await ctx.send("lol")
