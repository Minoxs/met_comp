#!/usr/bin/env python3
from tkinter import *
from bessel import *
from PIL import Image, ImageTk

root = Tk()

class Console(Frame):

	def __init__(self,master=None):
		Frame.__init__(self,master,width=800,height=200)
		self.master = master
		self.init_window()
	
	def init_window(self):
		self.master.title("Bessel")
		self.pack(side=BOTTOM,fill=BOTH, expand=0)
		exit_button = Button(self, text="Quit",command=exit,width=10,height=5)
		exit_button.pack(anchor=SE)

	def create_console_frame(self):
		self.console_frame = Frame(root)
		self.console_frame.pack(side=BOTTOM)

	def show(self,add):
		self.to_print = Label(self.console_frame,text=str(add))
		self.to_print.pack()

	def show_img(self,img):
		self.load = Image.open(img)
		self.render = ImageTk.PhotoImage(load)

		self.img = Label(self.console_frame, image=render)
		self.img.image = render
		self.img.pack()

	def delete_entry(self):
		self.to_print.destroy()

	def clean(self):
		self.console_frame.destroy()

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

	def create_temp_frame(self,ex = 1):
		self.temp = Frame(root,width=800,height=600)
		self.temp.pack(fill=BOTH, expand=ex)

	def init_window(self):
		self.pack(side=TOP, fill=BOTH, expand = 1)
		go_back = Button(self,text="Voltar",command=self.back)
		go_back.pack(anchor=NE)

		confirm = Label(self,text="Rodar Testes?\nUsualmente leva 1-3 minutos")
		confirm.pack()

		self.create_temp_frame()
		yes = Button(self.temp,text="Sim",command=self.Yes)
		no = Button(self.temp,text="Não",command=self.back)
		yes.place(x=320,y=70)
		no.place(x=420, y=70)

	def back(self):
		try:
			Console.clean(self)
		except:
			pass
		self.temp.destroy()
		self.destroy()
		app=Start_Menu(root)

	def next(self):
		if len(self.results) != self.n+1:
			Console.delete_entry(self)
			Console.show(self,str(self.results[self.n]))
			self.n += 1
		else:
			self.back()

	def Yes(self):
		self.n = 0
		self.temp.destroy() #retira os botões y/n
		self.warning = Label(self,text="Por favor aguarde, Rodando testes...")
		self.warning.pack()
		root.update_idletasks()
		self.results = default_tests()
		Console.create_console_frame(self)
		Console.show(self,"{} segundos decorridos.".format(round(self.results[-1],4)))
		Console.show(self,"Pronto! Clique Continuar para mostrar resultados.")
		self.create_temp_frame(0)
		cont = Button(self.temp,text="Continuar",command=self.next)
		cont.pack(anchor=S)

class Tabelar_Menu(Frame):

	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.master = master
		self.init_window()

	def init_window(self):
		self.pack(side=RIGHT, fill=BOTH, expand = 1)
		go_back = Button(self,text="Voltar",command=self.back)
		go_back.pack(anchor=NE)

		self.create_temp_frame()
		Xi_label = Label(self.temp,text="Xi")
		Xf_label = Label(self.temp,text="Xf")
		self.Xi = Entry(self.temp)
		self.Xf = Entry(self.temp)
		continue_button = Button(self.temp,text="Tabelar & Plotar",command=self.do)
		Xi_label.grid(row=1,column=0)
		Xf_label.grid(row=2,column=0)
		self.Xi.grid(row=1,column=1)
		self.Xf.grid(row=2,column=1)
		continue_button.grid(row=3,column=0)

	def create_temp_frame(self):
		self.temp = Frame(root)
		self.temp.pack(side=TOP,fill=BOTH,expand=1)

	def do(self):
		if self.Xi.get() == "" or self.Xf.get() == "":
			return 0
		Console.create_console_frame(self)
		Console.show(self,"Tabelando...")
		root.update_idletasks()
		run = tabelar(self.Xi.get(),self.Xf.get())
		Console.delete_entry(self)
		Console.show(self,"Pronto!")
		Console.show_img(self,run)

	def back(self):
		try:
			Console.clean(self)
		except:
			pass
		self.temp.destroy()
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