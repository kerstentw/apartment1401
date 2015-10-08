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
							borderwidth = 5,
							#height = 1000,
							#width = 550,
							cnf = {'height':700, 'width' : 550}
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
		self.frame.pack(
		fill = BOTH, 
		padx = 40, 
		pady = 0)
		
	
	
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
			pady = 5,
			padx = 5,
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
			anchor = 'se'
		)
		
		
	def myButtons_lower(self):
				
		###FORWARD###
		self.button_forward = Tkinter.Button(
			self.frame,
			text = "Fwd",
			command = lambda: self.testMe('Forward'),
			padx = 3,
			pady = 3
		)
		self.button_forward.place(x = 250, y = 525)
		#self.button_forward.pack(anchor = 's')
		
		###LEFT###
		self.button_left = Tkinter.Button(
			self.frame,
			text = "lft",
			command = lambda: self.testMe("Left"),
			padx = 3,
			pady = 3
		)
		self.button_left.place(x = 200, y = 575)
		#self.button_left.pack(anchor = 's')
		
		###RIGHT###
		self.button_right = Tkinter.Button(
			self.frame,
			text = "rgt",
			command = lambda: self.testMe('Right'),
			padx = 3,
			pady = 3
		)
		
		self.button_right.place(x = 275, y = 575 )
		#self.button_right.pack(anchor = 's')
		
		
		###BACK###
		self.button_back = Tkinter.Button(
			self.frame,
			text = "bck",
			command = lambda: self.testMe('Back'),
			padx = 3,
			pady = 3, 
		)
		self.button_back.place(x = 250, y = 600)
		
		#self.button_back.pack(anchor = 's')
		
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
			self.myFrame()
			self.myButtons_upper()
			self.myImage()
			self.myText()
			self.myButtons_lower()
			self.tk.mainloop()
			self.frame.winfo_children()



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
 
