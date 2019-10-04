import random
class Object:
	n = 0
	name = "Null"
	def __init__(self,num): #Função __init__ é rodada sempre que um objeto da classe é inicializado (criado).
		self.name = "OBJETO NÚMERO " + str(num) #Vai self. antes do nome da variável, 
		self.n = random.randint(1,100)			# 		pois está mudando a variável do PRÓPRIO objeto.
		print("Initialized") #Para demonstrar que esse bloco de código está sendo rodado, isso sera printado.

lista = []
for i in range(3):
	lista.append(Object(i)) #Adiciona 3 objetos da clase 'Object' para o array 'lista'.
					#como a função __init__ do object necessita uma variável num, ela deve ser adicionada
					#ao inicializar o objeto. Nesse caso é o i.	

print(lista) #Os objetos guardados na lista não são "legíveis", veja o terminal para ver o output.

for k in lista: #Para imprimir os detalhes da classe, usa-se esse for.
	print(k.name)
	print(k.n)

#
print(lista[0].name)
lista[0].n = 20 #Modificando uma variável do objeto
print(lista[0].n)
#

a = input("Press ENTER to close.") #Para que o programa não feche imediatamente após terminar.