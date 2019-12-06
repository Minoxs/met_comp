#!/usr/bin/env python3
from tkinter import *
from bessel import *
from PIL import Image, ImageTk

root = Tk()

class Start_Menu(Frame):

	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.master = master
		self.init_window()
	
	def init_window(self):
		self.master.title("Bessel")
		self.pack(fill=BOTH, expand=1)
		exit_button = Button(self, text="Quit",command=exit,height=4,width=8)
		exit_button.place(relx = 1, rely = 1, x = -2, y = -2,anchor = SE)
		switch_button = Button(self,text="switch",command=self.reform)
		switch_button.grid(row=1,column=0)

	def reform(self):
		self.destroy()
		app=entry_menu(root)

class entry_menu(Frame):

	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.master = master
		self.init_window()

	def init_window(self):
		self.pack(fill=BOTH, expand=1)
		back = Button(self,text="go back",command=self.switch)
		back.pack()

	def switch(self):
		self.destroy()
		app=Start_Menu(root)




app = Start_Menu(root)

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
w=400
h=300

root.geometry("{}x{}".format(w,h))

root.mainloop()