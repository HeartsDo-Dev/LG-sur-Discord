import json
import sys, traceback
import discord
from discord.ext import commands

with open('config.json', 'r') as fichier:
    config = json.load(fichier)

token = config['token']

initial_extensions = ['cogs.help',
                      'cogs.utils',
                      'cogs.servers',
                      'cogs.game',
                      'jishaku']
bot = commands.Bot(command_prefix='+')

@bot.event
async def on_ready():
    print(f'\n\nBot en cours de fonctionnemnt en tant que: {bot.user.name} - {bot.user.id}\nVersion de discord.py: {discord.__version__}\n')
    game = discord.Game(name="Le loup est là ! -- Version DEV")
    await bot.change_presence(activity=game, status=discord.Status.online)
    print(f'Bot ready pour faire des jeux !')

# Here we load our extensions(cogs) listed above in [initial_extensions].
if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

bot.run(token, bot=True, reconnect=True)