import random
import discord
from discord.ext import commands

def run():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():
        print(bot.user)
        print(bot.user.id)

    @bot.command(
        aliases=['p'],
        help="Pomoc",
        description='To jest opis',
        brief='To jest brief',
        enabled=True,
        hidden=True
    )
    async def ping(ctx):
        """ Odpowiada pong"""
        await ctx.send('pong')
    @bot.command()
    async def say(ctx, what = "co ty pierdolisz?"):
        await ctx.send(what)
    @bot.command()
    async def say2(ctx, *what):
        await ctx.send(" ".join(what))
    @bot.command()
    async def dodaj(ctx, jeden:int, dwa:int):
        await ctx.send(jeden+dwa)




    bot.run('MTE3MTc1Nzk2MjY1NDY2MjczOQ.GdXaQi.bU7xAvpxcGRJGma_L88rpB-4G4r-NYOATNKv4M')
if __name__ == "__main__":
    run()
