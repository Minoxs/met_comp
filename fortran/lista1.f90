program lista1
implicit none
integer :: a, b, c, d
character(len=*), parameter :: UFRGS = 'Universidade Federal do Rio Grande do Sul'
real :: f, o, l, m, h, ra
character(len=8) :: R 
real :: pi = 3.1415
a = 13
b = 12
c = a/b
a = a*c
d = a*b/(c+a)
print *, "Valores de a, b, c, d"
print *, a, b, c, d
print *, UFRGS
print *, "Digite um número: "
read *, f
print *, "Raiz Quadrada de ",f," é igual à ",f**(1./2.)
print *, "Digite um número real: "
read *, o
print *, "Raiz Cúbica de ",o," é igual à ",o**(1./3.)
print *, "Escolha dois números reais: "
read *, l, m
print*, real(l)/real(m)
R = 'ABCDEFGH'
print *, R
R = 'ABCD'//'01234'
print *, R
R(:7) = "ABCDEFHG"
print *, R
R(:6) = "ABCD"
print *, R
print *, "Escolha valores para L, B, H, r, respectivamente:"
read *, L, B, H, ra
print *, "Perímeto do quadrado de lado ",L," ",L*4
print *, "Área de um Triângulo de base ",B," e altura ",H," ",(B*H)/2
print *, "Volume de uma esfera de raio ",ra," ",4*pi*(ra**2)
end program lista1