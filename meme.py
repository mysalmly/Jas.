import discord
from discord.ext import commands
import aiohttp
import random
PREFIX = '.'
INTENTS = discord.Intents.default()
bot = commands.Bot(command_prefix=PREFIX, intents=INTENTS)

class Meme(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.Cog.listener()
    async def meme(ctx):
        async with aiohttp.ClientSesssion() as cs:
            async with cs.get("https://www.reddit.com/r/islamichistorymeme.json") as r:
                memes = await r.json()
                embed = discord.Embed(
                    color = discord.Color.gray()
                )
                embed.set_image(url=memes["data"]["children"][random.randit(0, 100)]["data"]["url"])
                embed.set_footer(text=f"Powered by r/islamichistorymeme | meme requested by {ctx.author}")
                await ctx.send(embed=embed)













                def setup(bot:commands.Bot):
                    bot.add_cog(Meme(bot))