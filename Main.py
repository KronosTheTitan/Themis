# Main.py
import os

import discord
from dotenv import load_dotenv

import Debug

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
    Debug.Log('We have logged in as {0.user}'.format())


client.run(TOKEN)
