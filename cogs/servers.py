import discord
from discord.ext import commands
import json
import utils.permissions
import asyncio

class Servers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def create_server(self, ctx):
        with open('config.json', 'r') as file:
            config = json.load(file)
        if ctx.guild.id != config['meta']:
            await ctx.send("Cette commande ne peut que être executé sur le serveur officiel !")
            return
        perms = utils.permissions.permissions_check_global(ctx, ctx.author)
        perms_pass = False
        if 2 in perms:
            perms_pass = True
        if 3 in perms:
            perms_pass = True
        if perms_pass == True:
            await ctx.send("Bienvenue sur le créateur de serveur pour jouer à LG de Thiercelieux\n"
                           "Pour commencer, donner le nom de votre serveur : ")
            def check(m):
                return m.author == ctx.author and m.channel == m.channel
            name = await self.bot.wait_for('message', check=check)
            name = name.content
            await ctx.send("Merci, votre serveur est en cours de création.")
            guild = await self.bot.create_guild(name=name)
            await asyncio.sleep(3)
            guild = self.bot.get_guild(guild.id)
            channel = guild.channels[1]
            idg = str(guild.id)
            invite = await channel.create_invite(
                reason="Invitation crée pour permettre au créateur de la partie de rejoindre")
            await ctx.send("Votre serveur est prêt !\n"
                           "ID du serveur : " + idg + "\n"
                           "Votre invitation au serveur : " + invite.url)
        else:
            await ctx.send("Vous n'avez pas la permission d'executer cette commande !")


def setup(bot):
    bot.add_cog(Servers(bot))