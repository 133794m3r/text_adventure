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
letter.interact="The letters have faded but you can make out a single sentence 'Those in the dark fear the light.'"
mailbox=Mailbox()
mailbox.desc='It is a mailbox with the flag up and the front closed'
mailbox.action='interact'
mailbox.contains=letter
starter=Room("You are in a room with four exits \033[1m north east south west\033[0m. There is a single mailbox before you.",mailbox)
letter.location=starter._id
mailbox.in_room=0
north=Room("You are in a room with a single source of light. A \033[1m flashlight.\033[0m")
west=Room("You are in a wet room. There is a \033[1mfish\033[0m flopping on the ground before you.")
east=Room("You are in an empty room. You can see nothing else")
south=Room("You are in a dark room. There is nothing that can be seen.")
starter.add_moves({'n':north,'e':east,'s':south,'w':west})
print(starter.exits)
print(north)
print(west)
print(south)
print(east)
print(starter)
current_room=starter
west.add_moves({'e':starter})
east.add_moves({'w':starter})
south.add_moves({'n':starter})
north.add_moves({'s':starter})
player=Player()
player.transport(starter)
inventory=Inventory()


