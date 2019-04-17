import discord
from discord.ext import commands
import asyncio

class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        '''Testing commands'''
        guild = await self.bot.create_guild(name="Test Guild for Bot")
        id = str(guild.id)
        await ctx.send("Guild ID: " + id)
        asyncio.sleep(10)
        await ctx.send(guild.channels)
        channel = guild.channels[1]
        invite = await channel.create_invite(reason="Invite automaticaly created for the creator of the party")
        await ctx.send(invite.url)

    @commands.command()
    async def get_servers(self, ctx):
        await ctx.send('Servers connected to:')
        for server in self.bot.guilds:
            await ctx.send(server.name + " -- " + str(server.id))

    @commands.command()
    async def get_roles(self, ctx):
        await ctx.send("Roles for this server is:")
        for roles in ctx.guild.roles:
            await ctx.send(roles.name + " -- " + str(roles.id))


def setup(bot):
    bot.add_cog(Utils(bot))