import discord

intents = discord.Intents.default()
intents.messages = True  # Ustawienie intencji na odczyt wiadomości

# Tworzenie klienta bota z intencjami
client = discord.Client(intents=intents)

# Event wywoływany podczas uruchomienia bota
@client.event
async def on_ready():
    print(f'Zalogowano jako {client.user}')

# Event obsługujący przychodzące wiadomości
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!witaj'):
        await message.channel.send('Witaj!')

# Uruchomienie bota
client.run('MTE3MTc1Nzk2MjY1NDY2MjczOQ.GdXaQi.bU7xAvpxcGRJGma_L88rpB-4G4r-NYOATNKv4M')
