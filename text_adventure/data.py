'''
Basic Text Adventure in Python
Data File
This file contains all of the items in the game world and it's intialization.
Macarthur Inbody
AGPLv3 or Later
2019
'''

from templates import *

letter=Item()
letter.desc="It's a letter you found in the mailbox."
letter.name="letter"
letter.interaction="The letters have faded but you can make out a single sentence \{b;i;u}'Those in the dark, are always fearul of the light.'\[o]"
mailbox=Mailbox()
mailbox.desc='It is a mailbox with the flag up and the front is closed.'
mailbox.contains=letter
mailbox.name="mailbox"
mailbox.interaction="You open the mailbox and see it contains a \[b]letter\[o]"
starter=Room("You are in a room with four exits \[b] north east south west\[o]. There is a single \[b]mailbox\[o] before you.",{'mailbox':mailbox})
#letter.location=starter._id
letter.locaton=None
mailbox.location=starter
north=Room("You are in a room with a single source of light. There is one exit to the \[b]south\[o]. A \[b] flashlight.\[o]")
west=Room("You are in a wet room. There is a single exit to the \[b]east\[o]. There is a \[b]fish\[o] flopping on the ground before you.")
east=Room("You are in an empty room. There is a single exit to the \[b]west\[o]. You can see nothing else")
south=Room("You are in a dark room.There is a single exit to the \[b]north\[o]. There is nothing that can be seen.")
flashlight=Item()
flashlight.desc="A bright flashlight that's still burning bright."
flashlight.grab_desc="You picked up the flashlight."
flashlight.interaction="You opened the flashlight and see it still contains batteries."
fish=Mob("It's a giant fish.","It's scales are slippery",name="fish")
fish.grab="It slips easily through your fingers, and slaps you in the face with it's fin."
fish.name='fish'
flashlight.location=north
flashlight.name='flashlight'
north.add_item(flashlight)
fish.location=west

west.add_mobs(fish)
starter.add_moves({'n':north,'e':east,'s':south,'w':west})
west.add_moves({'e':starter})
east.add_moves({'w':starter})
south.add_moves({'n':starter})
north.add_moves({'s':starter})
player=Player()
player.transport(starter)
player.inventory=Inventory()
