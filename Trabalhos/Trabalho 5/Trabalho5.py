#!/usr/bin/env python3
from decimal import *
import PySimpleGUI as gui
import threading
from queue import Queue
import time

pi = "3.141592653589793"
getcontext().prec = 100

def f(F,x):
	return eval(F)

def trapez(F,a,b,n):
	if F == "":
		F = x
	if a == "" or b == "" or n == "":
		print("Preencha os campos a,b e n")
		return 0
	start = time.time()
	a = Decimal(a)
	b = Decimal(b)
	n = int(n)
	step = (b-a)/n
	res_sum = 0
	m = 0
	while a <= b:
		if m%(n/100) == 0:
			gui.OneLineProgressMeter("Integrando...",m,n,"integrate_key")
		if event == "Cancel":
			break
		fx = f(F,a)
		try:
			a += step
		except TypeError:
			print("Função não suportada")
			return 0
		res_sum += fx
		m += 1
	end = time.time()
	return [round(res_sum*step,5),end-start]

gui.change_look_and_feel('Dark Blue 3')
layout = [
	[gui.T("f",size=(1,1)),gui.In(key="f",size=(40,2)),gui.T("a",size=(1,1)),gui.In(key="a",size=(40,2)),gui.T("b",size=(1,1)),gui.In(key="b",size=(40,2)),gui.T("N",size=(1,1)),gui.In(key="n",size=(40,2)),gui.Exit()],
	[gui.Output(size=(180,20))],
	[gui.Button("Integrate",size=(180,4))]
]

window = gui.Window("Integrate",layout,return_keyboard_events = True)

while True:
	event, values = window.read()
	if event in (None,"Exit"):
		break
	if event in ("Integrate"):
		if values['a'] == "" or values['b'] == "":
			continue
		run = trapez(values['f'],values['a'],values['b'],values['n'])
		print("{}\nTook: {}s".format(run[0],run[1]))