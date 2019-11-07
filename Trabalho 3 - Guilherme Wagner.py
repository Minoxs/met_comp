#------------------------- <Python 3.5.9> <Script> ------------------------
# Referência: Trabalho 3 - Solução de uma equação cúbica
# Nome(s): Guilherme Wagner Correa (00303992)
# Data: 06/11/2019
# Objetivo: Achar as raízes de uma equação cúbica qualquer.
#--------------------------------------------------------------------------
import math
pi = 3.141592653589793
############################################
inp = 0
index = 0
coef = []
while len(coef) < 4:
	inp = input("Escolha um valor para a({}).".format(index)) #Pegando os valores dos coeficientes, até a(3).
	try:
		inp = float(inp)
		coef.append(inp)
		index += 1
	except:
		print("Número não detectado.")
############################################
coef.reverse()
powe = len(coef)-1
f = ""
for i in range(len(coef)):
	if i == len(coef)-2:
		f += "{}x + ".format(coef[i])		# Esta parte serve apenas para printar um polinônio de grau n
		continue
	elif i == len(coef)-1:
		f += str(coef[i])
		continue
	f += "{}x^({}) + ".format(coef[i],powe)
	powe += -1
f += " = 0"
print(f)
coef.reverse()
############################################
a = coef[2]/coef[3]
b = coef[1]/coef[3]
c = coef[0]/coef[3]
print("a = {}, b = {}, c = {}".format(a,b,c)) # Essa parte calcula os primeiros parâmetros de teste.
q = ((a**2) - (3*b))/9
r = ((2*a**3)-(9*a*b)+(27*c))/54
print("q = {}, r = {} -- q³ = {}, r² = {}".format(q,r,q**3,r**2))
############################################
if q**3 > r**2:
	theta = math.acos(r/math.sqrt(q**3))
	x1 = -2*math.sqrt(q)*math.cos(theta/3)-a/3
	x2 = -2*math.sqrt(q)*math.cos((theta + 2*pi)/3)-a/3 # caso q³ > r² seja satisfeito, calcula as 3 raízes reais
	x3 = -2*math.sqrt(q)*math.cos((theta - 2*pi)/3)-a/3
	x1 = round(x1,2)
	x2 = round(x2,2)
	x3 = round(x3,2)
############################################
else:
	p = -1*math.copysign(1,r) * (abs(r)+math.sqrt((r ** 2 - q ** 3))) ** (1/3)
	if p == 0:
		s = 0
	else:
		s = q/p
	print("p = {}, s = {}".format(p,s)) # Caso a condição acima não seja satisfeita, calcula 1 raiz real e 2 complexas
	x1 = p + s - (a/3)
	x1 = round(x1,2)
	rx2 = -(1/2)*(p+s)-(a/3)
	ix2 = (math.sqrt(3)/2)*(p-s)            # é possível que a parte imaginária seja igual a 0 (ex: x2 = 1 + 0i)
	x2 = complex(round(rx2,2),round(ix2,2)) # isso acontece sempre que a função tenha apenas 1 raiz real, e 0 complexa
	rx3 = -(1/2)*(p+s)-(a/3)                # ou apenas 2 raízes reais e nenhuma complexa. Como estou apenas seguindo
	ix3 = -(math.sqrt(3)/2)*(p-s)           # o algorítmo, vou manter a forma "c + 0i" quando aparecer.
	x3 = complex(round(rx3,2),round(ix3,2))
############################################
# Todos os resultados foram arredondados para 2 casas decimais, assim evitando erros de float.
print("As Raizes são: x1 = {}, x2 = {}, x3 = {}".format(x1,x2,x3))
hold = input()