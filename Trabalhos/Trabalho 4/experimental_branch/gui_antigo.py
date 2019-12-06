#!/usr/bin/env python3
from tkinter import *
from PIL import Image, ImageTk

class Window(Frame):
	
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.master = master
		self.init_window()

	def init_window(self):
		self.master.title("Bessel")
		self.pack(fill=BOTH, expand = 1)
		quitButton = Button(self,text="Quit",command=self.client_exit)
		quitButton.place(x=0,y=0)
		menu = Menu(self.master)
		self.master.config(menu=menu)
		file = Menu(menu)
		file.add_command(label="exit", command=self.client_exit)
		menu.add_cascade(label="file", menu=file)
		edit = Menu(menu)
		edit.add_command(label="undo")

	def client_exit(self):
		exit()

root = Tk()
root.geometry("800x600")
app = Window(root)
root.mainloop()