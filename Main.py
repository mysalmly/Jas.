import discord
from discord.ext import commands
TOKEN = 'ODkyNzY2NTYzMDUxMTM5MDkz.YVRrpw.9fS3n1wjp2sw5db8aJCoPT0BK1A'
PREFIX = '.'
INTENTS = discord.Intents.default()
bot = commands.Bot(command_prefix=PREFIX, intents=INTENTS)


@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')




bot = commands.Bot(command_prefix=PREFIX, intents=INTENTS)
bot.remove_command("help")


@bot.command()
async def help(ctx):
    em = discord.Embed(Title = "Help", Description = "Use the command for more info")

    em.add_field("Other", value = "`ping`, `bored`, the rest are a SECRET")
    em.add_field("Moderation", value = "`DOESNT EXIST yet..")

    await ctx.send(embed = em)


@bot.command()
async def ping(ctx):
    await ctx.send('pongerino! ')


@bot.command()
async def bored(ctx):
    await ctx.send("go study kiddo")


@bot.command()
async def SuperSecretAdminCMD(ctx):
    await ctx.send("@everyone")



@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    await bot.change_presence(activity=discord.Game(name = "Cyber Jihad! Allahu Akbar! join me! 😼"))


bot.run(TOKEN)