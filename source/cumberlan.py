import discord

TOKEN = "NTM2MDY0NzAxOTkwMzA1ODAz.DyRRzw.UGku35w5arZUIxOYISU7o4IqqqI"

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
