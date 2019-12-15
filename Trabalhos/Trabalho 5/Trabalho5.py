#!/usr/bin/env python3
from decimal import *
from matplotlib import pyplot as plib
from matplotlib import ticker
import PySimpleGUI as gui
import time

pi = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
getcontext().prec = 100

def roots(F,a,b):
	a = Decimal(a)
	b = Decimal(b)
	if a >= b:
		print("a deve ser diferente de b")
		return 0
	if f(F,a) > 0 and f(F,b) > 0 or f(F,a) < 0 and f(F,b) < 0:
		print("Não há raiz no intervalo")
		return 0
	mid = 1
	m = 0
	while abs(mid) > Decimal("0.00000001"):
		print("Iteration {}, F(mid_point) = {}".format(m,mid))
		mid = f(F,(b+a)/2)
		if mid < 0:
			a = (b+a)/2
		elif mid > 0:
			b = (b+a)/2
		m += 1
		if m >= 1000:
			break
	return [(b+a)/2,mid]

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

def bessel_plot(graf):
	x  = graf[0]
	j0 = graf[1]
	plib.figure(figsize=(25,10))
	ax = plib.axes()
	plib.xlim(int(x[0]),int(x[-1]))
	ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
	ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
	ax.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
	ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.01))
	plib.grid(b=True)
	plib.plot(x,j0)
	plib.title("Função de Bessel de {} até {}, N = {}\nTempo de Cálculo: {}s".format(float(round(x[0],2)),float(round(x[-1],2)),graf[2],round(graf[3],3)))
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
	tempo = 0
	while xi <= xf:
		if xi > 0 and -xi in x_list:
			one = time.time()
			x_list.append(xi)
			j0.append(j0[x_list.index(-xi)])
			tempo += time.time() - one
			xi += Decimal("0.1")
		else:
			x_list.append(xi)
			run = bessel(xi,n)
			j0.append(run[0])
			tempo += run[1]
			xi += Decimal("0.1")
	return [x_list,j0,n,tempo]

def f(F,x):
	return eval(F)

def bessel(x, n = 10000):
	F = "cos(Decimal({})*sin(x))".format(x)
	res = trapez(F,0,pi,n)
	return [res[0] * (1/Decimal(pi)),res[1]]

def trapez(F,a,b,n):
	if F == "":
		F = "x"
	start = time.time()
	a = Decimal(a)
	b = Decimal(b)
	n = int(n)
	step = (b-a)/n
	res_sum = 0
	m = 0
	while a <= b:
		if n >= 100 and m%int(n/100) == 0:
			gui.OneLineProgressMeter("Integrando...",m,n,"integrate_key",F)
		fx = f(F,a)
		a += step
		res_sum += fx
		m += 1
	if n >= 100:
		gui.OneLineProgressMeter("Integrando...",n,n,"integrate_key",F)
	end = time.time()
	return [round(res_sum*step,5),end-start]


#GUI CODE
gui.change_look_and_feel('Dark Blue 3')
layout = [
	[gui.T("f",size=(1,1)),gui.In(key="f",size=(40,2)),gui.T("a",size=(1,1)),gui.In(key="a",size=(40,2)),gui.T("b",size=(1,1)),gui.In(key="b",size=(40,2)),gui.T("N",size=(1,1)),gui.In(key="n",size=(40,2)),gui.Exit()],
	[gui.Output(size=(180,20))],
	[gui.Button("Integrate",size=(160,4))],
	[gui.Button("Find Roots",size=(160,4))]
]

window = gui.Window("Trabalho 5",layout)

while True:
	event, values = window.read()
	if event in (None,"Exit"):
		break
	if event == "Integrate":
		if values['f'].lower() == "bessel" and values['a'] != "" and values['b'] == "" and values['n'] != "":
			run = bessel(values['a'],values['n'])
			print(round(run[0],5))
			continue
		if values['f'].lower() == "bessel" and values['a'] != "" and values['b'] != "" and values['n'] != "":
			run = tabelar(values['a'],values['b'],values['n'])
			print('Tempo total: {}s'.format(round(run[3],4)))
			bessel_plot(run)
			continue
		run = trapez(values['f'],values['a'],values['b'],values['n'])
		print("{}\nTook: {}s".format(run[0],run[1]))
	if event == "Find Roots":
		print("Finding roots")
		root = roots(values['f'],values['a'],values['b'])
		print("Raiz de {} é {}".format(values['f'],root))