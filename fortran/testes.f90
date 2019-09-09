program test
implicit none !sempre bom começar adicionando isso
integer, parameter :: v = 2 !inicializando uma constante 'v', inteira
!quando tem 'parameter' é uma constante.
print *, "Número inteiro: ",v
real :: c = 5.31254 !inicializando uma variável 'c' real
print *, "Número real: ",c
complex, parameter :: d = (5,-5) ! constante 'd' complexa
!fortran é um tanto ruim para lidar com strings
character(len=*), parameter :: tanto = 'Bem doido' !o len=* assume o tamanho d a string declarada
print *, tanto
print *, "Terminou a parte de declaração de coisas"
print *, "Començando parte de ifs and whatnots..."
!adicionar aqui, cansei kkkkk
end program test
