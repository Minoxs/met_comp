#!/usr/bin/env python3
from tkinter import *
from bessel import *
from PIL import Image, ImageTk

root = Tk()

oneframe = Frame(root)
oneframe.pack()

def do():
	button1.destroy()
	button2.pack()

button2 = Button(oneframe, text="quit?", command=exit)
button1 = Button(oneframe, text="Exit",command=do)
button1.pack()


root.geometry("800x600")
root.mainloop()