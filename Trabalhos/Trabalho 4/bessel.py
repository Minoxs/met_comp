#!/usr/bin/env python3
from matplotlib import pyplot as plib
import math
from decimal import *
"""
Estou usando a biblioteca decimal para ter um numero arbitrário de digitos significativos
"""
getcontext().prec = 60

def test_dif():
	pass

def test_find():
	pass

def Test():
	#50 digitos
	#Estimativas de erros usando valores encontrados na internet para a função
	print("Rodando Testes: ")
	j0_2 = Decimal("0.22389077914123566805182745464994862582515448221861")
	j0_37 = Decimal("0.010862369724899694740993821310850856019800294935816")
	calc_j0_2 = my_j0(2)
	calc_j0_37 = my_j0(37)
	#print("\n"*15 + "J0(2) - J0(2) Calculado: {}".format(j0_2 - calc_j0_2))
	#print("J0(37) - J0(37) Calculado: {} \n".format(j0_37 - calc_j0_37))
	#print(j0_2)
	#print(calc_j0_2)
	for i in range(len(str(j0_2))):
		if str(j0_2)[i] != str(calc_j0_2)[i]:
			print("Diferença na: {} casa decimal".format(i-2))
			break
		else:
			continue

def my_j0(x, kmax = 1337):
	J0 = Decimal(0)
	for k in range(kmax+1):
		print("Calculando J0({}): {}%".format(x,round((k*100/kmax),2)))
		J0 += Decimal(((-x**2)**k))/Decimal(((4**k)*(math.factorial(k)**2)))
	return J0

def my_j1(x, kmax = 1000):
	pass

Test()