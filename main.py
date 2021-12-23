import discord
import os
import logging
from discord.ext import commands

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
token = os.environ.get("token")
bot = commands.Bot(command_prefix="$")
@bot.event
async def on_ready():
    print("The bot is ready!")


@bot.command()
async def ping(ctx):
	await ctx.channel.send("pong")

bot.run(token)