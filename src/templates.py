'''
Basic Text Adventure in Python
Class Library File
This file contains all of the classes that are used in the game.
Macarthur Inbody
AGPLv3 or Later
2019
'''
try:
	lib
except NameError:
	import lib

class Buff:
	name="Nothing"
	desc="Nothing at all"
	modifier=None
	def __init__(self,name=name,desc=desc,modifier=modifier):
		self.name=name
		self.desc=desc
		self.modifer=modifier

# change the location to be player instead of
# a room id for where the item is. The location will
# be a signed int. If the item is gone it becomes None meaning
# that it's gone.
# if it's -1 then it has moved to the player's inventory
# because that is the "room" or structure id of their inventory.
class Item:
	_id=0
	name="Item"
	#the item's description
	desc=''
	interaction=''
	#the item's current location
	location=None
	#the initialization method for the object when it's first created.
	def __init__(self,desc=desc,interact=interaction,location=location):
		#self is python's version of this.
		self.desc=desc
		self.interaction=interact
		self.location=location
		#if you have a _ before a property name it means it's meant to be private.
		# but if you do __ then it's truly private because it can only be acessed through name mangling.
		self._id=Item._id
		#increment the item's id
		Item._id+=1
	#this method takes the item from the game world into the user's inventory.
	def get_item(self,player):

		#we call the move location method and tell it to put it into the player's inventory so that it's
		#no longer in the game world.
		if self.location != -1:
			self.move_location(-1)
			player.inventory.add(self)
			lib.pretty_print("You have grabbed \[b]{}\[o] and put it into your \[b]inventory.\[o]".format(self.name))
			if hasattr(self,'light'):
				player.alight=True
			player.location.remove_item(self)
		elif self.location is None:
			lib.pretty_print("This item doesn't exist")
		elif self.location == -1:
			lib.pretty_print("The item is in your inventory already.")
		else:
			lib.pretty_print("There is no item.")

	def look(self):
		lib.pretty_print(self.desc)

	def move_location(self,location):
		self.location=location

class Container(Item):
	contains=None
	is_open=False
	def __init__(self,contains=contains):
		Item.__init__(self)
		self.contains=contains
		self.interaction=interaction

	def interact(self):
		if self.contains != None:
			item_name=self.contains.name
			item_contained=self.contains


		if self.is_open:
			self.location.remove_item(self.contains)

			if item_contained.location == -1:
				self.contains=None
			else:
				item_contained.location=None

			self.location.remove_items(self.contains)
			interaction="You closed the \[b]{}\[o]".format(self.name)
			lib.pretty_print(interaction)

		else:
			interaction="You opened the \[b]{}\[o] and you see it contains \[b]{}\[o]".format(self.name,item_name)
			lib.pretty_print(interaction)
			if self.contains != None:
				self.location.add_item(self.contains)
				item_contained.location=self.location

		self.is_open = not self.is_open

		return 0
'''
The weapon class is a child class of the Item class. It extends Item with it's own
attributes that aren't part of the default item class itself.
In python when you are doing a sub class of a main class you create it like so.
class sub_class(main_class):
instead of the normal attributes.
'''

class Weapon(Item):
	damage=0
	desc='It is a weapon'
	def __init__(self,damage=damage,desc=desc):
		self.damage=damage
		self.desc=desc


class World():
	rooms={}
	def __init__(self):
		pass
	def add_room(self,room):
		self.rooms[(room.x,room.y)]=room

class Mailbox(Item):
	contains='letter'
	is_open=False
	def __init__(self,contains=contains):
		Item.__init__(self)
		self.contains=contains

	def interact(self):
		string_to_print=self.interaction
		if self.contains != None:
			item_name=self.contains.name
			item_contained=self.contains
			string_to_print=string_to_print[:-1]+' and it contains \[b]'+item_name+'\[o].'

		if self.is_open:
			self.location.remove_item(self.contains)
			if item_contained.location == -1:
				self.contains=None
			else:
				item_contained.location=None
			lib.pretty_print(string_to_print.replace('open','close')[:21],end=".\n")
		else:
			lib.pretty_print(string_to_print)
			if self.contains != None:
				self.location.add_items(self.contains)
				item_contained.location=self.location

		self.is_open = not self.is_open

	def look(self):
		string_to_print=self.desc
		if self.is_open:
			string_to_print=string_to_print.replace('closed','opened')
			if self.contains != None:
				string_to_print+=' You can also see that it contains \[b]'+item_name+'\[o].'

		lib.pretty_print(string_to_print)

	def get_item(self,player=None):
		print(player is None)
		if player is None:
			if self.is_open:
				lib.pretty_print("You pick up the {} and start to read it.\n{}".format(self.contains.name,self.contains.desc))
		else:
			lib.pretty_print("The mailbox is firmly attached to it's post.")


