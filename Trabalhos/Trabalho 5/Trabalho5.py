#!/usr/bin/env python3
from decimal import *
from matplotlib import pyplot as plib
from matplotlib import ticker
import time

#Constantes
pi = Decimal("3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679")
e = Decimal("2.718281828459045235360287471352662497757247093699959574966967627724076630353547594571382178525166427427")
getcontext().prec = 250 # Precisão da biblioteca decimal.
###############

#Funções do Trabalho 5
def f(F,x): #Calcula F(x) qualquer
	global pi, e
	F = F.replace("^","**").replace(",",".") #usa a notação de python, por isso '^' (denotando exponente) é mudado para '**', e vírgulas viram pontos.
	try:
		return eval(F)
	except TypeError: #Caso tenha um float na F(x), calcula-se usando x como um float (invés de 'Decimal')
		x = float(x)
		e = float(e)
		pi = float(pi)
		return eval(F)
	except NameError: #Geralmente ocorre quando há alguma variável indefinida, ex: y, dx, etc.
		print("Erro ao Interpretar Função.")
		raise NameError
	except SyntaxError:
		print("Erro de Sintaxe! \nGaranta que as multiplicações estão explicitas. (ex: 2*x invés de 2x)")
		raise NameError

def roots(F,a,b): #Função que calcula as raizes de F entre a e b. (Funciona melhor para pequenos intervalos de a e b)
	a = Decimal(a) #Encontra apenas UMA raiz.
	b = Decimal(b)
	if f(F,a) == 0: #se um dos pontos extremos estiver sobre uma raiz, retorna a raiz do ponto extremo.
		return [a,0]
	elif f(F,b) == 0:
		return [b,0]
	elif f(F,a) > f(F,b): #Caso a função seja decrescente entre a e b, inverte a e b para que o algoritmo funcione normalmente.
		temp = a
		a = b
		b = temp
		del temp
	mid = 1
	m = 0 # 'm' é o número de iterações, normalmente, ~30 são o suficiente.
	while abs(mid) > Decimal("0.00000000001"): #A função termina quando o valor abosulo da F(b+a/2) é menor que o especificado.
		mid_point = (b+a)/2
		mid = f(F,mid_point)
		if mid < 0:
			a = mid_point
		elif mid > 0:
			b = mid_point
		m += 1
		if m >= 200: # Caso m passe de 200, geralmente ocorreu algum erro, ou não há raiz, ou não foi encontrada.
			mid_point = "Raiz não encontrada"
			mid = None
			break #Então paro a função
	return [mid_point,mid] #Retorna o ponto da raiz, e o valor de F(b+a/2), que é basicamente o erro.

def cortes(F,a,b): #Função que corta F(x) em fatias bem pequenas, para checar quantos 0s há entre a e b.
	prim = a
	a = Decimal(a) #Muito útil para funções complicadas com vários 0s entre a e b.
	b = Decimal(b)
	step = Decimal("0.005") #Conforme testei, fatias de tamanho 0,005 é o suficiente para a maioria das funções,
	a_list=[]				#até as mais complicadas, sem prejudicar tanto o tempo de cálculo
	b_list=[]
	Lock = False
	while a <= b:
		try:
			left = f(F,a)
			right = f(F,a+step)
		except InvalidOperation:
			a += step
			continue
		if Lock: #Para evitar raízes duplicadas, caso na iteração anterior, um dos pontos extremos (a ou b) tenha caído[...]
			Lock = False #em cima de uma raiz, se pula uma iteração, para não duplicar a raiz.
		elif left == 0 or right == 0: #Ponto extremo caiu sobre uma raiz
			a_list.append(a)
			b_list.append(a+step)
			Lock = True #Ativa a Lock (próxima iteração será pulada)
		elif left > 0 and right < 0 or left < 0 and right > 0:
			a_list.append(a)
			b_list.append(a+step)
		a += step
	print("Raizes de F(x) = {}, Intervalo = ({} < x < {})".format(F,prim,b))
	for i in range(len(a_list)): #Calcula o ponto onde está a raiz dos intervalos com 0 encontrados.
		raiz = roots(F,a_list[i],b_list[i])
		print("Raiz: x = {} \nErro = {}\n".format(raiz[0],round(raiz[1],10)))
	if len(a_list) == 0:
		print("Nenhuma raiz encontrada no intervalo ({} < x < {})".format(prim,b))

