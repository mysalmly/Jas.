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
    em = discord.Embed(Title = "Help", Description = "Use the actual goddamned command for more info")

    em.add_field("Fun", value = "`bored`, `ping`, `kill`, `Saj`, `Soj`, `Jos`, `Kai`, `Forgor`, `nicokawai` ")
    em.add_field("Moderation", value = "`DOESNT EXIST yet..")

    await ctx.send(embed = em)


@bot.command()
async def ping(ctx):
    await ctx.send('pongerino! ')


@bot.command()
async def bored(ctx):
    await ctx.send('You are bored? ah well sucky life too bad for you ig saj was bored while writing this too lol i think ill regret putting this here too bad x2 ok wow im so bored i dont think this cmd will even work OR will the bot even get added to IHM like fr WHY am i doing this i also have homework to do right now a sci worksheet ,math and a social project i still need ideas for it too f')


@bot.command()
async def everyone(ctx):
    await ctx.send("@everyone 😳 ")


@bot.command()
async def kill(ctx):
    await ctx.send("R.I.P janazah time bois n gurls")


@bot.command()
async def soj(ctx):
    await ctx.send("**Where is Saj?**  Saj is busy :( i miss my master")


@bot.command()
async def kai(ctx):
    await ctx.send("**Who is kai?**  *mental health.exe has stopped working*")


@bot.command()
async def saj(ctx):
    await ctx.send("**Who is Saj?**  My master ofc! 😄")


@bot.command()
async def jos(ctx):
    await ctx.send("**Who is Jos?**  ALL HAIL GRANDMASTER")


@bot.command()
async def forgor(ctx):
    await ctx.send("**Who is literally everyone else?**  Ask **Them** lols")


@bot.command()
async def nicokawai(ctx):
    await ctx.send(' ima break your nico nico kneecaps stay halal bois ')


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    await bot.change_presence(activity=discord.Game(name = "Cyber Jihad! Allahu Akbar! join me! 😼"))


bot.run(TOKEN)