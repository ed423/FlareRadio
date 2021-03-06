from secrets import token_hex
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import radio
import image_from_text

load_dotenv()

token = os.environ.get('token')

bot = commands.Bot(command_prefix='//')
radio.setup(bot)
image_from_text.setup(bot)

@bot.event
async def on_ready():
    print('Bot successfully connected')

@bot.command()
async def hello(ctx):
    await ctx.send("hello!")

bot.run(token)






