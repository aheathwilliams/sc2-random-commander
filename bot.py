# bot.py
import os
import random
import discord
import commanders

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

cs = commanders.build_commander_list()


@bot.command(name='random', help='Should return a random commander to use in Starcraft 2 co-op')
async def random_commander(ctx):
    c = commanders.choose_commander(cs)

    embed = discord.Embed(title=c["name"], colour=discord.Colour(
        0x33cbff), url="https://starcraft2coop.com/commanders/" + c["urlPath"], description=c["description"])
    if "image" in c:
        embed.set_image(url=c["image"])
    if "builds" in c:
        for build in c["builds"]:
            embed.add_field(name=build["name"], value=build["value"], inline="false")
    embed.add_field(name="Build Order:", value="```" + c["buildOrder"] + "```")
    await ctx.send(content="GL HF!", embed=embed)

bot.run(TOKEN)
