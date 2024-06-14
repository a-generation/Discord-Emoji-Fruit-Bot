import random
import logging
import disnake
from disnake.ext import commands

# Set up intents
intents = disnake.Intents.default()
intents.members = True
intents.message_content = True

# Initialize the bot
bot = commands.Bot(intents=intents)

# Configure logging
logging.basicConfig(level=logging.INFO)

@bot.event
async def on_ready():
    logging.info(f'Logged in as {bot.user.name} - {bot.user.id}')
    print("Bot is ready!")

async def send_fruits(interaction: disnake.ApplicationCommandInteraction, fruit_emoji: str, count: int):
    await interaction.response.send_message(fruit_emoji * count)

@bot.slash_command(name="orange", description="Send an orange emoji")
async def orange(interaction: disnake.ApplicationCommandInteraction, count: int = 1):
    await send_fruits(interaction, "🍊", count)

@bot.slash_command(name="tomato", description="Send a tomato emoji")
async def tomato(interaction: disnake.ApplicationCommandInteraction, count: int = 1):
    await send_fruits(interaction, "🍅", count)

@bot.slash_command(name="apple", description="Send an apple emoji")
async def apple(interaction: disnake.ApplicationCommandInteraction, count: int = 1):
    await send_fruits(interaction, "🍎", count)

@bot.slash_command(name="banana", description="Send a banana emoji")
async def banana(interaction: disnake.ApplicationCommandInteraction, count: int = 1):
    await send_fruits(interaction, "🍌", count)

@bot.slash_command(name="pineapple", description="Send a pineapple emoji")
async def pineapple(interaction: disnake.ApplicationCommandInteraction, count: int = 1):
    await send_fruits(interaction, "🍍", count)

@bot.slash_command(name="lemon", description="Send a lemon emoji")
async def lemon(interaction: disnake.ApplicationCommandInteraction, count: int = 1):
    await send_fruits(interaction, "🍋", count)

@bot.slash_command(name="watermelon", description="Send a watermelon emoji")
async def watermelon(interaction: disnake.ApplicationCommandInteraction, count: int = 1):
    await send_fruits(interaction, "🍉", count)

@bot.slash_command(name="grape", description="Send a grape emoji")
async def grape(interaction: disnake.ApplicationCommandInteraction, count: int = 1):
    await send_fruits(interaction, "🍇", count)

# Run the bot
bot.run("YOUR_BOT_TOKEN_HERE")
