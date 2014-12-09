
# Rooms are individual classes who are stored in a dictionary as class data.
# Each Room consists of 3 things: 1.) the text of the room describing it.  And 2.) The HTML that formats it.
#       And 3.) The return keyword
# Each room is an HTML packet that is sent to the application layer through the Engine.

#############################################
################ROOMS########################
#############################################

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
					#0
					
	def enter(self):
		room_words = roomstrings.title() + '<form type = "input" action = "/index" method = "POST"><br/>\
			<input type = "radio" name = "content1" value = 3 >Begin Game</input>\
			<input type = "radio" name = "content1" value = 14>Exit</input>\
			<br/><br/> \
			<input type = "submit" value = "Start Game">\
			</form>'
	
		return room_words
		
		
class DiningAreaWest(Room): #1
			
	def enter(self):
		room_words = roomstrings.diningarea_west() + '<form action = "/index" method = "POST">\
		<br/><input type = "radio" name = "content1" value = 4>Turn Left. </input><br/>\
		<input type = "radio" name = "content1" value = 3> Turn Right. </input><br/>\
		<input type = "radio" name = "content1" value = 7>Go to Bathroom.</input><br/>\
		<input type = "submit" value = "GO"/>\
		</form>'
		
		return room_words
		
		

class DiningAreaEast(Room): #2
	
	def enter(self):
		room_words = roomstrings.diningarea_east() + '<br><form type = "input" action = "/index" method = "POST">\
		<input type = "radio" name = "content1" value = 3>Turn Left </input> <br/>\
		<input type = "radio" name = "content1" value = 4>Turn Right </input> <br/>\
		<input type = "radio" name = "content1" value = 10>Go to Kitchen </inout> <br/>\
		<br><input type = "submit" value = "Go.">\
		\
		</form>\
		'
		
		return room_words
		

		
class DiningAreaNorth(Room): #3
	
	def enter(self):
		room_words = roomstrings.diningarea_north() + '<br><form type = "input" action = "/index" method = "POST">\
		<input type = "radio" name = "content1" value = 1>Turn Left</input><br/>\
		<input type = "radio" name = "content1" value = 2>Turn Right</input><br/>\
		<input type = "radio" name = "content1" value = 5>Go to TV Room</input><br/>\
		<input type = "radio" name = "content1" value = 6>Go to Parent\'s room </input><br/>\
		<br><input type = "submit" value = "Go.">\
		\
		</form>\
		'
		return room_words
	
class DiningAreaSouth(Room): #4
	
	def enter(self):
		room_words = roomstrings.diningarea_south() + '<br><form type = "input" action = "/index" method = "POST">\
		<input type = "radio" name = "content1" value = 2>Turn Left</input> <br/>\
		<input type = "radio" name = "content1" value = 1>Turn Right</input> <br/>\
		<input type = "radio" name = "content1" value = 8> Go to the Study </input> <br/>\
		<input type = "radio" name = "content1" value = 9>Go to brother\'s room </input> <br/>\
		<br><input type = "submit" value = "Go.">\
		\
		</form>\
		'
		
		return room_words
	
	
	

class TV_Room(Room): #5

	def enter(self):
		room_words =  roomstrings.tvroom() + '<form action = "/index" method = "POST">\
		<br/><input type = "radio" name = "content1" value = 11> Approach Window. </input>\
		<br/><input type = "radio" name = "content1" value = 3> Go Back. </input>\
		<br/><input type = "submit" value = "Go."/>\
		</form>'		
		return room_words
		
class ParentRoom(Room): #6
	
	def enter(self):
		room_words =  roomstrings.parentroom() + '<form action = "/index" method = "POST">\
		<br/><input type = "radio" name = "content1" value = 3> Go Back.</input>\
		<br/><input type = "radio" name = "content1" value = 17> pick up piece of paper</input>\
		<br/><input type = "radio" name = "content1" value = 20> Look at mom\'s journal </input>\
		<br/><input type = "radio" name = "content1" value = 17> Look at report on table </input>\
		<br/><input type = "submit" value = "Go">\
		</form>\
		'
		
		return room_words
		

	
class Bathroom(Room): #7
	
	def enter(self):
		room_words = roomstrings.bathroom() + '<form action = "/index" method = "POST">\
		<br/><input type = "radio" name = "content1" value = 1> Go Back. </input>\
		<br/><input type = "radio name = "content1" value = 7> Look at paper in trashcan. </input>\
		<br/><input type = "submit" value = "Go.">\
		</form>\
		'
		
		return room_words
		
		
class Study(Room): #8

	def enter(self):
		room_words =  roomstrings.study() + '<form action = "index" method = "POST">\
		<br/><input type = "radio" name = "content1" value = 4> Go Back. </input>\
		<br/><input type = "radio" name = "content1" value = 16> Look at Homework. </input>\
		<br/><input type = "submit" value = "Go.">\
		</form>'

		return room_words
		
class BrothersRoom(Room): #9
	
	def enter(self):
		room_words =  roomstrings.brothersroom() + '<form action = "/index" method = "POST">\
		<br/><input type = "radio" name = "content1" value = 4>Go Back</input>\
		<br/><input type = "radio" name = "content1" value = 9> Look at Journal. </input>\
		<br/><input type = "submit" value = "go.">\
		</form>'
		
		return room_words
		
		
		
