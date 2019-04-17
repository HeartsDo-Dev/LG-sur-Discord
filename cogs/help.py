import discord
from discord.ext import commands
import asyncio


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        await ctx.send("Oui, il n'y a rien ici :(")


def setup(bot):
    bot.remove_command("help")
    bot.add_cog(Help(bot))