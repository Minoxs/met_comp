#!/usr/bin/env python3
from tkinter import *
from PIL import Image, ImageTk
import bessel

class Window(Frame):
	
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.master = master
		self.init_window()

	def init_window(self):
		self.master.title("Bessel")
		self.pack(fill=BOTH, expand = 1)
		quitButton = Button(self,text="Quit",command=self.client_exit)
		quitButton.place(x=50,y=0)
		wbutton = Button(self,text="input",command=self.winput)
		wbutton.place(x=0,y=0)

	def winput(self):
		winput = Tk()
		winput.geometry("800x600")
		app2 = InputWindow(winput)
		winput.mainloop()

	def client_exit(self):
		exit()

root = Tk()
root.geometry("800x600")
app = Window(root)
root.mainloop()
