import re
import sys
import signal
import discord
from plugins import COMMANDS, INLINES

TOKEN_FILE = "data/discord_bot_token.txt"
COMMAND_PATTERN = r"^?(?P<command>[a-zA-z]+)"

cumberlan = discord.Client()

@cumberlan.event
async def on_message(message):
	"""Check for commands after each new message."""

	# Skips messages sent by Cumberlan
	if message.author == cumberlan.user:
		return

	# Check message for inline commands.
	for inline in INLINES.keys():
		if re.search(inline, message.content):
			await INLINES[inline](cumberlan, messages)

			return

	command_match = re.match(COMMAND_PATTERN, message.content)
	if command_match is not None:
		command = command_match.group("command")

		# If the command is supported, execute its function. Else call
		# the "help" function
		if command in COMMANDS.keys():
			await COMMANDS[command](cumberlan, message)
		else:
			await COMMANDS["help"](cumberlan, message)

@cumberlan.event
async def on_ready():
	print("Logged in as")
	print(cumberlan.user.name)
	print(cumberlan.user.id)
	print('------')

def load_token():
	"""Loads the Discord API authentication token."""
	with open(TOKEN_FILE, "r") as token_file:
		return token_file.read().strip()

def handle_signals(signal_number, stack_frame):
	"""Gracefully shut down Cumberlan."""
	cumberlan.close()
	sys.exit(0)

# Initializing the bot
signal.signal(signal.SIGINT, handle_signals)
signal.signal(signal.SIGTERM, handle_signals)
cumberlan.run(load_token())
