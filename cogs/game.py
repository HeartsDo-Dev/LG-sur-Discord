import discord
from discord.ext import commands

class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def init_lobby(self, guild:discord.Guild=None):


    @commands.command()
    @commands.guild_only()
    async def create(self, ctx):
        # TODO: Create the command


def setup(bot):
    bot.add_cog(Game(bot))