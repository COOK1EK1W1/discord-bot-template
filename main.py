"""basic discord bot"""

from discord.ext import commands
import discord

from cog_example import ExampleCog

TOKEN = ""

bot = commands.Bot(command_prefix=["."])

@bot.event
async def on_ready():
    """when logged in"""
    print(f'We have logged in as {bot.user}')
    await bot.change_presence(status=discord.Status.online)

bot.add_cog(ExampleCog(bot))
bot.run(TOKEN)
