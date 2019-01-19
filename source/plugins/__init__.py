""""An initializer for all of the included plugins.

It imports all of the installed plugins and associates their command strings
with their command functions.

"""

from plugins import (
	help_menu
	# compliments
)

COMMANDS = {
	# include a list of commands here. Syntax as follows:
	# plugin.COMMAND : plugin.command_plugin
	# compliments.COMMAND : compliments.command_compliments
	help_menu.COMMAND : help_menu.command_help_menu
}

INLINES = {
	# Idk if this is supposed to be blank or not. Keeping it here as a just-in-case.
}
