import discord
from discord.ext import commands
from discord.utils import get

def permissions_check_local(member: discord.Member): # Verification des roles sur le serveur locale pour les
        # permissions locale
        #
        #Les différents niveau de permissions pour les commandes locales sont :
        # Niveau 0 : @everyone
        # Niveau 1 : Morts
        # Niveau 2 : Joueurs
        # Niveau 3 : Créateur de la partie
        # Niveau 4 : MDJ
        if not member:
            print("Euh, WHAT (Permissions local: pas de membre dans la variable")
            return Exception
        roles = []
        perms = []
        for list in member.roles:
            roles.append(list.name)
        lv4 = "MDJ"
        lv3 = "Créateur de la partie"
        lv2 = "Joueurs"
        lv1 = "Morts"
        perms.append(0)
        if lv1 in roles:
            perms.append(1)
        elif lv2 in roles:
            perms.append(2)
        elif lv3 in roles:
            perms.append(3)
        elif lv4 in roles:
            perms.append(4)
        return perms

def permissions_check_global(ctx, member: discord.Member): # Verification des roles du serveurs officiel pour les
        # permissons globale
        #
        #
        # Les différents niveau de permissions pour les commandes globales sont :
        # Niveau 0 : @everyone
        # Niveau 1 : Créateurs de parties (si activé)
        # Niveau 2 : Modérateurs globaux
        # Niveau 3 : Développeurs
        # Niveau 4 : Propriétaire du bot
        if not member:
            print("Euh, WHAT (Permissions global: pas de membre dans la variable")
            return Exception
        roles = []
        perms = []
        guild = ctx.bot.get_guild(566691210996088862)
        member = guild.get_member(member.id)
        for list in member.roles:
            roles.append(list.id)
        lv4 = 567023052437848064
        lv3 = 567022994828951552
        lv2 = 567023187192315904
        lv1 = 567023810025357312
        perms.append(0)
        if lv1 in roles:
            perms.append(1)
        if lv2 in roles:
            perms.append(2)
        if lv3 in roles:
            perms.append(3)
        if lv4 in roles:
            perms.append(4)
        return perms

