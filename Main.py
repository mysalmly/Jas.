import discord
from discord.ext import commands
import os
TOKEN = 'TOKEN GOES HERE'
PREFIX = '.'
INTENTS = discord.Intents.default()
bot = commands.Bot(command_prefix=PREFIX, intents=INTENTS)
import meme
import funsies

bot.load_extensions("meme", "funsies")
@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')




bot = commands.Bot(command_prefix=PREFIX, intents=INTENTS)
bot.remove_command("help")






@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    await bot.change_presence(activity=discord.Watching(name = "Put a name here and the bot status should say 'watching xyz' "))


bot.run(TOKEN)
