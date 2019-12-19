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
			if current_room.mobs is None:
				pass
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


def pretty_print(string,end='\n'):
	#For some reason we cannot use the real width length. So I am adding up to 5 for the length.
	#this module will get the me the terminal size and I only need the width as that's all that matters.
	max_width=get_terminal_size()[0]
	#I format the string to the maximum width I was given so that I can print it properly.
	formatted_string=fill(string,width=max_width,break_long_words=False)
	print(formatted_string,end=end)
