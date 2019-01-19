"""Displays a succinct help menu that lists all of the commands available
	to the user

"""

import discord

COMMAND = "help"

async def command_help_menu(client, message):

	response = "Here's a list of the commands I can do!"

	embedded_message = discord.Embed(color = 0xffee05)
	embedded_message.add_field(
		name = "->compliment",
		value = "Gives a nice little pick-me-up!",
		inline = False
	)

	await message.channel.send(response, embed = embedded_message)
