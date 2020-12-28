#!/usr/bin/python3
"""
Basic Text Adventure in Python
The library file that contains the various functions.
This file contains the auxillary function that helps the game run.
Macarthur Inbody
AGPLv3 or Later
2019
"""
# try:
#	data_defined
# except NameError:
#	from data import *

from textwrap import fill
import re

def init_terminal():
	import platform
	current_os = platform.system()
	if current_os == 'Windows':
		import ctypes
		kernel32 = ctypes.windll.kernel32
		kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)


def get_terminal_size():
	from os import get_terminal_size,environ
	if environ.get('DEBUG')=='1':
		return 80,24
	else:
		return get_terminal_size()


def debug(obj,player):
	current_room=player.location
	if obj is None:
		print(current_room)
	elif current_room.items is not None and obj in current_room.items:
		print(current_room.items[obj])
	elif current_room.mobs is not None and obj in current_room.mobs:
		print(current_room.mobs[obj])
	elif current_room.exits is not None and obj in current_room.exits:
		print(current_room.exits[obj])
	elif obj in player.inventory.items:
		print(player.inventory.items[obj])
	elif obj in ('Player','player'):
		print(player)
	else:
		print(f"Your object {obj} wasn't found.")

def use(obj,player):
	current_room=player.location
	if current_room.items is not None and obj in current_room.items:
		if hasattr(current_room.items[obj],'use'):
			current_room.items[obj].use(player)
		else:
			pretty_print(f"You can't use {obj}")
	elif obj in player.inventory.items:
		if hasattr(player.inventory.items[obj],'use'):
			player.inventory.items[obj].use(player)
		else:
			pretty_print(f"You can't use {obj}")
	else:
		pretty_print(f"You can't use {obj}")

def check_input(usr_input: str, player: object):
	"""
	Check input function. It will parse the user's input and perform the corresponding action so long as it was valid.
	Args:
		usr_input: The string that was passed to us from the main function.
		player: The global player object.
	"""
	verbs = ['look', 'grab', 'move', 'interact', 'help']
	inputs = usr_input.split(' ')
	movements = ["north","south","east","west","n","s","e","w"]
	verb = inputs[0]
	current_room = player.location

	if len(inputs) >= 2:
		obj = ' '.join(inputs[1:])
	else:
		obj = None

	if verb == 'move' and obj in movements:
		player.move(obj)
	elif verb in movements:
		player.move(verb)
	elif verb in ('look','l'):
		look(obj, player)
	elif verb in ('grab','g'):
		grab(obj, player)
	elif verb in ('interact','i'):
		interact(obj, player)
	elif verb in ('inventory','inv'):
		player.inventory.show()
	elif verb in ('help','h'):
		help(verbs, obj)
	elif verb in ('use','u'):
		use(obj,player)
	elif verb  == 'exit':
		pretty_print("Thank's for playing. I can't wait to see you again.")
		exit(0)
	elif verb in ('wait','w'):
		if hasattr(current_room,'wait'):
			current_room.wait(player)
		else:
			pretty_print('No valid input was given.')
	elif verb in ('debug','d'):
			debug(obj,player)
	else:
		pretty_print(f"The verb \[b]{verb}\[o] was no valid or the target of that verb was not valid.")


def interact(obj, player):
	"""

	Args:
		obj:
		player:
	"""
	current_room = player.location
	is_none = False
	exsists = False
	if obj is None:
		pretty_print("You touched the air.\nSurprisingly, nothing happened")
	elif current_room.mobs is not None and obj in current_room.mobs:
			current_room.mobs[obj].interact(player)
			pass
	elif current_room.items is not None and obj in current_room.items:
		if hasattr(current_room.items[obj], 'interact'):
			current_room.items[obj].interact()
		else:
			pretty_print(current_room.items[obj].interaction)
	elif obj in player.inventory.items:
		if hasattr(player.inventory.items[obj], 'interact'):
			player.inventory.items[obj].interact()
		else:
			pretty_print(player.inventory.items[obj].interaction)
	else:
		pretty_print("There was nothing to touch, so you touched the air. Surprisingly nothing happened.")


def grab(obj, player):
	current_room = player.location
	nothing_to_see = True
	second_check = False
	nothing_string = "You flailed your arms around wildly trying to grab the air. Sadly the air got away."
	if obj is None:
		pretty_print(nothing_string)
	else:
		if current_room.items is not None and obj in current_room.items:
			current_room.items[obj].get_item(player)
		elif current_room.mobs is not None and obj in current_room.mobs:
			current_room.mobs[obj].grab()
		else:
			pretty_print(nothing_string)


def look(obj, player):
	"""

	Args:
		obj:
		player:
	"""
	current_room = player.location

	if obj is None:
		current_room.look(player)
	else:
		if obj == 'inventory' or obj == 'i':
			player.inventory.show()
		elif obj in player.inventory.items:
			pretty_print(player.inventory.items[obj].desc)
			second_check = True
		else:
			current_room.look_obj(obj)


