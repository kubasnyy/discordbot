import random
import discord
from discord.ext import commands

class SimpleView(discord.ui.View):
    @discord.ui.button(label="Twitch: pafk0s",
                       style=discord.ButtonStyle.blurple)
    async def twitch(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("https://www.twitch.tv/pafk0sss")
    @discord.ui.button(label='Youtube: brylush',
                       style=discord.ButtonStyle.red)
    async def yt(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("https://www.youtube.com/channel/UCVxTEiIAZ165mS36CtiWbJg")

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
        help="Odpowiada pong",
        description='To jest opis',
        brief='To jest brief',
        enabled=True,
        hidden=True
    )
    async def ping(ctx):
        """ Odpowiada pong """
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
    @bot.command(
        help="Pokazuje date dołączenia uzytkownika oraz jego ID",
    )
    async def kiedy(ctx, kto:discord.Member):
        joined_date = kto.joined_at.strftime("%Y-%m-%d %H:%M:%S")
        message = f"Użytkownik {kto} dołączył {joined_date}"
        await ctx.send(message)
    @bot.command(
        help="Gra w papier kamien nozyce"
    )
    async def graj(ctx, user_choice: str):
        choices = ['papier', 'kamien', 'nozyce']

        if user_choice.lower() not in choices:
            await ctx.send('Nieprawidłowy wybór. Użyj: kamien, papier lub nozyce.')
            return

        bot_choice = get_winning_choice(user_choice)
        await ctx.send(f'Twój wybór: {user_choice}\nMój wybór: {bot_choice}')

        winner = determine_winner(user_choice, bot_choice)
        await ctx.send(f'Wynik: {winner.capitalize()}')

    def get_winning_choice(user_choice):
        if user_choice == 'kamien':
            return 'papier'
        elif user_choice == 'papier':
            return 'nozyce'
        elif user_choice == 'nozyce':
            return 'kamien'

    def determine_winner(player, opponent):
        if player == opponent:
            return 'remis'
        elif (player == 'kamien' and opponent == 'nozyce') or \
            (player == 'papier' and opponent == 'kamien') or \
            (player == 'nozyce' and opponent == 'papier'):
            return 'xd'
        else:
            return 'Przejebales, ja nigdy nie przegram'
    @bot.command()
    async def linki(ctx):
        view = SimpleView()
        await ctx.send("Wybierz co chcesz:", view=view)



    bot.run('MTE3MTc1Nzk2MjY1NDY2MjczOQ.GdXaQi.bU7xAvpxcGRJGma_L88rpB-4G4r-NYOATNKv4M')
if __name__ == "__main__":
    run()
