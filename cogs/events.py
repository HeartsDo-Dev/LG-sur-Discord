import discord
from discord.ext import commands
import sqlite3

conn = sqlite3.connect('db-template.db')
conn.text_factory = str
cursor = conn.cursor()



class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
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
            channel = guild.system_channel
            perm = discord.Permissions(permissions=8)
            color = discord.Color(value=2554848)
            role = await guild.create_role(name="Administrateur", permissions=perm, color=color, hoist=True)
            await member.add_roles(role)
            await channel.send("Bienvenue sur le serveur, vos droit Admnistrateur vous à été donné ! \n"
                               "Pour lancer votre partie, exectuter la commande +create")
        else:
            return


def setup(bot):
    bot.add_cog(Events(bot))