'''
Basic Text Adventure in Python
The library file that contains the various functions.
This file contains the auxillary function that helps the game run.
Macarthur Inbody
AGPLv3 or Later
2019
'''
verbs=['look','grab','move','interact']
def check_input(usr_input,player):
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
	elif verb == 'exit':
			exit()
	else:
		print('not valid')


def check_move(direction):
	global current_room
	if direction not in directions:
		print('You didn\'t enter a valid movement.')
	else:
		dir_id=directions.index(direction)
		if dir_id in valid_moves[current_room]:
			if current_room != 0:
				current_room=0
			else:
				if dir_id == 0:
					current_room=1
				elif dir_id == 1:
					current_room=3
				elif dir_id == 2:
					current_room=4
				elif dir_id == 3:
					current_room=2

def look(obj,player):
#	global player
	current_room=player.location
	if obj is None:
		print(current_room.desc)
	else:
		if current_room.items is None:
			print("There is nothing here except the room.")
		elif obj in current_room.items:
			print(current_room.items[obj].desc)
		elif obj in current_room.mobs:
			print(current_room.mobs[obj].desc)

