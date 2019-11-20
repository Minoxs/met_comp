!****************************** FUNCAO TRAPEZ *****************************
! Calcula a quadratura numérica de uma função f(x) pela regra trapezoidal
!   estendida.
! Argumentos:
! f:  Função na forma f(x) a ser integrada (Entrada).
! a:  Limite inferior de integração        (Entrada).
! b:  Limite superior de integração        (Entrada).
! n:  Número de subintervalos              (Entrada).
! Autor: Rudi Gaelzer, IF-UFRGS.
! Data: Maio/2011.
module procedure trapez
integer  :: i
real(dp) :: h, x
h= (b - a)/real(n, kind= dp)
x= a + h
trapez= zero
do i= 1, n - 1
   trapez= trapez + f(x)
   x= x + h
end do
trapez= half*h*(two*trapez + f(a) + f(b))
return
end procedure trapez
