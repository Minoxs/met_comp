#!/usr/bin/env python3
from matplotlib import pyplot as plib #Para produzir os gráficos
import math #Apenas para a função fatorial(usada em J0)
from decimal import * #Estou usando a biblioteca decimal para ter um numero arbitrário de digitos significativos
import time #Usado para capturar o tempo decorrido entre cálculos
import csv #Para lidar com as tabelas e gráficos
from pathlib import Path as find #Usado para encontrar e salvar o arquivo

getcontext().prec = 1000 #Quantidade de casas decimais dos objetos decimais; Para maiores valores de X, esse valor precisa ser aumentado.

####Funções de Teste###############################################################################################################
def Test(x_conhecido,resj0_conhecido,resj1_conhecido): #Função para testar as funções de bessel com valores conhecidos
	for i in [resj0_conhecido,resj1_conhecido]:
		if type(i) is not str and type(i) is not Decimal:
			print("Para evitar erros de float, o resultado de {} deve ser do tipo string ou decimal.".format(i))
			return 0 #Para o teste não dar resultados errados, usa-se um tipo de dado com menor perda de informação
	print("Rodando Teste: ")
	resj0_calculado = my_j0(x_conhecido)
	#difj0 = Decimal(resj0_conhecido) - resj0_calculado
	resj1_calculado = my_j1(x_conhecido,resj0_calculado)
	#difj1 = Decimal(resj1_conhecido) - resj1_calculado
	msg = []
	for t in [[resj0_conhecido,resj0_calculado],[resj1_conhecido,resj1_calculado]]:
		for i in range(len(t[0])):
			if  t[0][i] != str(t[1])[i] or i+1 == len(t[0]) or i+1 == len(str(t[1])):
				msg.append("Diferença no índice: {}".format(i))
				break
	test_result = """
=====J0({0})===============================================================
J0({0})           = {1}
J0_Calculado({0}) = {2}
{3}
===========================================================================
=====J1({0})===============================================================
J1({0})           = {5}
J1_Calculado({0}) = {6}
{7}
===========================================================================
Precisão Configurada: {4} casas decimais
===========================================================================
		""".format(x_conhecido,resj0_conhecido,str(resj0_calculado)[:60],msg[0],getcontext().prec,resj1_conhecido,str(resj1_calculado)[:60],msg[1])
	return test_result

def default_tests(): #Roda 3 testes usando valores que encontrei na internet
	start_time = Decimal(time.time())
	default_test1 = Test(2,"0.22389077914123566805182745464994862582515448221861","-0.57672480775687338720244824226913708692030268971968")
	default_test2 = Test(37,"0.010862369724899694740993821310850856019800294935816","0.13058003873375645502815126677389762266272038575475")
	default_test3 = Test(100,"0.019985850304223122424228390950848990680633578859028","0.077145352014112158032685494927234470211611667099243")
	end_time = Decimal(time.time())
	print(default_test1)
	print(default_test2)
	print(default_test3)
	print("Tempo decorrido: {}s".format(round(end_time-start_time,5)))
###############################################################################################################

def my_j0(x): #Função de Bessel J0
	kmax = 300
	J0 = Decimal(0)
	x = Decimal(x)
	if x == 0:
		return Decimal(1)
	for k in range(kmax+1):
		print("Calculando J0({}): {}%".format(x,round((k*100/kmax),2)))
		J0 += Decimal(((-x**2)**k))/Decimal(((4**k)*(math.factorial(k)**2)))
	return J0

def my_j1(x,calculado = "n"): #Função de Bessel J1, caso já tenha J0 calculado, usa-se o argumento 'calculado' para diminuir o tempo de cálculo
	x = Decimal(x)
	dx = Decimal("0.00000000000000000000000000000000000000000000001")
	if calculado == "n":
		dy = my_j0(x+dx) - my_j0(x)
	else:
		dy = my_j0(x+dx) - calculado
	return (dy/dx)

def tabelar(xi,xf):
	start_time = time.time()
	prim = xi
	o = open("PLOT_DATA_{}_{}.csv".format(xi,xf),"w+")
	o.write("X,J0,J1 \n")
	o.close()
	t = open("Tabela_J0_{}_{}.csv".format(prim,xf),"w+")
	t.write("x,J0,J1 \n")
	t.close()
	while xi <= xf:
		calc_j0 = my_j0(xi)
		calc_j1 = my_j1(xi,calc_j0)
		o = open("PLOT_DATA_{}_{}.csv".format(prim,xf),"a+") #Esse arquivo contém mais dígitos significativos; para ser usado no gráfico
		o.write("{},{},{} \n".format(xi,calc_j0,calc_j1))	 #Imprático de ser lido
		o.close()
		t = open("Tabela_J0_{}_{}.csv".format(prim,xf),"a+") 				 #Esse arquivo contém ~58 casas decimais
		t.write("{},{},{} \n".format(xi,str(calc_j0)[:60],str(calc_j1)[:60]))#Melhor de ser lido
		t.close()
		xi += Decimal("0.1")
	end_time = time.time()
	print("Pronto! Tempo decorrido: {}".format(end_time-start_time))
	return end_time-start_time

def pdfplot(graf):
	o = open(graf,"r")
	graf = list(csv.reader(o,delimiter=","))
	o.close()
	x  = [Decimal(graf[i][0]) for i in range(1,len(graf))]
	j0 = [Decimal(graf[i][1]) for i in range(1,len(graf))]
	j1 = [Decimal(graf[i][2]) for i in range(1,len(graf))]
	plib.plot(x,j0)
	plib.plot(x,j1)
	plib.savefig('Plot_{}_{}.pdf'.format(x[0],x[-1]))

####################################################################################
#times = []
#for i in range(1,101):
#	times.append(tabelar(0,i))
#plib.plot(list(range(1,101)),times)
#plib.savefig("timetaken.pdf")
#tabelar(-100,100)
#grafplot()
tabelar(-5,5)
pdfplot("Tabela_J0_-5_5.csv")