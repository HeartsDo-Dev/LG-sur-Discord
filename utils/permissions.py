import discord
from discord.ext import commands
from discord.utils import get

def permissions_check_local(member: discord.Member=None): # Verification des roles sur le serveur locale pour les
        # permissions locale
        #
        #Les différents niveau de permissions pour les commandes locales sont :
        # Niveau 0 : @everyone
        # Niveau 1 : Morts
        # Niveau 2 : Village
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
        lv2 = "Village"
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

def permissions_check_global(ctx, member: discord.Member=None): # Verification des roles du serveurs officiel pour les
        # permissons globale
        #
        #
        # Les différents niveau de permissions pour les commandes globales sont :
        # Niveau 0 : @everyone
        # Niveau 1 : Donateur
        # Niveau 2 : Amis
        # Niveau 3 : Créateurs de parties (si activé)
        # Niveau 4 : Modérateurs globaux
        # Niveau 5 : Développeurs
        # Niveau 6 : Administrateurs
        if not member:
            print("Euh, WHAT (Permissions global: pas de membre dans la variable")
            return Exception
        roles = []
        perms = []
        guild = ctx.bot.get_guild(566691210996088862)
        member = guild.get_member(member.id)
        for list in member.roles:
            roles.append(list.id)
        lv6 = 581901261251543057
        lv5 = 567022994828951552
        lv4 = 567023187192315904
        lv3 = 567023810025357312
        lv2 = 568134025278128160
        lv1 = 579036755156533291
        perms.append(0)
        if lv1 in roles:
            perms.append(1)
        if lv2 in roles:
            perms.append(2)
        if lv3 in roles:
            perms.append(3)
        if lv4 in roles:
            perms.append(4)
        if lv5 in roles:
            perms.append(5)
        if lv6 in roles:
            perms.append(6)
        return perms

def get_roles_with_level_global(ctx, level):
    # Récupérer le discord.Role via un level de permissions globale
    lv6 = 581901261251543057
    lv5 = 567022994828951552
    lv4 = 567023187192315904
    lv3 = 567023810025357312
    lv2 = 568134025278128160
    lv1 = 579036755156533291
    guild = ctx.bot.get_guild(566691210996088862)
    if level == 1:
        return guild.get_role(lv1)
    elif level == 2:
        return guild.get_role(lv2)
    elif level == 3:
        return guild.get_role(lv3)
    elif level == 4:
        return guild.get_role(lv4)
    elif level == 5:
        return guild.get_role(lv5)
    elif level == 6:
        return guild.get_role(lv6)
    else:
        return None