def cos(x): #Função que calcula cos(x) em decimal (retirada da documentação Decimal)
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

def sin(x): #Função que calcula sin(x) em decimal (retirada da documentação Decimal)
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

sen = sin #Nomeando sen(x) = sin(x)

def trapez(F,a,b,n): #F é uma função qualquer F(x), a e b números reais, onde a < b, n um número inteiro e n > 0
	start = time.time()
	a = Decimal(a)
	b = Decimal(b)
	n = int(n)
	step = (b-a)/n
	res_sum = 0
	m = 0
	while a <= b: #Calcula F(x) de a até b, onde a largura de cada fatia da F é (b-a)/n, e altura F(x).
		if m%(n/100) == 0:
			print("Integral f(x)={}, {}% calculada".format(F,round((m*100)/n,2)))
		fx = f(F,a)
		a += step
		res_sum += fx #Soma-se os resultados das F(x)
		m += 1
	end = time.time()
	if type(res_sum) is float:
		step = float(step)
	return [res_sum*step,end-start] #Por fim, multiplica a soma pela largura dos retângulos. Retorna [resultado_da_integral,tempo_de_calculo].

def bessel(x, n): #Posso reescrever J(x) como Integral(cos(ysenx)dx)[de 0, à pi] (para seguir a notação da função f(F,x))
	F = "cos(Decimal({})*sin(x))".format(x)
	res = trapez(F,0,pi,n) #Coloca o x na F, e chama trapez(F,0,pi,n)
	return [res[0] * (1/Decimal(pi)),res[1]] #Retorna o valor de J(x) e o tempo de cálculo

def tabelar(xi,xf,n): #Tabela valores de J0(x) entre xi e xf, com n pontos na formula da quadratura
	xi = Decimal(xi)
	xf = Decimal(xf)
	n  = Decimal(n)
	x_list = []
	j0 = []
	tempo = 0
	while xi <= xf:
		if xi > 0 and -xi in x_list: #J(x) é simetrica em torno de 0, logo J(-x) = J(x)
			one = time.time()		 #Portanto, posso cortar drasticamente o tempo p/ tabelar
			x_list.append(xi)		 #Quando J(-x) já foi calculada, J(x) é apenas 'copiada'
			j0.append(j0[x_list.index(-xi)])
			tempo += time.time() - one
			xi += Decimal("0.1")
		else:
			x_list.append(xi) #Quando J(-x) não foi calculada, usa-se a função bessel(x,n).
			run = bessel(xi,n)
			j0.append(run[0])
			tempo += run[1]
			xi += Decimal("0.1")
	return [x_list,j0,n,tempo] #Retorna a lista para ser usada em bessel_plot()

def bessel_plot(graf): #pega uma lista [[x0,x1,...,xn],[j00,j01,...,j0n],[N],[Tempo_de_Cálculo]] e coloca em um gráfico.
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
	print("Gráfico aberto \nFeche o gráfico para continuar.")
	plib.show()
	print("Salvos:\nPlot_{0}_{1}.pdf\nPlot_{0}_{1}.svg\n".format(int(x[0]),int(x[-1])))
	return "sucesso"

