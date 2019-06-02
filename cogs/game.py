import discord
from discord.ext import commands
import utils.permissions

class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def init_lobby(self, guild:discord.Guild=None):
        print("Not Done :c")

    @commands.command()
    @commands.guild_only()
    async def create(self, ctx):
        print("TODO")

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
            namep = await utils.permissions.get_roles_with_level_global(self=self, level=perms)
            namep = namep.name
            embed.add_field(name="Rôle dans le staff :", value=namep, inline=True)
        else:
            embed.add_field(name="Membre du staff", value="Non", inline=True)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Game(bot))