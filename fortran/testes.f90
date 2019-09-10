program test
!MUITO IMPORTANTE: DECLARÇÕES DE VARIÁVEIS APENAS ANTES DE EXECUTÁVEIS.
implicit none !sempre bom começar adicionando isso
integer, parameter :: v = 2 !inicializando uma constante 'v', inteira
real :: c = 5.31254 !inicializando uma variável 'c' real
complex, parameter :: d = (5,-5) ! constante 'd' complexa
!quando tem 'parameter' é uma constante.
character(len=*), parameter :: tanto = 'Bem doido' !o len=* assume o tamanho d a string declarada
print *, "Número inteiro: ",v
print *, "Número real: ",c
!fortran é um tanto ruim para lidar com strings
print *, tanto
print *, "Terminou a parte de declaração de coisas"
print *, "Començando parte de ifs and whatnots..."
end program test
