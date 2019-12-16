#!/usr/bin/python3
'''
Basic Text Adventure in Python
The Main Game iteself.
This file contains the main game functions.
Macarthur Inbody
AGPLv3 or Later
2019
'''

from templates import *
import sys
from  data import *
from lib import *

#def intialize():
#	module_name=globals()['__name__']
#	module_obj=sys.modules[modname]

#def main():
#	intialize()

#main()
prefix='> '
# room_ids={'starter':0,'north':1,'east':2,'south':3,'west':4}
# valid_moves={0:[0,1,2,3],1:[1],2:[2],3:[0],4:[3]}
# directions=['north','south','west','east']
# verbs=['look','grab','move','interact']
# items={'Mailbox':{'desc':'It is a mailbox with the flag up and the front closed','action':'interact','contains':'letter'},'flashlight':{'desc':'A bright flashlight that\'s still burning.','action':'interact','contains':'batteries'}}
# mobs=['grue','fish']
# item_interactions={'Mailbox':'You opened the mailbox and found a letter.','Flashlight':'You picked up the flashlight and started using it.'}
# mob_interactions={'grue':'You were eaten by a grue','fish':{'The fish is flopping helplessly'}}
# rooms={0:{'items':'Mailbox','mobs':None,'desc':'You are in a room with four exits \033[1m north east south west\033[0m. There is a single mailbox before you.'},1:{'items':None,'mobs':'grue','desc':'dark, and you were eaten by a grue'},2:{'items':'flashlight','mobs':None,'desc':'You are in a room with a single source of light. A \033[1m flashlight.\033[0m'},3:{'item':'Rope','enemy':'fish','desc':'You are in a wet room. There is a fish flopping on the ground before you.'},4:{'items':None,'mobs':None,'desc':'You are in an empty room. You can see nothing else.'}}
# current_room=0
print('Enter your name brave traveller.')
#name=input(prefix)
name='a';
print(f'{name} is in a room.')
print('Your action verbs are \033[1m{}\033[0m'.format(' '.join(verbs)))
print('Your possible movements are \033[1m{}\033[0m'.format(' '.join(directions)))

def interact(obj):
	if obj is None:
		print('You flail your arms about in the air making quite a fool of yourself.')
	else:
		print(items[''])


def main_loop():
	dead=False
	while dead == False:
		usr_input=input(prefix)
		check_input(usr_input,player)
#		dead=True

main_loop()
