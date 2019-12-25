from unittest import *
import unittest
class Room(object):

	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.paths = {}

	def go(self, direction):
		return self.paths.get(direction, None)

	def add_paths(self, paths):
		self.paths.update(paths)

start = Room("Start", "You can go west and down a hole.");
west = Room("Trees", "There are trees here, you can go east.");
down = Room("Dungeon", "It's dark down here, you can go up.");
start.add_paths({'west': west, 'down': down});
west.add_paths({'east': start});
down.add_paths({'up': start});
print(vars(start.go('west')));
