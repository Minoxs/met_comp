!****************************** FUNÇÃO SIMPSON *****************************
! Calcula a quadratura numérica de uma função f(x) pela regra de Simpson
!   estendida.
! Argumentos:
! f:  Função na forma f(x) a ser integrada    (Entrada).
! a:  Limite inferior de integração           (Entrada).
! b:  Limite superior de integração           (Entrada).
! n:  Número de subintervalos (deve ser par)  (Entrada).
! Autor: Rudi Gaelzer, IF-UFRGS.
! Data: Maio/2011.
module procedure simpson
integer  :: i
real(dp) :: h, x
h= (b - a)/real(n, kind= dp)
x= a + h
simpson= zero
do i= 1, n - 1, 2
   simpson= simpson + two*f(x) + f(x + h)
   x= x + two*h
end do
simpson= h*(two*simpson + f(a) - f(b))/three
return
end procedure simpson
