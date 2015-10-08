#!/usr/bin/python
import Tkinter,sys 
from UserDict import UserDict
from Tkconstants import *
#from PIL import Image as Pilconvert
#from PIL import imageTK


class Images(UserDict):
	
	def __init__(self):
		self.__init__ = UserDict.__init__
	
		
class TK(object):
	
	'''Pass the instance of TK to this class then build shit'''
	
	def __init__(self,interfaces):
		self.imagelib = Images()
		self.tk = interfaces
		self.frame = Tkinter.Frame(
							self.tk, 
							borderwidth = 15,
							)
							
		self.button_frame = Tkinter.Frame(
								self.tk,
								borderwidth = 0,
								height = 100,
								)
		self.message = 'WELCOME!'
		self.player_coord = (0,0)
	
	
	
	def __del__(self):
		print "Window Closed"
	
	def myFrame(self,*refresh):
		
		if refresh:
			for children in self.frame.winfo_children():
				if "Button" in str(children.__doc__):
					continue
					
				else:
					children.destroy()
		
		
		#self.frame = Tkinter.Frame(self.tk, borderwidth = 5)
		else:
			self.frame.pack()
			self.button_frame.pack()
	
	
	def myText(self):
		#self.text = Tkinter.Text(
		#cnf = {'height' : 1, 
		#'width' : 100,
		#'text' : 'Test'
		#}
		
		#) ### Build a config dictionary for this in a seperate .conf
		
		
		#self.text.pack(anchor = 'center')
		
		
		
		self.text = Tkinter.Label(
			self.frame,
			text = self.message,
			background = '#FFFFFF',
			height = 2,
		
		)
		self.text.pack(fill = BOTH, anchor = 'n')
	
	
	
	
	def myImage(self):
	
	##!!!!!!Turn this into an image serving thing based on the player
	## Location in an array.###
		
	#if PIL
		#imager = PIL.open("SADBATMAN.jpg")
		#titleimage = Tkinter.PhotoImage(imager)
		
		titleimage = Tkinter.BitmapImage(file = 'SADBATMAN.xbm')
		
		label = Tkinter.Label(
			self.frame, 
			image = titleimage,
			background = "#FFFFFF",
			height = 500,
			width = 500,
			)
		
		label.image = titleimage
		
		#label.pack(fill = BOTH)
		
		label.pack(anchor = 'n')

		#self.image_dic = Images()
		
		#image = Pilconvert.open('SADBATMAN.bmp')

		

		#photo = ImageTK.photoImage(image)
		#Label = Tkinter.Label(image = photo)
		#Label.image = photo
		#Label.pack()
			
	def myButtons_upper(self):
		###EXIT###
		self.button_exit = Tkinter.Button(
			self.frame,
			text = "Exit", 
			command = self.tk.destroy,
			padx = 3,
			pady = 3
		) 
		
		self.button_exit.pack(
			anchor = 'ne'
		)
		
		
	def myButtons_lower(self):
		
		
		###FORWARD###
		self.button_forward = Tkinter.Button(
			self.button_frame,
			text = "^",
			command = lambda: self.testMe('Forward'),
			padx = 3,
			pady = 3
		)
		#self.button_forward.place(x = 0, y = 0)
		#self.button_forward.pack(anchor = 's')
		self.button_forward.grid(row = 0, column = 1)
		
		
		###LEFT###
		self.button_left = Tkinter.Button(
			self.button_frame,
			text = "<",
			command = lambda: self.testMe("Left"),
			padx = 3,
			pady = 3
		)
		#self.button_left.place(x = -50, y = 1)
		#self.button_left.pack(anchor = 's')
		self.button_left.grid(row = 1, column = 0)
		
		###RIGHT###
		self.button_right = Tkinter.Button(
			self.button_frame,
			text = ">",
			command = lambda: self.testMe('Right'),
			padx = 3,
			pady = 3
		)
		
		#self.button_right.place(x = 50, y = 0 )
		#self.button_right.pack(anchor = 's')
		self.button_right.grid(row = 1, column = 2)
		
		###BACK###
		self.button_back = Tkinter.Button(
			self.button_frame,
			text = "v",
			command = lambda: self.testMe('Back'),
			padx = 4,
			pady = 4, 
		)
		#self.button_back.place(x = 5, y = 5 )
		
		
		#self.button_back.pack()
		self.button_back.grid(row = 2, column =1)
		###INVESTIGATE###
		
		
				
	def run(self, *refresh):

		if refresh:
			
			self.myFrame(1)
			#self.myButtons_upper()
			self.myImage()
			self.myText()
			#self.myButtons_lower()
			print self.frame.winfo_children()
			
		else:
			
			
			self.myButtons_upper()
			self.myImage()
			self.myText()
			self.myFrame()						
			self.myButtons_lower()
			self.tk.mainloop()
			


	def testMe(self, *test_text):
			
			if test_text:
				self.message = test_text
				#self.text.destroy()
				self.run(1)
				print "test %r" % test_text
			
			else:
				self.message = 'No Connect'
				print "Test Default, No entries"
	
   


inter = Tkinter.Tk()
#IMAGE = Tkinter.Image(imgtype = 'BitmapImage')

Gui = TK(inter)
Gui.run()
 
