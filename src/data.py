#!/usr/bin/python
"""
Basic Text Adventure in Python
Data File
This file contains all of the items in the game world and it's intialization.
Macarthur Inbody
AGPLv3 or Later
2019
"""

from templates import *


letter=Item()
letter.desc="It's a letter you found in the mailbox."
letter.name="letter"
letter.interaction="The letters have faded but you can make out a single sentence \[b;i;u]'Those in the dark, are always fearful of the light.'\[o]"
letter.locaton=None

mailbox=Mailbox()
mailbox.desc='It is a mailbox with the flag up and the lid is closed.'
mailbox.contains=letter
mailbox.name="mailbox"
mailbox.interaction="You open the mailbox."

starter=Room("You are in the middle of a field.",{'mailbox':mailbox})

mailbox.location=starter
#here are the basic rooms.
north=Room("You are in a room with a single source of light. There is one exit to the \[b]south\[o]. Also, there is a single \[b]flashlight on the ground.\[o]")
west=Room("You are in a wet room. There is a \[b]fish\[o] flopping on the ground before you.")
east=Room("You are room.")
south=DarkRoom("You are in a dark room. There is nothing that can be seen.","You are in a dark room. There is a terrifying beast before you a \[b]Grue\[o]")
endgame=FinalRoom("You are in the room that appeared after the \[b]Grue\[o] was defeated. Your \[b]flashlight\[o] is burning bright at an intensity unseen before. The room is filled with a blinding light. You cannot see anything. If only there was some way to \[b]turn off\[o] that light source.", "You are in the final room. With the \[b]flashlight\[o] turned off, the room is visible. You can finally see what the room contains.")
#this is an example of something that won't be shown until some condition is done.
south.add_hidden_exits({'s':endgame})
flashlight=Lantern()
flashlight.desc="A bright flashlight that's still burning bright."
flashlight.grab_desc="You picked up the flashlight."
flashlight.interaction="You opened the flashlight and see it still contains batteries."
flashlight.light=True
flashlight.location=north
flashlight.name='flashlight'
north.add_items(flashlight)
#Here is a normal initialization fo the macguffin. This is the final item that upon getting it, it'll end the game for them.
#it's what causes the game to end.
macguffin=MacGuffin(name='macguffin',desc="The amazing and wonderful \[b]macguffin\[o]. It is the greatest \[b]treasure\[o] you've ever seen. You must have it.",interaction="You touch it and it doesn't move.",location=endgame)
endgame.macguffin=macguffin
unobtanium=Treasure(name='unobtanium',desc='The rarest mineral in the whole universe. You have only heard of it in legends prior.',interaction="As you run your fingers acorss it's surface, you can feel a strange energy flowing up your finger-tips.",location=east,removeable=True,score=500)
treasure_chest=Container(name='treasure chest',desc="A treasure chest that's seen better days. The latch where the old lock used to be still shines.",contains=unobtanium,location=east,removeable=False)
east.add_items(treasure_chest)
print(east.items['treasure chest'])
#here you can see me making the fish mobb.
fish=Mob("It's a giant fish.","It's scales are slippery",name="fish")
fish.grab_desc="It slips easily through your fingers, and slaps you in the face with it's fin."
fish.name='fish'
fish.location=west

grue=Grue()
south.add_mobs(grue)
west.add_mobs(fish)

#here you can see me adding exits to the game  world. Don't overwrite any of these exits.
starter.exits={'n':north,'e':east,'s':south,'w':west}
#you can instead make it so that your room passes into this one. But make sure that you still link to it. An example of this
#will be provided in a future version.

#for now just place your room somewhere along here.
west.exits={'e':starter}
east.exits={'w':starter}
#just don't make yours have an exit to the south of this room as it'll be overwritten by the endgame room.
south.exits={'n':starter}
north.exits={'s':starter}

#this is the primary player object. Don't edit this.
player=Player()
player.transport(starter)
player.inventory=Inventory()
player.alight = True