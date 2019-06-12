import discord
from discord.ext import commands
import utils.permissions
import sqlite3

conn = sqlite3.connect('db-template.db')
conn.text_factory = str
cursor = conn.cursor()

class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def init_lobby(self, member:discord.Member=None, guild:discord.Guild=None):
        id = guild.id
        reason = "Création des channels et rôles nécessaire au fonctionnement de la partie"
        cat = await guild.create_category("Loup-Garou", reason=reason)
        channelL = await guild.create_text_channel("lobby", category=cat, reason=reason)
        channelV = await guild.create_text_channel("village", category=cat, reason=reason)
        channelLG = await guild.create_text_channel("loup-garou", category=cat, reason=reason)
        perms = discord.Permissions(0)
        roleMDJ = await guild.create_role(name="MDJ", permissions=perms, hoist=True, mentionable=True, reason=reason)
        roleC = await guild.create_role(name="Créateur de la partie", permissions=perms, reason=reason)
        roleV = await guild.create_role(name="Village", permissions=perms, hoist=True, reason=reason)
        roleM = await guild.create_role(name="Morts", permissions=perms, hoist=True, reason=reason)
        rolesc = [roleC, roleV]
        for role in rolesc:
            await member.add_roles(role, reason="Droit donné au créateur de la partie")
        players = 0 + 1
        cursor.execute("""INSERT INTO parties(id, cat, channelL, channelV, channelLG, roleMDJ, roleC, roleV, roleM) VALUES(?,
         ?, ?, ?, ?, ?, ?, ?, ?)""", (id, cat.id, channelL.id, channelV.id, channelLG.id, roleMDJ.id, roleC.id, roleV.id, roleM.id))
        conn.commit()
        await channelL.send("Channel prêt et opérationnel !")
        embed = discord.Embed(title="Rappel: Vous êtes sur une partie spécial !", color=0xfaa01b)
        embed.set_author(name="Bienvenue sur la partie", icon_url="https://i.imgur.com/UIkoEL4.png")
        embed.add_field(name="C'est quoi ce type de partie ?",
                        value="Ce type de partie est lancée par les créateurs de parties et les amis, ça peut être une animation ou une partie normale selon le créateur de partie ou MDJ.",
                        inline=True)
        embed.add_field(name="Il faut respecter quel règles dans cette espace ?",
                        value="Les règles de partie normale, pas de dévoilement et ne pas être AFK !", inline=True)
        embed.add_field(name="Peut t'il avoir des cadeaux en gagnant ces types de partie ?",
                        value="Cela dépend encore une fois de qui anime, à voir avec le créateur de la partie.",
                        inline=True)
        embed.set_footer(text="Créateur de la partie: " + member.name)
        return await channelL.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def create(self, ctx):
        member = ctx.author
        guild = member.guild
        gid = guild.id
        uid = member.id
        cursor.execute("""SELECT owner FROM servers WHERE id = ?""", (gid,))
        fetch = [r[0] for r in cursor.fetchall()]
        try:
            owid = fetch[0]
        except IndexError:
            owid = None
        if uid == owid:
            await self.init_lobby(member, guild)
        elif owid == None:
            await ctx.send("Actuellement, les parties sur les serveurs personnels sont désactivés !\n"
                           "Motif: Merci de patienter jusqu'a la Beta pour cette fonctionalité !")
        else:
            await ctx.send("Partie impossible à lancer !!!\n"
                           "Motif: Ce serveur n'a pas été crée par cette utilisateur !")


    @commands.command()
    @commands.guild_only()
    async def profil(self, ctx, profile: discord.Member = None):
        if profile == None:
            profile = ctx.author
        embed = discord.Embed(title="Profile de" + profile.name + ":")
        embed.set_thumbnail(url=profile.avatar_url)
        embed.add_field(name="Parties jouées :", value="WIP", inline=False)
        embed.add_field(name="Parties gagnés :", value="WIP", inline=False)
        perms = utils.permissions.permissions_check_global(ctx=ctx, member=profile)
        perms = max(perms)
        if perms >= 3:
            embed.add_field(name="Membre du staff :", value="Oui", inline=True)
            namep = utils.permissions.get_roles_with_level_global(ctx=ctx, level=perms)
            namep = namep.name
            embed.add_field(name="Rôle dans le staff :", value=namep, inline=True)
        else:
            embed.add_field(name="Membre du staff", value="Non", inline=True)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Game(bot))