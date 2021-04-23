import discord
from discord.ext import commands
import os
from keep_alive import keep_alive

client = discord.Client()

client = commands.Bot(command_prefix = '!') 


@client.event
async def on_ready():
    print("bot online")

@client.event
async def on_message(message):
  if message.author != client.user:
    if message.channel.id == 833814170121142302 or message.channel.id == 833814188002508800:
        await message.add_reaction("\U00002b06")
        await message.add_reaction("\U00002b07")
    

keep_alive()
client.run(os.getenv("TOKEN")) 