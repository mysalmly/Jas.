import discord
from discord.ext import commands


class funsies(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
@commands.Cog.listener
@commands.has_role("Soj")
async def SuperSecretAdminCMD(ctx):
    await ctx.send("@everyone")

@commands.Cog.listener()
async def ping(ctx):
    await ctx.send('await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")')


@commands.Cog.listener()
async def bored(ctx):
    await ctx.send("go study kiddo")




def setup(bot:commands.Bot):
    bot.add_cog(funsies(bot))