'''
Basic Text Adventure in Python
Class Library File
This file contains all of the classes that are used in the game.
Macarthur Inbody
AGPLv3 or Later
2019
'''
#change the location to be player instead of
#a room id for where the item is. The location will
#be a signed int. If the item is gone it becomes None meaning
#that it's gone.
# if it's -1 then it has moved to the player's inventory
# because that is the "room" or structure id of their inventory.
class Item:
	_id=0
	desc=''
	interaction=''
	location=None
	def __init__(self,desc=desc,interact=interaction,location=location):
		self.desc=desc
		self.interaction=interact
		self.location=location
		self._id=Item._id
		Item._id+=1
	def get_item(self,player):
		move_location(self,-1)
		print("You have grabbed {} and put it into your \033[1minventory".format(self.desc))

	def move_location(self,location):
		self.location=location

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
	def __init__(self,contains=contains):
		Item.__init__(self)
		self.contains=contains

class Player:
	x=0
	y=0
	location={}
	weapon=None
	dead=False
	hp=10
	def __init__(self):
		self.x=0
		self.y=0
		self.weapon=None
		self.dead=False
		self.location={}
		self.hp=10
	def transport(self,room):
		self.location=room

	def move(self,movement,current_room):
		exits=current_room.exits
#		selected_move = ( movement or movement[0:1] in self.location.exits.get(movement,None))
		if movement is None:
			print("None given.")
		elif movement in exits:
			selected_move=exits.get(movement,None)
		elif movement[0:1] in exits:
			selected_move=exits.get(movement[0:1],None)
		else:
			selected_move=False

		if  selected_move:
			self.location=selected_move
		else:
			return None

	def damaged(amount):
		self.hp=self.hp-amount


class Inventory(Player):
	items={}
	def __init__(self,items=items):
		self.items=items

	def add(self,item):
		self.items.append(item)

	def show(self):
		for item in self.items:
			print(item._id.desc)

	def use(self,item):
		if item in items:
			print(item.interaction)
		else:
			print("You don't have that item")

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

	def add_moves(self,moves=exits):
		self.exits=moves


class Mob:
	_id = 0
	desc="You can't discern anything about it."
	interact="It just looks at you."
	room=None
	alive=True
	name='None'
	hp=5
	def __init__(self,desc=desc,interact=interact,alive=alive,name=name,hp=hp):
		self.name=name
		self.desc=desc
		self.interact=interact
		self._id=Mob.id
		Mob._id+=1
		self.alive=alive
		self.hp=hp

class Grue(Mob):
	def __init__(self):
		super().__init__(desc='A giant grue stands before you',interact='You were eaten by a grue',name='Grue',hp=10)
