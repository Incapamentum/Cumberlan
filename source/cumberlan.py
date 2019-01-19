import discord

TOKEN_fo = open("data/discord_bot_token.txt", "r")
TOKEN = TOKEN_fo.read()

client = discord.Client()

@client.event
async def on_message(message):
	# Bot ain't gonna reply to itself here
	if message.author == client.user:
		return

	if message.content.startswith("!hello"):
		msg = "Hello {0.author.mention}".format(message)
		await client.send_message(message.channel, msg)

@client.event
async def on_ready():
	print("Logged in as")
	print(client.user.name)
	print(client.user.id)
	print('------')

client.run(TOKEN)
