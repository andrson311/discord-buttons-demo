import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

class CustomView(discord.ui.View):
    
    @discord.ui.button(label='blurple', style=discord.ButtonStyle.blurple)
    async def blurple(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('You just click on blurple button.')
    
    @discord.ui.button(label='gray', style=discord.ButtonStyle.gray)
    async def gray(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('You just click on gray button.')
    
    @discord.ui.button(label='grey', style=discord.ButtonStyle.grey)
    async def grey(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('You just click on grey button.')
    
    @discord.ui.button(label='green', style=discord.ButtonStyle.green)
    async def green(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('You just click on green button.')
    
    @discord.ui.button(label='red', style=discord.ButtonStyle.red)
    async def red(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('You just click on red button.')
    
    @discord.ui.button(label='primary', style=discord.ButtonStyle.primary)
    async def primary(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('You just click on primary button.')
    
    @discord.ui.button(label='secondary', style=discord.ButtonStyle.secondary)
    async def secondary(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('You just click on secondary button.')
    
    @discord.ui.button(label='success', style=discord.ButtonStyle.success)
    async def success(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('You just click on success button.')
    
    @discord.ui.button(label='danger', style=discord.ButtonStyle.danger)
    async def danger(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('You just click on danger button.')

def run():

    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(
        command_prefix=commands.when_mentioned_or('!'),
        description='Buttons demo',
        intents=intents
    )

    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user} (ID: {bot.user.id})')
        print('------')
        await bot.tree.sync()

    @bot.hybrid_command(name='buttons')
    async def buttons(ctx):
        view = CustomView()
        message = await ctx.send(view=view)
        view.message = message
        await view.wait()

    bot.run(DISCORD_TOKEN)

if __name__ == "__main__":
    run()
