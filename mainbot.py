from datetime import datetime as DT
from discord.ext import commands
from dotenv import load_dotenv
# from git import Repo
from variables import module
import discord
import os
import sys


load_dotenv()
bot = commands.Bot(command_prefix=['dev '.casefold()], intents=discord.Intents.all(), help_command=None)
bot.startTime = DT.now()
bot.currentTime = DT.now()
nonmodules = []

@bot.event
async def on_ready():
    print(f"{bot.user} ({bot.user.id}) is online\nTime at start: {bot.currentTime}\nTime to start: " + str((DT.now() - bot.startTime)))
    await bot.change_presence(activity=discord.Game(name="On My Terminal"))
    channel = bot.get_channel(998067191020798042) #bot-online-status(bot testing)
    await channel.send("[LOGGING] Im Alive!")



@bot.command()
async def loggit(ctx, type = None):
    if ctx.author.id != 557286947106586627:
        return
    if type == "pull" or type is None:
        os.chdir(gitdr)
        try:
            repo = Repo('/.git')
            origin = repo.remote('origin')
            origin.pull()
            await ctx.send('git pulled')
            print('git pulled')
        except:
            await ctx.send("an error occured")

@bot.command()
async def logreload(ctx, extension):
    if ctx.author.id == 557286947106586627: 
        await extenstion_reload(ctx, 'modules', extension)
    else:
        await ctx.send("unknown command.")

@bot.command()
async def logload(ctx, extension):
    if ctx.author.id == 557286947106586627: 
        await extenstion_load(ctx, 'modules', extension)
    else:
        await ctx.send("unknown command.")

@bot.command()
async def logunload(ctx, extension):
    if ctx.author.id == 557286947106586627: 
        await extenstion_unload(ctx, 'modules', extension)
    else:
        await ctx.send("unknown command.")


async def extenstion_load(ctx, type, cog):
        if type == 'modules':
            modules = module.main    
        if cog == 'all':
            for cogs in modules:
                try:
                    bot.load_extension(f"{type}.{cogs}")
                except:
                    print(f'{cogs} could not be loaded')
                    nonmodules.append(f'{cogs}')
            if len(nonmodules) != 0:
                noncog = "\n".join([f"{g} was not loaded" for g in nonmodules])
                nonmodules.clear()
            await ctx.send(f"{noncog}\nextensions have been loaded")
        elif cog in modules:
            try:
                bot.load_extension(f"{type}.{cog}")
                await ctx.send(f"{cog} has been loaded")
            except:
                await ctx.send(f'could not load {cog}')
        else:
            await ctx.send("module does not exist")    

async def extenstion_unload(ctx ,type, cog):
        if type == 'modules':
            modules = module.main
        if cog == 'all':
            for cogs in modules:
                try:
                    bot.unload_extension(f"{type}.{cogs}")
                except:
                    print(f'{cogs} could not be unloaded')
                    nonmodules.append(f'{cogs}')
            if len(nonmodules) != 0:
                noncog = "\n".join([f"{g} was not unloaded" for g in nonmodules])
                nonmodules.clear()
            await ctx.send(f"{noncog}\nextensions have been unloaded")
        elif cog in modules:
            try:
                bot.unload_extension(f"{type}.{cog}")
                await ctx.send(f"{cog} has been unloaded")
            except:
                await ctx.send(f'could not unload {cog}')
        else:
            await ctx.send("module does not exist")  

async def extenstion_reload(ctx ,type, cog):
        if type == 'modules':
            modules = module.main  
        if cog == 'all':
            for cogs in modules:
                try:
                    bot.reload_extension(f"{type}.{cogs}")
                except:
                    print(f'{cogs} could not be reloaded')
                    nonmodules.append(f'{cogs}')
            if len(nonmodules) != 0:
                noncog = "\n".join([f"{g} was not reloaded" for g in nonmodules])
                nonmodules.clear()
                await ctx.send(f"{noncog}\nextensions have been reloaded")
        elif cog in modules:
            try:
                bot.reload_extension(f"{type}.{cog}")
                await ctx.send(f"{cog} has been reloaded")
            except:
                await ctx.send(f'could not reload {cog}')
        else:
            await ctx.send("module does not exist")  


for cogs in module.main:
    try:
        bot.load_extension(f"modules.{cogs}")
    except:
        print(f'{cogs} could not be loaded')
        nonmodules.append(f'{cogs}')


bot.run(os.getenv('TOKEN'))