class Player:
	x=0
	y=0
	location={}
	weapon=None
	dead=False
	hp=10
	inventory=None
	alight=False

	def __init__(self):
		self.x=0
		self.y=0
		self.weapon=None
		self.dead=False
		self.location={}
		self.hp=10
		self.alight=False

	def add_status(self,buffed):
		self.status.update({buffed.name,buffed.turns})

	def remove_status(self,buffed):
		self.status.pop(buffed)

	def transport(self,room):
		self.location=room

	def move(self,movement,current_room):
		exits=current_room.exits
#		selected_move = ( movement or movement[0:1] in self.location.exits.get(movement,None))
		if movement is None:
			lib.pretty_print("None given.")
		elif movement in exits:
			selected_move=exits.get(movement,None)
		elif movement[0:1] in exits:
			selected_move=exits.get(movement[0:1],None)
		else:
			selected_move=False

		if selected_move:
			selected_move.look(self)
			self.location=selected_move
		else:
			lib.pretty_print("The move you entered is invalid");
			return None

	def damaged(amount):
		self.hp=self.hp-amount


class Inventory:
	items={}
	def __init__(self,items=items):
		self.items=items

	def add(self,item):
		self.items.update({item.name:item})

	def show(self):
		tmp_str='Your inventory contains:'
		for item in self.items:
			tmp_str+=f'a \[b]{item}\[o] '
			lib.pretty_print(tmp_str)

	def use(self,item):

		if item in items:
			lib.pretty_print(item.interaction)
		else:
			lib.pretty_print("You don't have that item")

	def remove(self,item):
		self.items.pop(item.name,None)

class Room:
	desc="You're in a room"
	items=None
	mobs=None
	x=0
	y=0
	_id=0
	exits={}

	def __init__(self,desc=desc,items=items,mobs=mobs,x=x,y=y,exits=exits):
		self.exits=exits
		self.desc=desc
		self.items=items
		self.mobs=mobs
		self.x=x
		self.y=y
		self._id=Room._id
		Room._id+=1

	def add_items(self,items):
		if self.items is None:
			self.items={}
		items_type = type(items).__name__
		if items_type == 'list':
			for item in items:
				self.items[tem.name]=item
		elif items_type == 'dict':
			for item_name,item in items.items():
				self.items[item_name]=item
		else:
			self.items[items.name]=items

	def print_exits(self):
		exits=' '.join(self.exits.keys())
		exits=exits.replace('n','north')
		exits=exits.replace('s','south')
		exits=exits.replace('e','east')
		exits=exits.replace('w','west')
		string=""
		if len(exits) == 4:
			string="There is a single exit to the \[b]{}\[o].".format(exits)
		else:
			string="There are exits to the \[b]{}\[o].".format(exits)
		lib.pretty_print(string)

	def print_items(self):
		if self.items is None:
			return 1
		items=self.items.keys()
		total_items=len(items)
		items=[ 'a \[b]{}\[o]'.format(item) for item in items ]

		if total_items == 0:
			pass
		elif total_items == 1:
			items_fmt=items[0]
			lib.pretty_print("There is a single {} before you.".format(items_fmt))
		else:
			items_fmt='{}, and{}'.format(','.join(items[:-1]),items[total_items-1])
			lib.pretty_print("You can see {} before you.".format(items_fmt))
		return 0

	def look(self,player):
		lib.pretty_print(self.desc)
		self.print_exits()
		self.print_items()

	def remove_item(self,items):
		self.items.pop(items.name,None)

	def remove_mob(self,mob):
		self.mobs.pop(mob.name,None)

	def add_mobs(self,mobs):
		if self.mobs is None:
			self.mobs={}
		mobs_type=type(mobs).__name__
		if mobs_type == 'list':
			for mob in mobs:
				self.mobs[mob.name]=mob
		elif mobs_type == 'dict':
			for mob_name,mob in mobs.items():
				self.mobs[mob_name]=mob
		else:
			self.mobs[mobs.name]=mobs

	def add_moves(self,moves=exits):
		self.exits=moves

	def look_obj(self,obj):
		if self.mobs is None and self.items is None:
			lib.pretty_print("There is \[b]nothing\[o] here to see.")
		elif self.mobs is not None and obj in self.mobs:
			lib.pretty_print(self.mobs[obj].desc)
		elif self.items is not None and obj in self.items:
			lib.pretty_print(self.items[obj].desc)
		else:
			lib.pretty_print(f"The \[b]{obj}\[o] doesn't exist or you mistyped it. Check your spelling.")

