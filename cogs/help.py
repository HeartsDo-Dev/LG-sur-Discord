import discord
from discord.ext import commands
import asyncio
import utils.permissions


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



def setup(bot):
    # bot.remove_command("help")
    bot.add_cog(Help(bot))