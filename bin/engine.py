
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
			<input type = "radio" name = "start" value = "choice1"/>Begin Game</input>\
			<br/><br/> \
			<input type = "submit">\
		</form>'
	
		return room_words


	
class Engine(object):
	'''
	This is the part that organizes the rooms 
	into HTML packets and sends them to the application layer.
	Also takes requests from the Application layer.
	
	Acts also as a server for the rooms...
	'''
		
	def __init__(self):
		self.rooms = {0: Title(),}
		
	def startRoom(self):
		beginning = self.rooms[0]
		return beginning.enter()
	
	def nextRoom(self,room_designator):
		#Room Designator must be a number sent back from the formfeed in the html
		nextroom = self.rooms[room_designator] 
		return nextroom.enter()
		
		
		
def gamerun():
	Roomdude = Engine()
	return Roomdude.startRoom()
