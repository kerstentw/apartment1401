
# Rooms are individual classes who are instanced in a library.
# Each room is an HTML packet that is sent to the application layer through the Engine.


class Room(object):

	'''
	This is the Parent class for the module.
	There wont be much here at first.  It's more a service module
	
	'''

	
class Title(Room):

	def enter(self):
		room_words = 'You are on the title screen!  What next?\
		<form type = "input" action = "/" method = "post"><br/>\
			<input type = "radio" name = "start" value = "choice1"/>\
		</form>'
	
		return room_words

class RoomLibrary(object):
	'''
	
	This is where you put the rooms.
	Store them in a dictionary with the keys labeled by numbers
	'''

	rooms = {1: Title()}
	
	
class Engine(object):
	'''
	This is the part that organizes the rooms 
	into HTML packets and sends them to the application layer.
	Also takes requests from the Application layer.
	
	Acts also as a server for the rooms...
	'''
		
	def __init__(self, roomlib = {}):
		self.rooms = roomlib
		
	def startRoom(self):
		self.rooms[1].enter()
	
	def nextRoom(self):
		pass
		
		
		
#def gamerun():
#	RoomLib = RoomLibrary()
#	Roomdude = Engine(RoomLib)
#	Roomdude.startRoom()