###Código da UI
print("Digite o número do comando")
while True:
	print("\n"*10)
	print("""
0 - Sair
1 - Função trapez(F,a,b,n)
2 - Cálculo da função de Bessel usando trapez
3 - Cálculo de raízes de um polinômio
		""")
	com = input("Comando: ")
	print("\n"*10)
	
	if com == "0":
		break
	
	elif com == "1":
		while True:
			
			F = input("Digite F(x)\nex: 'x^2'\nF(x): ")
			a = input("Digite o limite INFERIOR da integral\na: ")
			b = input("Digite o limite SUPERIOR da integral\nb: ")
			n = input("Digite o número de pontos à ser usado na quadratura\nn: ")
			
			try:
				a = Decimal(a)
				b = Decimal(b)
				n = int(n)
			except:
				print("Valores numéricos de 'a,b ou n' não reconhecidos")
				continue
			
			if a == b:
				print("'a' igual a 'b'")
				print("Integral de {} = 0".format(F))
				Run = False
				break
			
			elif a > b:
				print("'a' deve ser menor que 'b'")
				print("Calculando Integral de 'b' até 'a'")
				temp = a
				a = b
				b = temp
				del temp
			
			while n <= 0:
				print("n deve ser >= 0")
				n = input("Digite o número de pontos à ser usado na quadratura\nn: ")
				n = int(n)
			
			Run = True
			break
		
		while Run:
			try:
				integral = trapez(F,a,b,n)
				print("\n#####RESULTADO######")
				print("Resultado da Integral: {} \nTempo de Cálculo: {}".format(round(integral[0],10),round(integral[1],3)))	
				print("####################")		
			except NameError:
				F = input("Digite F(x)\nex: 'x^2'\nF(x): ")
				continue
			Run = False

	elif com == "2":
		while True:
			print("0 - Voltar \n1 - Calcular J0(x) \n2 - Plotar J0(x) entre xi e xf")
			inp = input("Comando: ")
			
			if inp == "0":
				break
			
			elif inp == "1":
				while True:
					x = input("Digite x para calcular J(x):\n")
					n = input("Números de ponto a ser usado no calculo da integral:\n")
					try:
						x = Decimal(x)
						n = int(n)
					except:
						print("Erro ao interpretar valores de x ou n (devem ser números)")
						continue
					if n <= 0:
						print("n deve ser inteiro e maior que 0")
						continue
					j0 = bessel(x,n)
					print("J({}) = {} \nTempo de Cálculo: {}".format(x,round(j0[0],10),round(j0[1],10)))
					break
			
			elif inp == "2":
				print("Xi deve ser menor que Xf")
				while True:
					xi = input("Digite Xi: ")
					xf = input("Digite Xf: ")
					n  = input("Números de ponto a ser usado no calculo da integral:\n")
					try:
						xi = Decimal(xi)
						xf = Decimal(xf)
						n  = int(n)
					except:
						print("Erro ao interpretar valores de xi, xf ou n (devem ser números)")
						continue
					if n <= 0:
						print("n deve ser inteiro e maior que 0")
						continue
					graf_data = tabelar(xi,xf,n)
					bessel_plot(graf_data)
					break
	
	elif com == "3":
		while True:
			print("0 - Voltar \n1 - Calcular raízes de F(x) qualquer \n2 - Encontrar raízes das funções dadas no Trabalho")
			inp = input("Comando: ")
			
			if inp == "0":
				break

			if inp == "1":
				print("'a' deve ser menor que 'b'")
				while True:
					F = input("Digite F(x): ")
					a = input("Limite INFERIOR do intervalo para procurar a raiz \na: ")
					b = input("Limite SUPERIOR do intervalo para procurar a raiz \nb: ")

					try:
						a = Decimal(a)
						b = Decimal(b)
					except:
						print("Valores numéricos de 'a,b ou n' não reconhecidos")
						continue

					if a == b:
						print("'a' deve ser menor que 'b'")

					if a > b:
						print("Calculando intervalo b < x < a")
						temp = a
						a = b
						b = temp
						del temp
					while True:
						try:
							cortes(F,a,b)
						except NameError:
							F = input("Digite F(x)\nex: 'x^2'\nF(x): ")
							continue
						break
					break

			if inp == "2":
				print("\n"*10)
				teste1 = "x - 2^(-x)"
				teste2 = "e^x - x^2 + 3*x - 2"
				teste3 = "2*x*cos(2*x)-(x+1)^2"
				cortes(teste1,0,1)
				cortes(teste2,0,1)
				cortes(teste3,-3,0)
				print("\n"*2)