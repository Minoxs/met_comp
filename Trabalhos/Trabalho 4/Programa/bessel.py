#!/usr/bin/env python3
from matplotlib import pyplot as plib #Para produzir os gráficos
from matplotlib import ticker #Para modificar os 'ticks' dos gráficos
from math import factorial #Apenas para a função fatorial(usada em J0)
from decimal import * #Estou usando a biblioteca decimal para ter um numero arbitrário de digitos significativos
import time #Usado para capturar o tempo decorrido entre cálculos
import csv #Para lidar com as tabelas e gráficos
from pathlib import Path as find #Usado para encontrar a pasta atual


#######Variáveis Globais##################################################
#Ambas afetam precisão; getcontext().prec afeta menos o tempo de cálculo do que kmax
#AS VARIÁVEIS GLOBAIS FORAM TROCADAS POR VARIÁVEIS DINÂMICAS
#getcontext().prec = 2000 #Quantidade de casas decimais dos objetos decimais; Para valores de x > 100, esse valor precisa ser aumentado.
#kmax = 3000 #kmax é o k máximo das somas de J0(x) - (Foi substituído por um valor dinâmico)
##########################################################################


####Funções de Teste###############################################################################################################
def Test(x_conhecido,resj0_conhecido,resj1_conhecido): #Função para testar as funções de bessel com valores conhecidos
	for i in [resj0_conhecido,resj1_conhecido]:
		if type(i) is not str and type(i) is not Decimal:
			print("Para evitar erros de float, o resultado de {} deve ser do tipo string ou decimal.".format(i))
			return 0 #Para o teste não dar resultados errados, usa-se um tipo de dado com menor perda de informação
	print("Rodando Teste: ")
	resj0_calculado = my_j0(x_conhecido)
	resj1_calculado = my_j1(x_conhecido,resj0_calculado)
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
		""".format(x_conhecido,resj0_conhecido,round(resj0_calculado,60),msg[0],getcontext().prec,resj1_conhecido,round(resj1_calculado,60),msg[1])
	return test_result

def default_tests(): #Roda 5 testes usando valores que encontrei na internet
	start_time = Decimal(time.time())
	default_test1 = Test(2,"0.22389077914123566805182745464994862582515448221861","0.57672480775687338720244824226913708692030268971968")
	default_test2 = Test(100,"0.019985850304223122424228390950848990680633578859028","-0.077145352014112158032685494927234470211611667099243")
	default_test3 = Test(249,"-0.05054361019992152349247603013408618460724935701513987722","-0.00153126021193784447519403077306501550646690195666120635")
	default_test4 = Test(499,"-0.0095930996349789212572774511326990627036914753655901","0.034396260940337637501321797778376299069817169182645")
	default_test5 = Test(500,"-0.03410055688073199826512506045189455813144279153168387048","0.010472613470372292844467094756967054578966611894700673094")
	default_test6 = Test(699,"0.021436359010795065183459364123769093585704041673003443121","0.021257753656885555591464165457600932132078055405985654930")
	default_test7 = Test(1000,"0.024786686152420174561330731115693708786166447133246548414","0.004728311907089523917576071901216916285418024202059636868")
	end_time = Decimal(time.time())
	o = open("log_teste.txt","a+")
	for save in [default_test1,default_test2,default_test3,default_test4,default_test5,default_test6,default_test7]:
		print(save)
		o.write("{}\n".format(save))
	o.write("Tempo Decorrido: {}s\n".format(round(end_time-start_time,5)))
	o.close()
	print("Tempo decorrido: {}s".format(round(end_time-start_time,5)))
###############################################################################################################
#Aqui começa a parte principal do script
#getcontext().prec é a quantidade de casas decimais precisas de objetos decimais, quanto mais casas, menor o erro de arredondamento.
def my_j0(x): #Função de Bessel J0
	if abs(x) >= 700:
		getcontext().prec = 1500
		kmax = 3000
	elif abs(x) >= 500:
		getcontext().prec = 1500
		kmax = 1500
	elif abs(x) >= 250:
		getcontext().prec = 1000
		kmax = 1000
	elif abs(x) >= 100:
		getcontext().prec = 750
		kmax = 500
	else:
		getcontext().prec = 500
		kmax = 300
	J0 = Decimal(0)
	x = Decimal(x)
	if x == 0:
		return Decimal(1)
	for k in range(kmax+1):
		if k%50 == 0:
			print("Calculando J0({}): {}%".format(x,round((k*100/kmax),2)))
		J0 += Decimal(((-x**2)**k))/Decimal(((4**k)*(factorial(k)**2)))
	return J0

def my_j1(x,calculado = "n"): #Função de Bessel J1, caso já tenha J0 calculado, usa-se o argumento 'calculado' para diminuir o tempo de cálculo
	x = Decimal(x)
	dx = Decimal("0.00000000000000000000000000000000000000000000001")
	if calculado == "n":
		dy = my_j0(x+dx) - my_j0(x)
	else:
		dy = my_j0(x+dx) - calculado
	return (-dy/dx)

def plotconfig(): #Essa função acompanha saveplot() para configurá-la com parâmetros dados via input do usuário
	while 1 != 0:
		print("Digite o tamanho (em cm) do gráfico: \n(Deixe em Branco para ser do tamanho A4)")
		
		inp = input("Digite a largura \n")
		if inp.strip() == "":
			inp = "29.7"
		
		inp2 = input("Digite a altura \n")
		if inp2.strip() == "":
			inp2 = "21.0"
		
		try:
			lar = Decimal(inp)/Decimal(2.54)
			alt = Decimal(inp2)/Decimal(2.54)
			lar = float(round(lar,4))
			alt = float(round(alt,4))
			break
		except:
			print("Erro ao interpretar input.")
			continue
	
	while 1 != 0:
		print("Escolha o espaçamento da escala no eixo x \n(Deixe em branco para ser [0,5,10,15,...])")
		inp = input("Digite um número inteiro \n")
		if inp.strip() == "":
			scl = 5
			break
		try:
			scl = int(inp)
			break
		except:
			print("Erro ao interpretar input. (Deve ser um número inteiro)")
			continue
	return [lar,alt,scl]

def saveplot(graf): #Função que plota os dados de (x,J0,J1), graf é um arquivo .csv, resultado em .svg e .pdf
	o = open(graf,"r")
	graf = list(csv.reader(o,delimiter=","))
	o.close()
	x  = [Decimal(graf[i][0]) for i in range(1,len(graf))]
	j0 = [Decimal(graf[i][1]) for i in range(1,len(graf))]
	j1 = [Decimal(graf[i][2]) for i in range(1,len(graf))]
	config = plotconfig()
	plib.figure(figsize=(config[0],config[1]))
	ax = plib.axes()
	plib.xlim(int(x[0]),int(x[-1]))
	ax.xaxis.set_major_locator(ticker.MultipleLocator(config[2]))
	ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
	ax.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
	ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.01))
	plib.grid(b=True)
	plib.plot(x,j0)
	plib.plot(x,j1)
	plib.title("Função de Bessel de {} até {}".format(float(round(x[0],2)),float(round(x[-1],2))))
	plib.ylabel("y")
	plib.xlabel("x")
	plib.legend(["J0(x)","J1(x)"])
	plib.savefig('Plot_{}_{}.pdf'.format(int(x[0]),int(x[-1])),bbox_inches='tight',pad_inches=0.25)
	plib.savefig('Plot_{}_{}.svg'.format(int(x[0]),int(x[-1])),bbox_inches='tight',pad_inches=0.25)
	print("Plot_{0}_{1}.pdf\nPlot_{0}_{1}.svg\nSalvos em: {2}\n".format(int(x[0]),int(x[-1]),find.cwd()))
	return "sucesso"

def tabelar(xi,xf): #Essa função tabela os pontos x, J0(x), e J1(x) entre (xi,xf) [com xf incluso]
	start_time = time.time()
	prim = xi
	o = open("PLOT_DATA_{}_{}.csv".format(xi,xf),"w+")
	o.write("X,J0,J1 \n")
	o.close()
	t = open("Tabela_{}_{}.csv".format(prim,xf),"w+")
	t.write("x,J0,J1 \n")
	t.close()
	while xi <= xf:
		calc_j0 = my_j0(xi)
		calc_j1 = my_j1(xi,calc_j0)
		o = open("PLOT_DATA_{}_{}.csv".format(prim,xf),"a+") #Esse arquivo contém mais dígitos significativos; para ser usado no gráfico
		o.write("{},{},{} \n".format(xi,calc_j0,calc_j1))	 #Imprático de ser lido
		o.close()
		t = open("Tabela_{}_{}.csv".format(prim,xf),"a+") 				 #Esse arquivo contém ~58 casas decimais
		t.write("{},{},{} \n".format(xi,round(calc_j0,60),round(calc_j1,60)))#Melhor de ser lido
		t.close()
		xi += Decimal("0.1")
	end_time = time.time()
	print("PLOT_DATA_{1}_{2}.csv\nTabela_{1}_{2}.csv\nSalvo em: {0}\n".format(find.cwd(),prim,xf))
	print("Pronto! Tempo decorrido: {}".format(end_time-start_time))
	saveplot("PLOT_DATA_{}_{}.csv".format(prim,xf)) #Chamando função de criar o gráfico
	return "sucesso"

####################################################################################

inp = input("Rodar testes de Precisão? (y/n)\n(Leva 1-3 minutos)\n") #perguntando caso queira rodar os testes padrões
if inp.lower() == "y":
	default_tests()
	hold = input("Pressione ENTER para continuar.\n")

while 1: #Essa parte toda é responsável apenas por receber inputs do usuário.
	print("""
	\n
