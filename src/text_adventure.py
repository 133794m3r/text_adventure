#!/usr/bin/python3
'''
Basic Text Adventure in Python
The Main Game iteself.
This file contains the main game functions.
Macarthur Inbody
AGPLv3 or Later
2019
'''

try:
	lib
except NameError:
	import lib

#from templates import *
import sys
from  data import *


#def intialize():
#	module_name=globals()['__name__']
#	module_obj=sys.modules[modname]

#def main():
#	intialize()
verbs=['look','grab','move','interact','help']

prefix='> '

directions=['north','south','west','east']
print('Enter your name brave traveller.')
name=input(prefix)
#name='a';
lib.pretty_print("Welcome to the world of \[b;i]Adventure\[o].\nBut before we begin first a brief tutorial on how this world works. In this world you will be tasked discovering it's secrets. The parser is your interface to this game world. It will accept commands in the following input.\n \[b]{VERB} {OBJECT}\[o]. An example is given below. To move north you'd type into the prompt denoted by \[b]>\[o] \n> move north\nIt also supports shorthand for movements so move n also works. Your verbs are given at the start. Anything you can interact with via a verb will be \[b]bolded\[o].\nYou also have an inventory you can utilize. It is accessed via \[b]look inventory\[o].\n")

lib.pretty_print(f'\[b]{name}\[o] finds themself in the middle of a field.')
lib.pretty_print('Your action verbs are \[b]{}\[o]'.format(' '.join(verbs)))
lib.pretty_print('Your possible movements are \[b]{}\[o]'.format(' '.join(directions)))


def main_loop():
	dead=False
	while dead == False:
		usr_input=input(prefix)
		lib.check_input(usr_input,player)
#		dead=True
	dead=player.dead

main_loop()
