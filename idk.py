import discord
from discord.ext import commands


class funsies(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
@commands.Cog.listener
@commands.has_role("# USER MUST HAVE WHATEVER ROLE YOU PUT HERE")
async def SuperSecretAdminCMD(ctx):
    await ctx.send("@everyone")

@commands.Cog.listener()
async def ping(ctx):
    await ctx.send('await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")')



def setup(bot:commands.Bot):
    bot.add_cog(funsies(bot))
