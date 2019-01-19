import discord

TOKEN_FILE = "data/discord_bot_token.txt"

client = discord.Client()

@client.event
async def on_message(message):
	"""Check for commands after each new message."""

	# Skips messages sent by Cumberlan
	if message.author == client.user:
		return

@client.event
async def on_ready():
	print("Logged in as")
	print(client.user.name)
	print(client.user.id)
	print('------')

def load_token():
	"""Loads the Discord API authentication token."""
	with open(TOKEN_FILE, "r") as token_file:
		return token_file.read().strip()

# Initializing the bot
client.run(load_token())
