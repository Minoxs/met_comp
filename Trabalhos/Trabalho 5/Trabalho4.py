#!/usr/bin/env python3
from decimal import *
import PySimpleGUI as gui
import threading
from queue import Queue

a = "3.141592653589793"
getcontext().prec = 5

q = Queue()

def quad(x):
	return Decimal(x) ** 2

def trapez(a,b):
	a = Decimal(a)
	b = Decimal(b)
	res_sum = 0
	step = Decimal("0.0001")
	while a <= b:
		gui.OneLineProgressMeter("Integral from {} to {}".format(a,b),float(a),float(b),"integrate_key")
		worker = q.get()
		f = quad(a)
		a += step
		area = f * step
		res_sum += area
	print(res_sum)

gui.change_look_and_feel('Dark Blue 3')
layout = [
	[gui.T("a",size=(2,1)),gui.In(key="a",size=(40,2)),gui.T("b",size=(2,1)),gui.In(key="b",size=(40,2)),gui.Exit()],
	[gui.Output(size=(130,40))],
	[gui.Button("Integrate",size=(120,6))]
]

window = gui.Window("Integrate",layout)

while True:
	event, values = window.read()
	if event in (None,"Exit"):
		break
	if event == "Integrate":
		trapez(values['a'],values['b'])