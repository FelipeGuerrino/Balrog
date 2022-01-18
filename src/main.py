import os, json, discord
from discord.ext import commands
from server import keep_alive
from dotenv import load_dotenv

load_dotenv() #Se for utilizado um arquivo .env

if os.path.exists(os.getcwd() + "/config.json"): #Se for utilizado um arquivo JSON

    with open('./config.json') as f:
        configData = json.load(f)
else:
    configTemplate = {"Owner": "", "Prefix": ""}

    with open(os.getcwd() + "./config.json", "w+") as f:
        json.dump(configTemplate, f)

owner=configData["Owner"]
prefix=configData["Prefix"] #JSON
#usando a config

bot = commands.Bot(command_prefix=prefix)

def is_owner():
    """Checa se quem usou o comando é o dono do bot |
       Checks if the command user is the bot owner
    """
    async def predicate(ctx):
        return ctx.author.id == owner
    return commands.check(predicate)


@bot.event
async def on_ready():
    print('Bot ready!')

@bot.command()
@is_owner()
async def on(ctx):
    await bot.change_presence(status=discord.Status.online)

@bot.command()
@is_owner()
async def idle(ctx):
    await bot.change_presence(status=discord.Status.idle)
#Comandos para mudar presença (e.g. Online)

@bot.command()
@is_owner()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    print(f'Cog {extension} loaded.')

@bot.command()
@is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    print(f'Cog {extension} unloaded.')

@bot.command()
@is_owner()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    print(f'Cog {extension} reloaded succesfully.')
#load/reload/unload


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
#Carrega todas as 'cogs' do bot na inicialização

keep_alive() #Server
bot.run(os.getenv('TOKEN')) #.env