import discord
from discord.ext import commands
import os

from help_cog import help_cog
from music_cog import music_cog
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'siema {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

@client.event
async def on_ready():
    print(f'Zalogowano jako {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!siema'):
        await message.channel.send('siemano')
    if message.content.startswith('!ile razy sie rozjebales'):
        await message.channel.send('69')

client.run('MTE3MTc1Nzk2MjY1NDY2MjczOQ.GdXaQi.bU7xAvpxcGRJGma_L88rpB-4G4r-NYOATNKv4M')
