!**************************** FUNCAO TRAPEZ_ROM ****************************
! Calcula a quadratura numérica de uma função f(x) pela regra dos trapézios
!   estendida.
! Criada como parte integrante do Método de Romberg para integração 
!   automática.
! Argumentos:
! f:    Função na forma f(x) a ser integrada (Entrada).
! a:    Limite inferior de integração        (Entrada).
! b:    Limite superior de integração        (Entrada).
! n_ordem: Ordem de chamada da função        (Entrada).
! Autor: Rudi Gaelzer, IF-UFRGS.
! Data: Maio/2008.
function trapez_rom(f, a, b, n_ordem)
use Metodos_Computacionais_Fisica, only: dp, zero, half, one, two, fabst
implicit none
real(dp)             :: trapez_rom
integer, intent(in)  :: n_ordem
real(dp), intent(in) :: a, b
procedure(fabst)     :: f
integer        :: i
integer, save  :: npts
real(dp)       :: h, delta, x, soma
real(dp), save :: I_te, fat2
h= b - a
! Testa primeira rodada.
select case(n_ordem)
case(0)      ! Primeira rodada.
   I_te= half*h*(f(a) + f(b))
   fat2= one
   npts= 1
case default ! Rodadas subsequentes.
   delta= h/fat2
   x= a + half*delta
   soma= zero
   do i= 1, npts
      soma= soma + f(x)
      x= x + delta
   end do
   I_te= half*(I_te + h*soma/fat2)
   fat2= two*fat2
   npts= 2*npts
end select
trapez_rom= I_te
return
end function trapez_rom
