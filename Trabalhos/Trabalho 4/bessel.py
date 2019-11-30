#!/usr/bin/env python3
from matplotlib import pyplot as plib
import math
from decimal import *
"""
Estou usando a biblioteca decimal para ter um numero arbitrário de digitos significativos
"""
getcontext().prec = 70

def Test(x_conhecido,res_conhecido):
	if type(res_conhecido) is not str and type(res_conhecido) is not Decimal:
		print("Para evitar erros de float, o resultado de res_conhecido deve ser do tipo string ou decimal.")
		return 0
	print("Rodando Teste: ")
	res_calculado = my_j0(x_conhecido)
	dif = Decimal(res_conhecido) - res_calculado
	for i in range(len(res_conhecido)):
		if  res_conhecido[i] != str(res_calculado)[i] or i+1 == len(res_conhecido) or i+1 == len(str(res_calculado)):
			if i <= 2:
				msg = "Diferença no índice: {}".format(i)
			else:
				msg = "Diferença na: {} casa decimal (Índice: {})".format(i-1,i)
			break
		else:
			continue
	test_result = """
=====J0({0})===============================================================
J0({0}) - J0_Calculado({0}) = {1}
J0({0})           = {2}
J0_Calculado({0}) = {3}
{4}
===========================================================================
		""".format(x_conhecido,dif,res_conhecido,res_calculado,msg)
	return test_result

def my_j0(x, kmax = 2000):
	J0 = Decimal(0)
	for k in range(kmax+1):
		print("Calculando J0({}): {}%".format(x,round((k*100/kmax),2)))
		J0 += Decimal(((-x**2)**k))/Decimal(((4**k)*(math.factorial(k)**2)))
	return J0

def my_j1(x, kmax = 1000):
	pass

default_test1 = Test(2,"0.22389077914123566805182745464994862582515448221861")
default_test2 = Test(37,"0.010862369724899694740993821310850856019800294935816")
print(default_test1)
print(default_test2)