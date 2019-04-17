import discord
from discord.ext import commands
from discord.utils import get

class Permissions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def permissions_check_global(self, member: discord.Member): # Un outils pour voir votre niveau de permissions :)
        # Les différents niveau de permissions pour les commandes globales sont :
        # Niveau 0 : @everyone
        # Niveau 1 : Créateurs de parties (si activé)
        # Niveau 2 : Modérateurs globaux
        # Niveau 3 : Développeurs
        # Niveau 4 : Propriétaire du bot
        self.bot.get_guild(566691210996088862)
        if :
            perms.append(4)
        else:
            return 0 # Niveau 0 = @everyone

def setup(bot):
    bot.add_cog(Permissions(bot))