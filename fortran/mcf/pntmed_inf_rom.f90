!*************************** FUNCAO PNTMED_INF_ROM ***************************
! Calcula a quadratura numerica de uma funcao f(x) pela regra dos pontos
!   medios estendida.
! Criada como parte integrante do Metodo de Romberg para a integracao 
!   automatica de uma funcao no intervalo [a,Infinito).
! Argumentos:
! f:    Funcao na forma f(x) a ser integrada (Entrada).
! a:    Limite inferior de integracao        (Entrada).
! n_ordem: Ordem de chamada da funcao        (Entrada).
! Autor: Rudi Gaelzer, IF-UFRGS.
! Data: Junho/2010.
function pntmed_inf_rom(f, a, n_ordem)
use Metodos_Computacionais_Fisica, only: dp, half, one, two, three, six, fabst
implicit none
real(dp)             :: pntmed_inf_rom
integer, intent(in)  :: n_ordem
real(dp), intent(in) :: a
procedure(fabst)     :: f
integer  :: i, npts
real(dp) :: h, del
real(dp), save :: I_pme
real(dp), dimension(2*(3**(n_ordem-1))) :: x, f_eval
h= one/(one + a)
select case(n_ordem) ! Testa primeira rodada.
case(0)      ! Primeira rodada.
   I_pme= h*func(half*h)
case default ! Rodadas subsequentes.
   npts= 3**(n_ordem - 1)
   del= h/(six*npts)
   forall(i= 1:npts)
      x(2*i-1)= (6*i-5)*del
      x(2*i)=   (6*i-1)*del
   end forall
   forall(i= 1:2*npts)
      f_eval(i)= func(x(i))
   end forall
I_pme= two*del*sum(f_eval) + I_pme/three
end select
pntmed_inf_rom= I_pme
return
CONTAINS
   pure function func(x)
   real(dp) :: func
   real(dp), intent(in) :: x
   func= f(one/x - one)/(x*x)
   return
   end function func
end function pntmed_inf_rom
