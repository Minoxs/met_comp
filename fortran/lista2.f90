program lista2
implicit none

integer, dimension(:), allocatable :: array
integer(kind=16) :: next
integer :: com, even, odd, fst, snd, thd, fth, xaxis, yaxis, lim1, one, two, n, cur, val
integer :: pick, tl, tr, size, test, cursize, start, end, cur2, prob
real :: pi = 3.1415926535897932384626433832795028841971693993751
real :: a, b, c, a1, b1, c1, raiz1, raiz2, delta, V, Z, theta, I, P, Q, S, F, n1, n2, theta1, theta2, left, X, Y
real :: tstart, tend

com = 1
do while (com .GT. 0)
!Escolhendo o exercício
print *, "Escolha o exercício. (Digite 0 para sair)"
read *, com

if (com .LE. 0) then
exit
endif
!
!
if (com .EQ. 1) then
print *, "Escolha 2 Valores:"
read *, a, b

if (a .GT. b .OR. a .EQ. b) then
c = a
endif

if (b .GT. a) then
c = b

endif
print *, "Bigger Value:",c
!
!
else if (com .EQ. 2) then
print *,"Escolha 3 Valores"
read *, a1, b1, c1
print *, "Polinômio:",a1,"x²+",b1,"x",c1

if (a1 .NE. 0) then
delta = sqrt((b1**2)-(4*a1*c1))
raiz1 = (-b1+delta)/(2*a1)
raiz2 = (-b1-delta)/(2*a1)
print *, "Raizes:",raiz1,raiz2

else
print *, "Não é um Polinômio de segundo grau."
endif
!
!
else if (com .EQ. 3) then
print *, "Escolha Valores para V, Z e theta(em graus), respectivamente"
read *, V, Z, theta
theta = theta*(pi/180)
if (Z .NE. 0) then
I = V/Z
P = V*I*cos(theta)
Q = V*I*sin(theta)
S = V*I
F = cos(theta)
print *, "I, P, Q, S, F, respectivamente."
print *, I, P, Q, S, F

else
print *, "Circuito Impossível."
endif
!
!
else if(com .EQ. 4) then
print *, "Escolha índices de refração n1, n2, e theta1(em graus), respectivamente."
read *, n1,n2,theta1
theta1 = theta1*(pi/180)
if (n1 .LT. 1 .OR. n2 .LT. 1) then
print *, "Parabéns! Você estragou a física. (n1 ou n2 não podem ser < 1)"

else
left = n1*sin(theta1)
theta2 = ASIN((left/n2))
theta2 =  theta2*(180/pi)
print *, "Refraction Angle:",theta2
endif
!
!
else if(com .EQ. 5) then
even = 0
odd = 0
do while (i >= 0)
print *, "Insira um numero positivo. Para terminar, insitra um número negativo."
read *, i

if (i .LT. 0) then
exit

else if (MOD(i,2.) .EQ. 0.) then
even = even + 1 

else if(MOD(i,2.) .EQ. 1.) then
odd = odd + 1
endif

enddo
print *, even,"pares e",odd,"ímpares"
!
!
else if(com .EQ. 6) then
fst = 0
snd = 0
thd = 0
fth = 0
xaxis = 0
yaxis = 0
x = 1
y = 1
do while(x .NE. 0 .OR. y .NE. 0)
print *, "Escolha valores para (x, y),respectivamente."
read *, x,y

if (x .EQ. 0 .AND. y .EQ. 0) then
exit

else if (x .EQ. 0) then
xaxis = xaxis + 1

else if (y .EQ. 0) then
yaxis = yaxis + 1

else if (x .GT. 0 .AND. y .GT. 0) then
fst = fst + 1

else if (x .LT. 0 .AND. Y .GT. 0) then
snd = snd + 1

else if (x .LT. 0 .AND. Y .LT. 0) then
thd = thd + 1

else if (x .GT. 0 .AND. Y .LT. 0) then
fth = fth + 1

endif
enddo
print *, "Pares Ordenados em: Primeiro qd, Segundo qd, Terceiro qd, Quarto qd, X axis and Y axis, respectivamente"
print *, "            ",fst,snd,thd,fth,xaxis,yaxis
!
!
else if (com .EQ. 7) then
x = 0
do while(x .NE. -1)
print *, "Escolha um valor para X"
read *, x

if (x .EQ. -1) then
print *, "x = -1 não é válido"
x = 0
cycle
endif

print *, (x/(1+x))
exit
enddo
!
!
else if (com .EQ. 8) then
print *, "Escolha o índice limite da sequência"
read *, lim1

if (lim1 .LE. 2) then
print *, "Valor limite inválido"
exit
endif

fst = 1
snd = 1
x = 3
next = 0

print *, 1
print *, 1

do while(x .LE. lim1)
next = fst + snd
print *, next
fst = snd
snd = next
x = x + 1
enddo
!
!
else if (com .EQ. 9) then
lim1 = 0

do while (lim1 .LE. 0)
print *, "Escolha a linha limite do triângulo. (Número inteiro maior que 0)"
print *, "O programa sempre vai ir até uma linha par, pois eu sou preguiçoso"
read *, lim1
enddo

if (MOD(lim1,2) .EQ. 1) then
lim1 = lim1 + 1
endif

val = (lim1+1)*(lim1/2)

allocate(array(val))

n = 1
cur = 1
pick = 1
do while (n .LE. lim1)

if (cur .EQ. 1) then
array(pick) = 1
cur = cur + 1
pick = pick + 1
endif

do while (cur .LT. n)
tl = array(pick-n)
tr = array(pick+1-n)
array(pick) = (tl+tr)
cur = cur + 1
pick = pick + 1
enddo

if (cur .EQ. n) then
array(pick) = 1
cur = cur + 1
pick = pick + 1
endif

cur = 1
n = n + 1
enddo

fth = 1
fst = 1
thd = 1
do even = 1, n-1
print *, array(fst:thd) !Esse bloco é para printar o triangulo
fst = thd + 1
thd = thd + fth + 1
fth = fth + 1
enddo

deallocate(array) !Desalocar o array para que possa ser reutilizado sem reiniciar o programa e salvar memória
!
!
else if (com .EQ. 10) then
lim1 = 0
size = 0
prob = 0
cursize = 2
cur = 3
do while (lim1 .LE. 3)
print *, "Insira um número inteiro maior que 3"
read *, lim1
enddo

if (MOD(lim1,2) .EQ. 1) then
size = (lim1+1)/2
else
size = lim1/2
endif

allocate(array(size))
array(1) = 2
array(2) = 3
call cpu_time(tstart)
do test=4,lim1

if (MOD(test,2) .EQ. 0) then
cycle
endif

	prob = 0
	do start = 1, cursize
		if (MOD(test,array(start)) .EQ. 0) then
			exit
		else
			prob = prob + 1
		endif
	enddo

if (prob .EQ. cursize) then
array(cur) = test
cursize = cursize + 1
cur = cur + 1
endif
enddo

do test = 1, cursize
if (array(test) .EQ. 0) then
exit
endif
print *, array(test)
enddo
call cpu_time(tend)
print '("Time = ",f6.3," seconds.")',tend-tstart
deallocate(array)

else
print *, com,"não corresponde à um exercício da lista 2."
endif
enddo
print *, "Terminando programa..."
end program lista2