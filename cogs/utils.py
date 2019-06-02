import discord
from discord.ext import commands
import asyncio
import psutil
import utils.permissions

class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @commands.is_owner()
    async def get_servers(self, ctx):
        await ctx.send('Serveurs connecté au bot :')
        for server in self.bot.guilds:
            await ctx.send(server.name + " -- " + str(server.id))

    @commands.command()
    @commands.guild_only()
    @commands.is_owner()
    async def get_roles(self, ctx):
        await ctx.send("Les rôles de ce serveur sont :")
        for roles in ctx.guild.roles:
            await ctx.send(roles.name + " -- " + str(roles.id))

    @commands.command()
    @commands.guild_only()
    async def info(self, ctx):
        embed = discord.Embed(title="Un bot développé principalement par HeartsDo#0530 et par les membres de Developy",
                              color=0xfc0133)
        embed.set_author(name="LG Sur Discord",
                         icon_url="https://pierre.chachatelier.fr/jeux-societe/images/loups-garous-loup-large.jpg")
        embed.add_field(name="Version du bot :", value="DEV", inline=True)
        embed.add_field(name="Version de Discord.py :", value=discord.__version__, inline=True)
        embed.add_field(name="Serveurs :", value=len(self.bot.guilds), inline=True)
        embed.add_field(name="Utilisation du CPU :", value=str(psutil.cpu_percent()) + "%", inline=True)
        embed.add_field(name="RAM utilisé :", value=str(psutil.virtual_memory()[2]) + "%", inline=True)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def get_perms(self, ctx, user:discord.Member):
        if not user:
            await ctx.send("J'ai besoin d'un utilisateur pour fonctionner !")
            return
        permsg = utils.permissions.permissions_check_global(ctx=ctx, member=user)
        permsl = utils.permissions.permissions_check_local(member=user)
        await ctx.send("Permissions de l'utilisateur " + user.mention + ": \n"
                       "Global: " + str(permsg) + "\n"
                        "Local: " + str(permsl))





def setup(bot):
    bot.add_cog(Utils(bot))