def help(verbs, obj=None):
	if obj is None:
		pretty_print("""Welcome to the game. In this game you interact with the game w1orld through a simple parser.
Anything you can interact with is going to be bolded. In addition to this formatting will tell you what it is.
You give it commands in the following format. \[b][VERB] [OBJECT]\[o].1
Where object is what you're interacting with and verb is one of these verbs \[b]"{}"\[o]. If you want help with a specific verb then run this command again like so.
help [VERB].
It will tell you more about the verb and how it is used.
Mobs in the game world are \[u]underlined\[o] in addition to being \[b]bolded\[u].
""".format(' '.join(verbs)))
	else:
		# TODO: Actually write some helpful information for each of the verbs but oh well it works for now.
		if obj == 'help':
			pretty_print("""This command will give you help about the different verbs that you can utilize. The format is \[b]help verb\[o]. Then what you will have to do is select which verb you want to know more about to have the help information printed.
""")
		elif obj == 'look':
			pretty_print("""This command has an optional argument \[b]{OBJECT}\[o]. The "object" is what you want to look at. If you omit it, you will simply look at the room. Anything that you can look at will be bolded. This tells you that it is something important in the flavor text. So for example if you were in a room and you get the following shown as the description of the room. \n"You are in a dark dank room. You see a large \[b]rock\[o] that's emitting a strange light."\nThis means that if you wanted to look at this rock you'd type "look rock" and it'd give you it's description.
				""")
		elif obj == 'grab':
			pass
		elif obj == 'interact':
			pass
		elif obj == 'move':
			pass


# TODO: Make sure that this thing doesn't literally run _all_ regexes at one time. In reality
# this should be a single RegEX that replaces based upon the capture groups that are matched.
# but for now this will work. It's highly ineffecient but oh well.
def pretty_format(string):
	# bold underlined and italicized.
	output_string = re.sub(r'\\\[([u|b|i];)(?!\1)([u|b|i];)(?!\2)([u|b|i])\]', r'\033[1;3;4m', string)
	# bold and underlined.
	output_string = re.sub(r'\\\[([u|b];)(?!\1)[u|b]\]', r'\033[1;4m', output_string)
	# underlined and italicized.
	output_string = re.sub(r'\\\[([u|i];)(?!\1)[u|i]\]', r'\033[3;4m', output_string)
	# bold and italized
	output_string = re.sub(r'\\\[([b|i];)(?!\1)[b|i]\]', r'\033[1;3m', output_string)
	# just bold
	output_string = re.sub(r'\\\[b]', r'\033[1m', output_string)
	# just underlined
	output_string = re.sub(r'\\\[u]', r'\033[4m', output_string)
	# just italicized
	output_string = re.sub(r'\\\[i]', r'\033[3m', output_string)
	# clearing all formatting
	output_string = re.sub(r'\\\[o]', r'\033[0m', output_string)
	# Now we will be doing all color modes. They are done seperately from other ones.
	# and you must know the color codes as I'm keeping this super simple for the regex.
	# What I'm doing is very complex and requires a coarse in regex to understand but I'll keep it simple.
	"""
	First off you need to know how python/regex works. First we're going to look for the following string.
	PLACEHOLDER is representing some string of characters.
	1)\[PLACEHOLDER]
	2)Then we're going to do a positive lookbehind. Making sure the following regex matches.
		a) We're going to go forward one character and then amke sure that it is what we're expecting.
		b) [ and only one time.
	3) Then we're going to make sure that there's a capture group that starts with a number.
		a) And contains only numbers or the character ;.
	4)Next we're going to make a postive lookahead. to make sure that the character ] is matched.
	5) Then we make sure that the character is there.
	6) We then replace the string using the capture group that was everything in the string and we ignore all of the characters not inside of the [].
	7) We place them after the magic token \033[ then put the capture group there followed by 'm'.
	8) We make this replacement go throughout the whole string till the end.
	9) We return the string.
	"""
	output_string = re.sub(r"\\\[(?<=\[)(\d.[\d|;]*)(?=\])\]", r"\033[\1m", output_string)
	return output_string


# This will format the output and also add coloring. Plus it'll give shorthands for various control characters.
# There will be another function that replaces the "control" characters with the actual escape codes.
# \[b] = Bold. \[u]=Underline. \[i]=Italic. \[o]=Clear formatting.
# Combining them is done similarly. \{b;u}=bold and underlined.
# All of these codes will be replaced via the actual control codes.
# Bold = \033[1m
# Underline = \033[2m
# TODO: Actually do this as right now formatter is using nonprintable characters in it's calculations.
def pretty_print(string, end='\n'):
	# this will soon do a custom formatting system.
	# to keep the number of extra characters to a minimum. It will use escape characters.
	# the format will be \b=\033[1m \o=\033[0m. \u=\033[2m etc. The basic formatting will be using
	# these commands to make format work better.
	# For some reason we cannot use the real width length. So I am adding up to 5 for the length.
	# this module will get the me the terminal size and I only need the width as that's all that matters.
	max_width = (1 + get_terminal_size()[0])
	string = pretty_format(string)
	string = re.sub(r'\n', r'\\[n\]', string)
	# I format the string to the maximum width I was given so that I can print it properly.
	formatted_string = fill(string, width=max_width)
	formatted_string = re.sub(r'\\\[n\\]', r'\n', string)
	print(formatted_string, end=end)


def fight():
	pass
