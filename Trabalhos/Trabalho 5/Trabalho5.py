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

def f(F,x): #Calcula F(x) qualquer
	global pi, e
	F = F.replace("^","**").replace(",",".") #usa a notação de python, por isso '^' (denotando exponente) é mudado para '**', e vírgulas viram pontos.
	try:
		return eval(F)
	except TypeError: #Caso tenha um float na F(x), calcula-se usando x como um float (invés de 'Decimal')
		x = float(x)
		return eval(F)
	except NameError: #Geralmente ocorre quando há alguma variável indefinida, ex: y, dx, etc.
		print("Erro ao Interpretar Função.")
		return 0

def roots(F,a,b): #Função que calcula as raizes de F entre a e b. (Funciona melhor para pequenos intervalos de a e b)
	a = Decimal(a)
	b = Decimal(b)
	if a == b:
		print("a deve ser diferente de b")
		return 0
	elif f(F,a) == 0: #se um dos pontos extremos estiver sobre uma raiz, retorna a raiz do ponto extremo.
		return [a,0]
	elif f(F,b) == 0:
		return [b,0]
	elif f(F,a) > f(F,b): #Caso a função seja decrescente entre a e b, inverte a e b para que o algoritmo funcione normalmente.
		temp = [a]
		a = b
		b = temp[0]
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
	a = Decimal(a) #Muito útil para funções complicadas com vários 0s entre a e b.
	b = Decimal(b)
	step = Decimal("0.001") #Conforme testei, fatias de tamanho 0,001 é o suficiente para a maioria das funções,
	a_list=[]				#até as mais complicadas, sem prejudicar tanto o tempo de cálculo
	b_list=[]
	Lock = False
	while a <= b:
		left = f(F,a)
		right = f(F,a+step)
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
	return [a_list,b_list]

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

sen = sin

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

def bessel(x, n = 100):
	F = "cos(Decimal({})*sin(x))".format(x)
	res = trapez(F,0,pi,n)
	return [res[0] * (1/Decimal(pi)),res[1]]

def trapez(F,a,b,n):
	start = time.time()
	a = Decimal(a)
	b = Decimal(b)
	n = int(n)
	step = (b-a)/n
	res_sum = 0
	while a <= b:
		fx = f(F,a)
		a += step
		res_sum += fx
	end = time.time()
	return [res_sum*step,end-start]


print(cortes("x**2",-1,1))
print("Digite o número do comando")
while True:
	break
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
			n = input("Digeite o número de pontos à ser usado na quadratura\nn: ")
			try:
				a = Decimal(a)
				b = Decimal(b)
				n = Decimal(n)
			except:
				print("Valores numéricos de 'a,b ou n' não reconhecidos")
				continue
			if a == b:
				print("'a' igual a 'b'")
				print("Integral de {} = 0".format(F))
				Run = False
				break
			while n <= 0:
				print("n deve ser >= 0")
				n = input("Digeite o número de pontos à ser usado na quadratura\nn: ")
			Run = True
			break
		if Run == True:
			integral = trapez(F,a,b,n)
			print("Resultado da Integral: {} \nTempo de Cálculo: {}".format(round(integral[0],5),round(integral[1],3)))	
	elif com == "2":
		pass
	elif com == "3":
		pass