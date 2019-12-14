#!/usr/bin/env python3
from decimal import *
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

def f(F,x):
	return eval(F)

def bessel(x, n = 10000):
	F = "cos({}*sin(x))".format(x)
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

window = gui.Window("Trabalho 5",layout,return_keyboard_events = True)

while True:
	event, values = window.read()
	if event in (None,"Exit"):
		break
	if event == "Integrate":
		if values['f'].lower() == "bessel":
			run = bessel(values['a'],values['n'])
			print(run)
			continue
		run = trapez(values['f'],values['a'],values['b'],values['n'])
		print("{}\nTook: {}s".format(run[0],run[1]))
