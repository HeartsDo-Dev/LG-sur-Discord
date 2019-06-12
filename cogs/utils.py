import discord
from discord.ext import commands
import asyncio
import psutil
import utils.permissions

class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def reload_team_channel(self, ctx):
        channel = 587551314599346176
        guild = ctx.guild
        channel = guild.get_channel(channel)
        limit = 4
        before = ctx.message
        try:
            await channel.purge(limit=limit, before=before)
        except:
            print("OK, peut-être qu'il a un probléme !")
        embed = discord.Embed(title="Les administrateur s'occupe de tout le serveur officiel et du bot, il gère le "
                              "staff et leurs travails",
                              color=0xfc0133)
        embed.set_author(name="Administrateurs",
                         icon_url="https://pierre.chachatelier.fr/jeux-societe/images/loups-garous-loup-large.jpg")
        role = utils.permissions.get_roles_with_level_global(ctx=ctx, level=6)
        members = str()
        for member in role.members:
            if member.bot == True:
                members = members + member.name + "#" + member.discriminator + " *Cette utilisateur est un bot !*" + "\n"
            else:
                members = members + member.name + "#" + member.discriminator + "\n"
        if members == "":
            members = "*Il n'y a aucun membre dans cette équipe !*"
        embed.add_field(name="Liste des membres actuellements dans cette équipe:", value=members, inline=True)
        await channel.send(embed=embed)
        embed = discord.Embed(title="Les dévelopeurs gère la partie technique, ils crées de nouvealle cartes, commandes"
                                    " et fonctionalités pour les joueurs",
                              color=0xfc0133)
        embed.set_author(name="Dévelopeurs",
                         icon_url="https://pierre.chachatelier.fr/jeux-societe/images/loups-garous-loup-large.jpg")
        role = utils.permissions.get_roles_with_level_global(ctx=ctx, level=5)
        members = str()
        for member in role.members:
            if member.bot == True:
                members = members + member.name + "#" + member.discriminator + "*Cette utilisateur est un bot !*" + "\n"
            else:
                members = members + member.name + "#" + member.discriminator + "\n"
        if members == "":
            members = "*Il n'y a aucun membre dans cette équipe !*"
        embed.add_field(name="Liste des membres actuellements dans cette équipe:", value=members, inline=True)
        await channel.send(embed=embed)
        embed = discord.Embed(title="Les modérateurs globaux gère les cas globaux (bannisements globale et reports), "
                                    "il sont également modérateur du serveur offciel",
                              color=0xfc0133)
        embed.set_author(name="Modérateurs Globaux",
                         icon_url="https://pierre.chachatelier.fr/jeux-societe/images/loups-garous-loup-large.jpg")
        role = utils.permissions.get_roles_with_level_global(ctx=ctx, level=4)
        members = str()
        for member in role.members:
            if member.bot == True:
                members = members + member.name + "#" + member.discriminator + "*Cette utilisateur est un bot !*" + "\n"
            else:
                members = members + member.name + "#" + member.discriminator + "\n"
        if members == "":
            members = "*Il n'y a aucun membre dans cette équipe !*"
        embed.add_field(name="Liste des membres actuellements dans cette équipe:", value=members, inline=True)
        await channel.send(embed=embed)
        embed = discord.Embed(title="Les créteurs de partie crée des partie évenementiel pour amuser les joueurs avec"
                                    "de nouveau concept",
                              color=0xfc0133)
        embed.set_author(name="Créateurs de partie",
                         icon_url="https://pierre.chachatelier.fr/jeux-societe/images/loups-garous-loup-large.jpg")
        role = utils.permissions.get_roles_with_level_global(ctx=ctx, level=3)
        members = str()
        for member in role.members:
            if member.bot == True:
                members = members + member.name + "#" + member.discriminator + "*Cette utilisateur est un bot !*" + "\n"
            else:
                members = members + member.name + "#" + member.discriminator + "\n"
        if members == "":
            members = "*Il n'y a aucun membre dans cette équipe !*"
        embed.add_field(name="Liste des membres actuellements dans cette équipe:", value=members, inline=True)
        await channel.send(embed=embed)



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

    @commands.command()
    @commands.guild_only()
    @commands.is_owner()
    async def print_team_channel(self, ctx):
        await ctx.send("OK, je force l'actualisation de la page de l'équipe !")
        await self.reload_team_channel(ctx)



def setup(bot):
    bot.add_cog(Utils(bot))