class Kitchen(Room): #10

	def enter(self):
		room_words = roomstrings.kitchen() + '<form action = "/index" method = "POST">\
		<br/><input type = "radio" name = "content1" value = 18> Look at note on refridgerator. </input>\
		<br/><input type = "radio" name = "content1" value = 22> Look at Bill on counter. </input>\
		<br/><input type = "radio" name = "content1" value = 2> Go back. </input>\
		<br/><input type = "submit" value = "Go.">\
		</form>\
		'
		
		return room_words


		
class Window(Room): #11

	def enter(self):
		room_words =  roomstrings.window() + '<form action = "/index" method = "POST">\
		<br/><input type = "radio" name = "content1" value = 5> Go Back </input>\
		\
		<input type = "submit" value = "Go.">\
		</form>'
		
		return room_words
		
class End(Room): #12
	
	def enter(self):
		return roomstrings.end()
		
class Porch(Room): #25

	def enter(self):
		room_words = "The view has always been nice here.  There's a note on the floor." + '<form action = "/index" method = "POST">\
		<br/><input type = "radio" name = "content1" value = 19> Go Back </input>\
		<input type = "submit" value = "Go.">\
		</form>'
		
		return room_words
		
class Credits(Room): #13

	def enter(self):
		return roomstrings.credits()
	
class Exit(Room): #14

	def enter(self):
		return roomstrings.exit()
	
	
#############################################################
###############NOTES AND OBJECTS#############################
#############################################################

class ReportCard(Room): #15

	def enter(self):
		room_words = "It's a report card." + '<form action = "/index" method = "POST">\
	<br/><input type = "radio" name = "content1" value = 10> Go Back </input>\
	<input type = "submit" value = "Go.">\
	</form>'

		return room_words


class Homework(Room): #16

	def enter(self):
		room_words = "Doesn't look that bad to me." + '<form action = "/index" method = "POST">\
	<br/><input type = "radio" name = "content1" value = 9> Go Back </input>\
	<input type = "submit" value = "Go.">\
	</form>'
	
		return room_words
	
	
class TeacherReport(Room): #17

	def enter(self):
		room_words = "This teacher sounds like an idiot." + '<form action = "/index" method = "POST">\
	<br/><input type = "radio" name = "content1" value = 6> Go Back </input>\
	<input type = "submit" value = "Go.">\
	</form>'
		
		return room_words	
			
class TeamNote(Room): #18

	def enter(self):
		room_words = "Nice!  Little Bro.  Be Ambitious." + '<form action = "/index" method = "POST">\
		<br/><input type = "radio" name = "content1" value = 10> Go Back </input>\
		<input type = "submit" value = "Go.">\
		</form>'
		
		return room_words
		
class SuicideNote(Room): #19
	
	def enter(self):
		room_words = "What a creative kid." + '<form action = "/index" method = "POST">\
		<br/><input type = "radio" name = "content1" value = 11> Go Back </input>\
		<input type = "submit" value = "Go.">\
		</form>'
		
		return room_words
		
class MomJournal(Room): #20

	def enter(self):
		room_words = "Maybe I shouldn't be reading this..." + '<form action = "/index" method = "POST">\
		<br/><input type = "radio" name = "content1" value = 6> Go Back </input>\
		<input type = "submit" value = "Go.">\
		</form>'
		
		return room_words
		
class DadLayoff(Room): #21

	def enter(self):
		room_words = "Uh Oh.  I hope he's okay." + + '<form action = "/index" method = "POST">\
		<br/><input type = "radio" name = "content1" value = 7> Go Back </input>\
		<input type = "submit" value = "Go.">\
		</form>'
		
		return room_words
		
class Bills(Room): #22

	def enter(self):
		room_words = "What a bunch of vultures." + '<form action = "/index" method = "POST">\
		<br/><input type = "radio" name = "content1" value = 10> Go Back </input>\
		<input type = "submit" value = "Go.">\
		</form>'
		
		return room_words
		
class BrotherJournal(Room): #23

	def enter(self):
		room_words = "Maybe I shouldn't be reading this... Maybe." + '<form action = "/index" method = "POST">\
		<br/><input type = "radio" name = "content1" value = 9> Go Back </input>\
		<input type = "submit" value = "Go.">\
		</form>'
		
		return room_words
		
class ThreatNote(Room): #24

	def enter(self):
		room_words = "Who wrote this?" + + '<form action = "/index" method = "POST">\
		<br/><input type = "radio" name = "content1" value = 6> Go Back </input>\
		<input type = "submit" value = "Go.">\
		</form>'
		
		return room_words
	
#########################################################################
######################ENGINE####################################
#########################################
	
class Engine(object):
	'''
	This is the part that organizes the rooms 
	into HTML packets and sends them to the application layer.
	Also takes requests from the Application layer.
	
	Acts also as a server for the rooms...
	'''
		
	def __init__(self):
		self.rooms = {
		#####ROOMS#####
		0: Title(),
		1: DiningAreaWest(),
		2: DiningAreaEast(),
		3: DiningAreaNorth(),
		4: DiningAreaSouth(),
		5: TV_Room(),
		6: ParentRoom(),
		7: Bathroom(),
		8: Study(),
		9: BrothersRoom(),
		10: Kitchen(),
		11: Window(),
		12: End(),
		13: Credits(),
		14: Exit(),
		#####OBJECTS#####
		15: ReportCard(),
		16: Homework(),
		17: TeacherReport(),
		18: TeamNote(),
		19: SuicideNote(),
		20: MomJournal(),
		21: DadLayoff(),
		22: Bills(),
		23: BrotherJournal(),
		24: ThreatNote(),
		###FINALE###
		25: Porch(),
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