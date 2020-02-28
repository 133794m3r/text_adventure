#!/usr/bin/python
'''
Basic Text Adventure in Python
Data File
This file contains all of the items in the game world and it's intialization.
Macarthur Inbody
AGPLv3 or Later
2019
'''

data_defined=True
#try:
#	Item()
#except:
from templates import *


letter=Item()
letter.desc="It's a letter you found in the mailbox."
letter.name="letter"
letter.interaction="The letters have faded but you can make out a single sentence \[b;i;u]'Those in the dark, are always fearul of the light.'\[o]"
mailbox=Mailbox()
mailbox.desc='It is a mailbox with the flag up and the lid is closed.'
mailbox.contains=letter
mailbox.name="mailbox"
mailbox.interaction="You open the mailbox."
starter=Room("You are in the middle of a field.",{'mailbox':mailbox})
#letter.location=starter._id
letter.locaton=None
mailbox.location=starter
north=Room("You are in a room with a single source of light. There is one exit to the \[b]south\[o]. Also, there is a single \[b]flashlight on the ground.\[o]")
west=Room("You are in a wet room. There is a \[b]fish\[o] flopping on the ground before you.")
east=Room("You are in an empty room. You can see nothing else.")
south=Dark_room("You are in a dark room. There is nothing that can be seen.","You are in a dark room. There is a terrifying beast before you a \[b]Grue\[o]")
flashlight=Item()
flashlight.desc="A bright flashlight that's still burning bright."
flashlight.grab_desc="You picked up the flashlight."
flashlight.interaction="You opened the flashlight and see it still contains batteries."
flashlight.light=True
fish=Mob("It's a giant fish.","It's scales are slippery",name="fish")
fish.grab_desc="It slips easily through your fingers, and slaps you in the face with it's fin."
fish.name='fish'
flashlight.location=north
flashlight.name='flashlight'
north.add_items(flashlight)
fish.location=west
grue=Grue()
south.add_hidden_mobs(grue)
west.add_mobs(fish)
starter.add_moves({'n':north,'e':east,'s':south,'w':west})
west.add_moves({'e':starter})
east.add_moves({'w':starter})
south.add_moves({'n':starter})
north.add_moves({'s':starter})
player=Player()
player.transport(starter)
player.inventory=Inventory()
player.alight=True
