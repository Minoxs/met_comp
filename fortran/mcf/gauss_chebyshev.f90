!************************** FUNÇÃO Gauss_Chebyshev **************************
! Implementa a fórmula de Gauss-Chebyshev para uma integral definida de 
!   limites arbitrários.
! Argumentos:
!   f: Função a ser integrada (integrando menos função peso).
!   x1: Limite inferior de integração.
!   x2: Limite superior de integração.
!   n: Número de pontos usados na quadratura gaussiana (n > 1).
! Autor: Rudi Gaelzer, IF-UFRGS.
! Data: Maio/2008.
function gauss_chebyshev(f, x1, x2, n)
use Metodos_Computacionais_Fisica, only: dp, zero, half, pi, fabst
real(dp)             :: gauss_chebyshev
integer, intent(in)  :: n
real(dp), intent(in) :: x1, x2
procedure(fabst)     :: f
integer  :: j
real(dp) :: x_menos, x_mais, y, xj, wj
x_menos= half*(x2 - x1)
x_mais=  half*(x1 + x2)
wj= pi/real(n,dp)
gauss_chebyshev= zero
do j= 1, n
   xj= cos((j - half)*pi/real(n,dp))
   y= x_menos*xj + x_mais
   gauss_chebyshev= gauss_chebyshev + wj*f(y)
end do
return
end function gauss_chebyshev
