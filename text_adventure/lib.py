'''
Basic Text Adventure in Python
The library file that contains the various functions.
This file contains the auxillary function that helps the game run.
Macarthur Inbody
AGPLv3 or Later
2019
'''
from data import *
from textwrap import fill
from terminal_size import get_terminal_size
import re

def check_input(usr_input,player):
	verbs=['look','grab','move','interact']
	inputs=usr_input.split(' ')
	verb=inputs[0]
	current_room=player.location
	if len(inputs) >= 2:
		obj=inputs[1]
	else:
		obj=None

	if verb in verbs:
		if verb == 'move':
			player.move(obj,current_room)
		elif verb == 'look':
			look(obj,player)
		elif verb == 'grab':
			grab(obj,player)
		elif verb == 'interact':
			interact(obj,player)
		else:
			pretty_print('Your verb {} is not valid'.format(verb))
	elif verb == 'exit':
		pretty_print("Thank's for playing. I can't wait to see you again.")
		exit(0)
	else:
		pretty_print('No valid input was given.')

def interact(obj,player):
	current_room=player.location
	is_none=True
	if obj == None:
		is_none=False
		pretty_print("You touched the air.\nSurprisingly, nothing happened")
	else:
		if current_room.mobs is None:
			pass
		elif obj in current_room.mobs:
			is_none=False
			if hasattr(current_room.mobs[obj],'interact'):
				current_room.mobs[obj].interact()
				pass
			else:
				pass
		if current_room.items is None:
			pass
		elif obj in current_room.items:
			is_none=False
			if hasattr(current_room.items[obj],'interact'):
				current_room.items[obj].interact()
				pass
			else:
				pretty_print(current_room.items[obj].interaction)
				pass
	if is_none:
		pretty_print("This action was not valid.")


def grab(obj,player):
	current_room=player.location
	nothing_to_see=True
	nothing_str="You flailed your arms around wildly trying to grab the air. Sadly the air got away."
	if obj == None:
		pretty_print("You flailed your arms around wildly trying to grab the air. Sadly the air got away.")
	else:
			if current_room.items is None:
				pass
			elif obj in current_room.items:
				current_room.items[obj].get_item(player)
				nothing_to_see=False
			if current_room.mobs is None:
				pass
				nothing_to_see=False
			elif obj in current_room.mobs:
				pretty_print(current_room.mobs[obj].grab)
	if nothing_to_see:
		pretty_print(nothing_str)


def look(obj,player):
#	global player
	current_room=player.location
	nothing_to_see=True
	if obj is None:
		pretty_print(current_room.desc)
		nothing_to_see=False
	else:
		if obj == 'inventory' or obj == 'i':
			player.inventory.show()
			nothing_to_see=False
		if current_room.mobs is None:
			pass
		elif obj in current_room.mobs:
			nothing_to_see=False
			pretty_print(current_room.mobs[obj].desc)

		if current_room.items is None:
			pass
		elif obj in current_room.items:
			pretty_print(current_room.items[obj].desc)
			nothing_to_see=False

	if nothing_to_see:
		pretty_print("There is nothing to see here")


# TODO: Make sure that this thing doesn't literally run _all_ regexes at one time. In reality
# this should be a single RegEX that replaces based upon the capture groups that are matched.
# but for now this will work. It's highly ineffecient but oh well.
def pretty_format(string):
	output_string=re.sub(r'\\\[([u|b|i];)(?!\1)([u|b|i];)(?!\2)([u|b|i])\]',r'\033[1;3;4m',string)
	output_string=re.sub(r'\\\[([u|b];)(?!\1)[u|b]\]',r'\033[1;4m',output_string)
	output_string=re.sub(r'\\\[([u|i];)(?!\1)[u|i]\]',r'\033[3;4m',output_string)
	output_string=re.sub(r'\\\[([b|i];)(?!\1)[b|i]\]',r'\033[1;3m',output_string)
	output_string=re.sub(r'\\\[b]',r'\033[1m',output_string)
	output_string=re.sub(r'\\\[u]',r'\033[4m',output_string)
	output_string=re.sub(r'\\\[i]',r'\033[3m',output_string)
	output_string=re.sub(r'\\\[o]',r'\033[0m',output_string)

	return output_string;


# This will format the output and also add coloring. Plus it'll give shorthands for various control characters.
# There will be another function that replaces the "control" characters with the actual escape codes.
# \[b] = Bold. \[u]=Underline. \[i]=Italic. \[o]=Clear formatting.
# Combining them is done similarly. \{b;u}=bold and underlined.
# All of these codes will be replaced via the actual control codes.
# Bold = \033[1m
# Underline = \033[2m
# TODO: Actually do this as right now formatter is using nonprintable characters in it's calculations.
def pretty_print(string,end='\n'):
	#this will soon do a custom formatting system.
	#to keep the number of extra characters to a minimum. It will use escape characters.
	#the format will be \b=\033[1m \o=\033[0m. \u=\033[2m etc. The basic formatting will be using
	#these commands to make format work better.
	#For some reason we cannot use the real width length. So I am adding up to 5 for the length.
	#this module will get the me the terminal size and I only need the width as that's all that matters.
	max_width=get_terminal_size()[0]
	string=pretty_format(string)
	#I format the string to the maximum width I was given so that I can print it properly.
	formatted_string=fill(string,width=max_width,break_long_words=False)
	print(formatted_string,end=end)
