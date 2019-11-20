!**************************** FUNÇÃO PNTMED_ROM ****************************
! Calcula a quadratura numérica de uma função f(x) pela regra dos pontos
!   médios estendida.
! Criada como parte integrante do Metodo de Romberg para integração 
!   automática.
! Argumentos:
! f:    Função na forma f(x) a ser integrada (Entrada)
! a:    Limite inferior de integração        (Entrada)
! b:    Limite superior de integração        (Entrada)
! n_ordem: Ordem de chamada da função        (Entrada)
! Autor: Rudi Gaelzer, IF-UFRGS
! Data: Junho/2010.
function pntmed_rom(f, a, b, n_ordem)
use Metodos_Computacionais_Fisica, only: dp, half, two, three, six, fabst
implicit none
real(dp)             :: pntmed_rom
integer, intent(in)  :: n_ordem
real(dp), intent(in) :: a, b
procedure(fabst)     :: f
integer        :: i, npts
real(dp)       :: h, del
real(dp), save :: I_pme
real(dp), dimension(2*(3**(n_ordem-1))) :: x, f_eval
h= b - a
select case(n_ordem) ! Testa primeira rodada.
case(0)      ! Primeira rodada.
   I_pme= h*f(half*(a+b))
case default ! Rodadas subsequentes.
   npts= 3**(n_ordem - 1)
   del= h/(six*npts)
   forall(i= 1:npts)
      x(2*i-1)= a + (6*i-5)*del
      x(2*i)=   a + (6*i-1)*del
   end forall
   forall(i= 1:2*npts)
      f_eval(i)= f(x(i))
   end forall
I_pme= two*del*sum(f_eval) + I_pme/three
end select
pntmed_rom= I_pme
return
end function pntmed_rom
