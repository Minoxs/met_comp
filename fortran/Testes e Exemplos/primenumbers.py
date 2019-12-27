import time

lim1 = 0
prob = 0
cursize = 2
primes = [2,3]

while lim1 < 3:
	print("How far to look for primes:")
	com = input()
	lim1 = int(com)

start_time = round(time.time(),2)

for check in range(4,lim1+1):
	if check%2 == 0:
		continue
	prob = 0
	for prime in primes:
		if check%prime == 0:
			break
		else:
			prob += 1
	if prob == cursize:
		primes.append(check)
		cursize += 1

end_time = round(time.time(),2)

done = end_time - start_time

print(primes)
print(done)