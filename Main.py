# Main.py
import os
import sys

import discord
from dotenv import load_dotenv

import Debug

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
    Debug.Log('We have logged in as {0.user}'.format())


try:
    client.run(TOKEN)
except discord.ClientException as e:
    Debug.LogError('A critical error occurred')
    Debug.LogError(str(e))
    sys.exit(1)

Debug.Log('Client Started')
