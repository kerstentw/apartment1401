
# Rooms are individual classes who are stored in a dictionary as class data.
# Each Room consists of 3 things: 1.) the text of the room describing it.  And 2.) The HTML that formats it.
#       And 3.) The return keyword
# Each room is an HTML packet that is sent to the application layer through the Engine.



import roomstrings #Roomstrings contains a bunch of functions to call that return strings

class Room(object):

	'''
	This is the Parent class for the module.
	There wont be much here at first.  It's more a service module
	
	'''
	game_inventory = 5 # This will be a game 'inventory' but each entry is a 'gate' you must read at least 
						# 5 of the 10 pieces of info before getting to the end...

						
						
						
class Title(Room): #The RADIO must send a value equaling the key of the
					#dictionary storage location you are storing the room

	def enter(self):
		room_words = roomstrings.title() + '<form type = "input" action = "/index" method = "POST"><br/>\
			<input type = "radio" name = "content1" value = 1 />Begin Game</input>\
			<input type = "radio" name = "content1" value = 2>Exit</input>\
			<br/><br/> \
			<input type = "submit" value = "Start Game">\
		</form>'
	
		return room_words

		
		
		
class TestRoom(Room): #This will eventually be a room!!!!!!
	
	def enter(self):
		room_words = roomstrings.testroom() + '<br><form type = "input" action = "/index" method "POST">\
		<input type = "radio" name = "content1" value = 0>Go Back</input>\
		<br><input type = "submit" value = "DO IT!">\
		</form>\
		'
		
		return room_words
	
	
class Exit(Room):

	def enter(self):
		return roomstrings.exit()
	
class Engine(object):
	'''
	This is the part that organizes the rooms 
	into HTML packets and sends them to the application layer.
	Also takes requests from the Application layer.
	
	Acts also as a server for the rooms...
	'''
		
	def __init__(self):
		self.rooms = {
		0: Title(),
		1: TestRoom(),
		2: Exit()
		}
		
	def startRoom(self):
		beginning = self.rooms[0]
		return beginning.enter()
	
	def nextRoom(self,room_designator):
		#Room Designator must be a number sent back from the formfeed in the html
		#Everytime this function is called it goes to whatever integer it was fed...
		nextroom = self.rooms[int(room_designator)] 
		return nextroom.enter()
		
		

#THIS USED TO BE THE WAY WE STARTED THE GAME BUT NOT THE INDEX HANDLER CLASS JUST COMPOSES AN INSTANCE OF THE ENGINE IN ITS __init__
#def gamerun():
#	Roomdude = Engine()
#	return Roomdude.startRoom()