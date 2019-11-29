#!/usr/bin/env python3
from matplotlib import pyplot as plib
import math
from decimal import *
"""
Estou usando a biblioteca decimal para ter um numero arbitrário de digitos significativos
"""
getcontext().prec = 60

def Test():
	#50 digitos
	#Estimativas de erros usando valores encontrados na internet para a função
	j0_2 = Decimal(0.22389077914123566805182745464994862582515448221861)
	j0_37 = Decimal(0.010862369724899694740993821310850856019800294935816)
	calc_j0_2 = my_j0(2)
	calc_j0_37 = my_j0(37)
	print(j0_2 - calc_j0_2)
	print(j0_37 - calc_j0_37)

def my_j0(x, kmax = 1000):
	J0 = Decimal(0)
	for k in range(kmax):
		J0 += Decimal(((-x**2)**k))/Decimal(((4**k)*(math.factorial(k)**2)))
	return J0

def my_j1(x, kmax = 1000):
	pass

Test()
