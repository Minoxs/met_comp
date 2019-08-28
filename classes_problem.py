import random
class Object:
	n = 0
	name = "Null"
	def __init__(self,num):
		self.name = "OBJETO NÚMERO " + str(num)
		self.n = random.randint(1,100)
		print("Initialized")

list = []
for i in range(3):
	list.append(Object(i))
	
print(list)

for k in list:
	print(k.name)
	print(k.n)