class Dark_room(Room):
	desc={'dark':"It's dark and you can see nothing",
		'light':"You can see the room now."}
	is_dark=True
	#this will hold the hidden mobs and items
	#that we'll eventually make public and usable once the room is lit up.
	hidden_mobs=None
	hidden_items=None

	def __init__(self,dark=desc['dark'],light=desc['light']):
		super().__init__()
		self.dark=dark
		self.light=light
		self.desc='Nothing can be seen.'

	def add_hidden_mobs(self,mobs):
		self.hidden_mobs={}
		mobs_type=type(mobs).__name__
		if mobs_type == 'list':
			for mob in mobs:
				self.hidden_mobs[mob.name]=mob
		elif mobs_type == 'dict':
			for mob_name,mob in mobs.items():
				self.hidden_mobs[mob_name]=mob
		else:
			self.hidden_mobs[mobs.name]=mobs

	def add_hidden_items(self,items):
		self.hidden_items={}
		items_type = type(items).__name__
		if items_type == 'list':
			for item in items:
				self.hidden_items[tem.name]=item
		elif items_type == 'dict':
			for item_name,item in items.items():
				self.hidden_items[item_name]=item
		else:
			self.hidden_items[items.name]=items

	def remove_hidden_mob(self,mob):
		self.hidden_mobs.pop(mob.name)

	def remove_hidden_item(self,item):
		self.hidden_items.pop(item.name)

	def look(self,player):
		if player.alight:
			lib.pretty_print(self.light)
			if self.hidden_mobs != None and self.mobs == None:
				print(self.hidden_mobs)
				super().add_mobs(self.hidden_mobs)
			if self.hidden_items != None and self.items == None:
				super().add_items(self.hidden_items)
		else:
			lib.pretty_print(self.dark)

		super().print_exits()
		super().print_items()

class Mob:
	_id = 0
	desc="You can't discern anything about it."
	interaction="It just looks at you."
	room=None
	alive=True
	name='None'
	hp=5
	grab_desc="It's too large to fit in your pocket."

	def __init__(self,desc=desc,interaction=interaction,alive=alive,name=name,hp=hp,grab_desc=grab_desc):
		self.name=name
		self.desc=desc
		self.interaction=interaction
		self._id=Mob._id
		self.grab_desc=grab_desc
		Mob._id+=1
		self.alive=alive
		self.hp=hp

	def interact(self):
		lib.pretty_print(self.interaction)

	def grab(self):
		lib.pretty_print(self.grab_desc)

class Grue(Mob):
	def __init__(self):
		super().__init__(desc='A teriffying beast stands before you a giant grue',interaction='You were eaten by a grue',name='Grue',hp=10)

	def interact(self,player):
		#if the room is lit up we can see everything. By default the grue is always there.
		#if you have the flashlight and interact with it. It'll tell lyou some information
		#and then it'll let you shine it in it's eyes causing it run away and break through the wall
		#thus leading to the victory room.
		#if you interact with it without a flaslight you'll be eaten.
		if player.alight:
			lib.pretty_print("The \[b]Grue\[o] stared at the \[b]flashglight\[o]'s glowing beam intently. It then stared at you. You could see the primal fear in its eyes as it ran away into the darkness.")
			player.location.remove_mob(self)
			player.location.remove_hidden_mob(self)
		else:
			lib.pretty_print("The \[b]Grue\[o] opened it mouth and the last thing you remember is the warmth leaving your body.")
			player.dead=True
