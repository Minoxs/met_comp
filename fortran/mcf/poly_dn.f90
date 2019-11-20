!***************************** SUBROTINA POLY_DN *****************************
! Calcula o polynômio P_N(x) e suas nd primeiras derivadas.
! Método: algoritmo de Horner.
!
! Argumentos:
!   c:  Vetor de forma [0:N] com os coeficientes.                  (Entrada)
!   x:  Argumento do polinômio.                                    (Entrada)
!   pd: Vetor de forma [0:nd] contendo P_N(x) e suas nd derivadas. (Saída)
!
! Autor: Rudi Gaelzer, IF-UFRGS.
! Data: Setembro/2019.
! Obs: baseado na rotina ddpoly do Numerical Recipes.
subroutine poly_dn(c, x, pd)
use Metodos_Computacionais_Fisica, only: dp, zero, one
implicit none
real(dp), intent(in) :: x
real(dp), intent(in), dimension(0:) :: c
real(dp), intent(out), dimension(0:) :: pd
integer :: i, j, nc, nd
real(dp) :: co
nc= size(c) - 1 ; nd= size(pd) - 1
pd(0)= c(nc) ; pd(1:nd)= zero
do i= nc - 1, 0, -1
   do j= min(nd, nc - i), 1, -1
      pd(j)= pd(j)*x + pd(j - 1)
   end do
   pd(0)= pd(0)*x + c(i)
end do
co= one
do i= 2, nd ! Correção para derivadas de ordem nd > 1.
   co= co*i
   pd(i)= co*pd(i)
end do
return
end subroutine poly_dn
