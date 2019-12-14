#!/usr/bin/env python3
from decimal import *
from matplotlib import pyplot as plib
from matplotlib import ticker
import PySimpleGUI as gui
import time

pi = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
getcontext().prec = 100

def cos(x):
    getcontext().prec += 2
    i, lasts, s, fact, num, sign = 0, 0, 1, 1, 1, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    getcontext().prec -= 2
    return +s

def sin(x):
    getcontext().prec += 2
    i, lasts, s, fact, num, sign = 1, 0, x, 1, x, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    getcontext().prec -= 2
    return +s

def saveplot(graf): #Função que plota os dados de (x,J0,J1), graf é um arquivo .csv, resultado em .svg e .pdf
	x  = graf[0]
	j0 = graf[1]
	plib.figure(figsize=(50,20))
	ax = plib.axes()
	plib.xlim(int(x[0]),int(x[-1]))
	ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
	ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
	ax.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
	ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.01))
	plib.grid(b=True)
	plib.plot(x,j0)
	plib.title("Função de Bessel de {} até {}, N = {}".format(float(round(x[0],2)),float(round(x[-1],2)),graf[2]))
	plib.ylabel("y")
	plib.xlabel("x")
	plib.legend(["J0(x)"])
	plib.savefig('Plot_{}_{}.pdf'.format(int(x[0]),int(x[-1])),bbox_inches='tight',pad_inches=0.25)
	plib.savefig('Plot_{}_{}.svg'.format(int(x[0]),int(x[-1])),bbox_inches='tight',pad_inches=0.25)
	print("Salvos:\nPlot_{0}_{1}.pdf\nPlot_{0}_{1}.svg\n".format(int(x[0]),int(x[-1])))
	return "sucesso"

def tabelar(xi,xf,n):
	xi = Decimal(xi)
	xf = Decimal(xf)
	n  = Decimal(n)
	x_list = []
	j0 = []
	while xi <= xf:
		x_list.append(xi)
		run = bessel(xi,n)
		j0.append(run)
		xi += Decimal("0.1")
	return [x_list,j0,n]

def f(F,x):
	return eval(F)

def bessel(x, n = 10000):
	F = "cos(Decimal({})*sin(x))".format(x)
	res = trapez(F,0,pi,n)
	return res[0] * (1/Decimal(pi))

def trapez(F,a,b,n):
	if F == "":
		F = x
	start = time.time()
	a = Decimal(a)
	b = Decimal(b)
	n = int(n)
	step = (b-a)/n
	res_sum = 0
	m = 0
	while a <= b:
		if n >= 100 and m%int(n/100) == 0:
			gui.OneLineProgressMeter("Integrando...",m,n,"integrate_key")
		fx = f(F,a)
		a += step
		res_sum += fx
		m += 1
	gui.OneLineProgressMeter("Integrando...",n,n,"integrate_key")
	end = time.time()
	return [round(res_sum*step,5),end-start]


#GUI CODE
gui.change_look_and_feel('Dark Blue 3')
layout = [
	[gui.T("f",size=(1,1)),gui.In(key="f",size=(40,2)),gui.T("a",size=(1,1)),gui.In(key="a",size=(40,2)),gui.T("b",size=(1,1)),gui.In(key="b",size=(40,2)),gui.T("N",size=(1,1)),gui.In(key="n",size=(40,2)),gui.Exit()],
	[gui.Output(size=(180,20))],
	[gui.Button("Integrate",size=(180,4))]
]

window = gui.Window("Trabalho 5",layout)

while True:
	event, values = window.read()
	if event in (None,"Exit"):
		break
	if event == "Integrate":
		if values['f'].lower() == "bessel" and values['a'] != "" and values['b'] == "" and values['n'] != "":
			run = bessel(values['a'],values['n'])
			print(round(run,5))
			continue
		if values['f'].lower() == "bessel" and values['a'] != "" and values['b'] != "" and values['n'] != "":
			run = tabelar(values['a'],values['b'],values['n'])
			saveplot(run)
			continue
		run = trapez(values['f'],values['a'],values['b'],values['n'])
		print("{}\nTook: {}s".format(run[0],run[1]))
