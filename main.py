import os
import secrets

import discord
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TOKEN")
if not token:
    raise RuntimeError("TOKEN is missing from .env")


class MyBot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()


bot = MyBot()


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.tree.command(name="ping", description="Check if the bot is online")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")


bot.run(token)