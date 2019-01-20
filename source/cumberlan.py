import discord
import random

TOKEN_FILE = "data/discord_bot_token.txt"

cumberlan = discord.Client()

@cumberlan.event
async def on_message(message):
	"""Check for commands after each new message."""

	# Skips messages sent by Cumberlan
	if message.author == cumberlan.user:
		return

	if message.content.startswith("->hello"):
		msg = "Hello {0.author.mention}".format(message)
		await cumberlan.send_message(message.channel, msg)

	if message.content.startswith("->compliment"):
		possible_responses = [
			"Lookin' good today!",
			"You light up the room!",
			"You have a great sense of humor!",
			"You are enough!",
			"You should be proud of yourself!",
			"You bring out the best in other people!",
			"You are making a difference.",
			"You're all that and a super-size bag of chips!",
			"When you think you're done, try again.",
			"You look awesome!",
			"Seize the day, and then take the night, while you're at it!",
			"You're the coolest person reading this message!",
			"You've earned a day of relaxation!",
			"You're the brightest star in my sky!",
			"When you're confident enough to do anything, you'll succeed!",
			"I think you're pretty neat-o!",
			"You light up every room you walk into!",
			"Have a great day, you amazing human being!",
			"Your friends and family love you to bits; don't forget that!",
			"If no one else's, you're my sunshine!",
			"You have a great smile; show it more often!",
			"I like your sense of fashion.",
			"Your eyes shimmer like sunshine off waves!",
			"You remind me of a soft pillow; I could never not love you!",
			"You are loved!",
			"You are wanted!",
			"Make today awesome!",
			"You just made my day; now go make someone else's!",
			"Here's to you, kid",
			"I like that attitude"
		]

		await cumberlan.send_message(message.channel, random.choice(possible_responses))

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

# Initializing the bot
cumberlan.run(load_token())
