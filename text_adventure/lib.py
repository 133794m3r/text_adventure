#!/usr/bin/python3
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
		elif verb == 'help':
			help(obj)
		else:
			pretty_print('Your verb {} is not valid'.format(verb))
	elif verb == 'exit':
		pretty_print("Thank's for playing. I can't wait to see you again.")
		exit(0)
	else:
		pretty_print('No valid input was given.')

def interact(obj,player):
	current_room=player.location
	is_none=False
	exsists=False
	if obj == None:
		pretty_print("You touched the air.\nSurprisingly, nothing happened")
	else:
		if current_room.mobs is None:
			is_none=True
			pass
		elif obj in current_room.mobs:

			if hasattr(current_room.mobs[obj],'interact'):
				current_room.mobs[obj].interact()
				exsists=True
				pass
			else:
				is_none=True
				pass
		if current_room.items is None:
			is_none=True
			pass
		elif obj in current_room.items:
			is_none=False
			exsists=True
			if hasattr(current_room.items[obj],'interact'):
				current_room.items[obj].interact()
				pass
			else:
				pretty_print(current_room.items[obj].interaction)
				pass

	if is_none and not exsists:
		pretty_print("This action was not valid.")


def grab(obj,player):
	current_room=player.location
	nothing_to_see=True
	second_check=False
	nothing_string="You flailed your arms around wildly trying to grab the air. Sadly the air got away."
	if obj == None:
		pass
	else:
			if current_room.items is None:
				nothing_to_see=True
				pass
			elif obj in current_room.items:
				nothing_to_see=False
				second_check=True
				current_room.items[obj].get_item(player)

			if current_room.mobs is None:
				nothing_to_see=True
				pass
			elif obj in current_room.mobs:
				nothing_to_see=False
				second_check=True
				pretty_print(current_room.mobs[obj].grab)

	if nothing_to_see and not second_check:
		pretty_print(nothing_string)

def look(obj,player):
#	global player
	current_room=player.location
	nothing_to_see=True
	second_check=False

	if obj is None:
		current_room.look(player)
		nothing_to_see=False
		second_check=False
	else:
		if obj == 'inventory' or obj == 'i':
			player.inventory.show()
			second_check=True

		if current_room.mobs is None:
			nothing_to_see=True
			pass
		elif obj in current_room.mobs:
			pretty_print(current_room.mobs[obj].desc)
			second_check=True

		if current_room.items is None:
			nothing_to_see=True
			pass
		elif obj in current_room.items:
			pretty_print(current_room.items[obj].desc)
			second_check=True
	if nothing_to_see and not second_check:
		pretty_print("There is nothing to see here")

def help(obj=None):
	if obj is None:
		pretty_print(''' To play the game you need

'''

# TODO: Make sure that this thing doesn't literally run _all_ regexes at one time. In reality
# this should be a single RegEX that replaces based upon the capture groups that are matched.
# but for now this will work. It's highly ineffecient but oh well.
def pretty_format(string):
	#bold underlined and italicized.
	output_string=re.sub(r'\\\[([u|b|i];)(?!\1)([u|b|i];)(?!\2)([u|b|i])\]',r'\033[1;3;4m',string)
	#bold and underlined.
	output_string=re.sub(r'\\\[([u|b];)(?!\1)[u|b]\]',r'\033[1;4m',output_string)
	#underlined and italicized.
	output_string=re.sub(r'\\\[([u|i];)(?!\1)[u|i]\]',r'\033[3;4m',output_string)
	#bold and italized
	output_string=re.sub(r'\\\[([b|i];)(?!\1)[b|i]\]',r'\033[1;3m',output_string)
	#just bold
	output_string=re.sub(r'\\\[b]',r'\033[1m',output_string)
	#just underlined
	output_string=re.sub(r'\\\[u]',r'\033[4m',output_string)
	#just italicized
	output_string=re.sub(r'\\\[i]',r'\033[3m',output_string)
	#clearing all formatting
	output_string=re.sub(r'\\\[o]',r'\033[0m',output_string)
	#Now we will be doing all color modes. They are done seperately from other ones.
	#and you must know the color codes as I'm keeping this super simple for the regex.
	#What I'm doing is very complex and requires a coarse in regex to understand but I'll keep it simple.
	'''
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
	'''
	output_string=re.sub(r"\\\[(?<=\[)(\d.[\d|;]*)(?=\])\]",r"\033[\1m",output_string)
	#output_string=re.sub(r'\\\[n]',r'\n',output_string)
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
	max_width=(1+get_terminal_size()[0])
	string=pretty_format(string)
	string=re.sub(r'\n',r'\\[n\]',string)
	#I format the string to the maximum width I was given so that I can print it properly.
	formatted_string=fill(string,width=max_width)
	formatted_string=re.sub(r'\\\[n\\]',r'\n',string)
	print(formatted_string,end=end)
