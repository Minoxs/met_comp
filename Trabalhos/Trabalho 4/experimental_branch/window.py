#!/usr/bin/env python3
from tkinter import *
from bessel import *
from PIL import Image, ImageTk

root = Tk()

class Console(Frame):

	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.master = master
		self.init_window()
	
	def init_window(self):
		self.master.title("Bessel")
		self.pack(side=BOTTOM,fill=BOTH, expand=0)
		exit_button = Button(self, text="Quit",command=exit,width=10,height=5)
		exit_button.pack(anchor=SE)

class Start_Menu(Frame):

	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.master = master
		self.init_window()
	
	def init_window(self):
		self.master.title("Bessel")
		self.pack(side=TOP,fill=BOTH, expand=1)
		
		W = 20
		H = 2
		test_button = Button(self, text="Rodar Testes de Precisão", command=self.default_tests,width=W,height=H)
		test_button.pack()
		tabelar_button = Button(self, text="Tabelar & Plotar", command=self.tabelar_menu,width=W,height=H)
		tabelar_button.pack()
		plot_button = Button(self, text="Carregar Gráfico", command=self.plot_menu,width=W,height=H)
		plot_button.pack()

	def default_tests(self):
		self.destroy()
		app=Default_Tests(root)

	def tabelar_menu(self):
		self.destroy()
		app=Tabelar_Menu(root)

	def plot_menu(self):
		self.destroy()
		app=Plot_Menu(root)

class Default_Tests(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.master = master
		self.init_window()

	def init_window(self):
		self.pack(side=TOP, fill=BOTH, expand = 1)
		go_back = Button(self,text="Voltar",command=self.back)
		go_back.pack(anchor=NE)

		confirm = Label(self,text="Rodar Testes?\nUsualmente leva 1-3 minutos")
		confirm.pack()

	def back(self):
		self.destroy()
		app=Start_Menu(root)

class Tabelar_Menu(Frame):

	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.master = master
		self.init_window()

	def init_window(self):
		self.pack(side=TOP, fill=BOTH, expand = 1)
		go_back = Button(self,text="Voltar",command=self.back)
		go_back.pack(anchor=NE)

	def back(self):
		self.destroy()
		app=Start_Menu(root)

class Plot_Menu(Frame):

	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.master = master
		self.init_window()

	def init_window(self):
		self.pack(side=TOP, fill=BOTH, expand = 1)
		go_back = Button(self,text="Voltar",command=self.back)
		go_back.pack(anchor=NE)

	def back(self):
		self.destroy()
		app=Start_Menu(root)

app = Start_Menu(root)
app = Console(root)

root.geometry("800x600")
root.resizable(0,0) #Desativar modificação no tamanho da janela

root.mainloop()