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
		load = Image.open(img)
		render = ImageTk.PhotoImage(load)

		self.img = Label(self.console_frame, image=render)
		self.img.image = render
		self.img.pack()

	def remove_img(self):
		self.img.destroy()

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
		
		W = 40
		H = 4
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
		yes = Button(self.temp,text="Sim",command=self.Yes,height=3,width=10)
		no = Button(self.temp,text="Não",command=self.back,height=3,width=10)
		yes.place(x=515,y=70)
		no.place(x=615, y=70)

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
		Xi_label.grid(row=0,column=0)
		Xf_label.grid(row=0,column=2)
		self.Xi.grid(row=0,column=1)
		self.Xf.grid(row=0,column=3)
		continue_button.grid(row=0,column=4)
		self.nt = 0

	def create_temp_frame(self):
		self.temp = Frame(root)
		self.temp.pack(side=TOP,fill=BOTH,expand=1)

	def do(self):
		if self.Xi.get() == "" or self.Xf.get() == "":
			return 0
		if self.nt >= 1:
			Console.remove_img(self)
			Console.delete_entry(self)
		else:
			Console.create_console_frame(self)
		Console.show(self,"Tabelando...")
		root.update_idletasks()
		self.tab = tabelar(Decimal(self.Xi.get()),Decimal(self.Xf.get()))
		self.run = pngplot(self.tab)
		Console.delete_entry(self)
		Console.show(self,"Pronto!")
		Console.show_img(self,self.run)
		self.size_label = Label(self.temp, text="Mudar escala de X")
		self.size_entry = Entry(self.temp)
		self.size_confirm = Button(self.temp,text="Confirmar",command=self.config)
		self.size_label.grid(row=1,column=0)
		self.size_entry.grid(row=1,column=1)
		self.size_confirm.grid(row=1,column=2)
		self.nt += 1

	def config(self):
		if self.size_entry.get() == "":
			return 0
		pngplot(self.tab,5.5,13.5,round(float(self.size_entry.get()),2))
		saveplot(self.tab,Decimal(50)/Decimal(2.54),Decimal(30)/Decimal(2.54),round(float(self.size_entry.get()),2))
		Console.remove_img(self)
		Console.show_img(self,self.run)

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
		self.pack(side=RIGHT, fill=BOTH, expand = 1)
		go_back = Button(self,text="Voltar",command=self.back)
		go_back.pack(anchor=NE)

		self.create_temp_frame()
		Xi_label = Label(self.temp,text="Xi")
		Xf_label = Label(self.temp,text="Xf")
		self.Xi = Entry(self.temp)
		self.Xf = Entry(self.temp)
		continue_button = Button(self.temp,text="Carregar Gráfico",command=self.do)
		Xi_label.grid(row=0,column=0)
		Xf_label.grid(row=0,column=2)
		self.Xi.grid(row=0,column=1)
		self.Xf.grid(row=0,column=3)
		continue_button.grid(row=0,column=4)
		empty_button = Button(self.temp,width=15)
		explanation = Label(self.temp,text="Certifique que PLOT_DATA está na mesma pasta que window.py")
		empty_button.grid(row=0,column=5)
		explanation.grid(row=0,column=6)
		self.nt = 0
		self.err = 0

	def create_temp_frame(self):
		self.temp = Frame(root)
		self.temp.pack(side=TOP,fill=BOTH,expand=1)

	def do(self):
		if self.Xi.get() == "" or self.Xf.get() == "":
			return 0
		if self.err == 1:
			Console.delete_entry(self)
			self.err -= 1
		if self.nt >= 1:
			Console.remove_img(self)
			Console.delete_entry(self)
		elif self.nt == 0:
			Console.create_console_frame(self)
			self.nt += 1
		Console.show(self,"Carregando...")
		root.update_idletasks()
		self.tab = "PLOT_DATA_{}_{}.csv".format(self.Xi.get(),self.Xf.get())
		try:
			self.run = pngplot(self.tab)
		except:
			Console.delete_entry(self)
			Console.show(self,"{} Não encontrado!".format(self.tab))
			self.err += 1
			return 0
		Console.delete_entry(self)
		Console.show(self,"Pronto!")
		Console.show_img(self,self.run)
		self.size_label = Label(self.temp, text="Mudar escala de X")
		self.size_entry = Entry(self.temp)
		self.size_confirm = Button(self.temp,text="Confirmar",command=self.config)
		self.size_label.grid(row=1,column=0)
		self.size_entry.grid(row=1,column=1)
		self.size_confirm.grid(row=1,column=2)

	def config(self):
		if self.size_entry.get() == "":
			return 0
		pngplot(self.tab,5.5,13.5,round(float(self.size_entry.get()),2))
		saveplot(self.tab,Decimal(50)/Decimal(2.54),Decimal(30)/Decimal(2.54),round(float(self.size_entry.get()),2))
		Console.remove_img(self)
		Console.show_img(self,self.run)

	def back(self):
		try:
			Console.clean(self)
		except:
			pass
		self.temp.destroy()
		self.destroy()
		app=Start_Menu(root)

app = Start_Menu(root)
app = Console(root)

root.geometry("1200x700")
root.resizable(0,0) #Desativar modificação no tamanho da janela

root.mainloop()