Digite 'calcular' ou 'c' para calcular J0(x) e J1(x) em um intervalo (Xi,Xf)
Insira 'plot' ou 'p' para gerar um gráfico à partir de uma tabela (X,J0,J1)
(Digite 'sair' para fechar o programa)
	\n
	""")

	command = input("Comando: ")

	while command.lower() == "plot" or command.lower() == "p":
		print("Digite o intervalo (Xi,Xf) salvo em arquivo para carregar.\n(Digite 'c' para cancelar)")
		inp1 = input("Xi: ")
		if inp1 == "c":
			break
		inp2 = input("Xf: ")
		try:
			saveplot("PLOT_DATA_{}_{}.csv".format(inp1,inp2))
			break
		except:
			print("Aquivo: {}/PLOT_DATA_{}_{}.csv não encontrado \n\n".format(find.cwd(),inp1,inp2))
			continue

	while command.lower() == "calcular" or command.lower() == "c":
		print("Tabelando J0(x) e J1(x) em: Xi < x < Xf")
		inp1 = input("Digite o valor de Xi\n")
		inp2 = input("Digite o valor de Xf\n")
		print("{} < x < {} INSERIDO.".format(inp1,inp2))
		if inp1 == inp2:
			print("Xi deve ser diferente de Xf")
			continue
		try:
			xi = Decimal(inp1)
			xf = Decimal(inp2)
		except:
			print("Erro ao interpretar input.")
			continue
		tabelar(xi,xf)
		ask = input("Calcular outro intervalo (y/n)\n")
		if ask.lower() == "y":
			continue
		else:
			break

	if command.lower() == 'sair' or command.lower() == 'exit':
		break
	command = "novo comando"