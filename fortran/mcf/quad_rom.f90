!**************************** SUBROTINA QUAD_ROM ****************************
! Calcula a quadratura numérica de uma função f(x) usando o Método de Romberg.
! Argumentos:
!   f: Função na forma f(x) a ser integrada            (Entrada).
!   a: Limite inferior de integração                   (Entrada).
!   b: Limite superior de integração                   (Entrada).
!   errrel: Valor máximo admitido para o erro relativo (Entrada).
!   reslt: Valor obtido para a quadratura numérica     (Saida).
!   errest: Valor estimado para o erro relativo        (Saida).
! Autor: Rudi Gaelzer, IF-UFRGS.
! Data: Maio/2008.
subroutine quad_rom(f, a, b, errrel, reslt, errest)
use Metodos_Computacionais_Fisica, only: dp, zero, one, three, four, &
                                         fabst, trapez_rom
implicit none
real(dp), intent(in)  :: a, b, errrel
real(dp), intent(out) :: reslt, errest
procedure(fabst)      :: f
integer  :: k, i, np
real(dp) :: quatroi, quatroim1, errabs
real(dp), dimension(:), allocatable :: Ikm1, Ik, temp1, temp2
if(b == a)then
   reslt= zero ; errest= zero
   return
end if
np= 100
allocate(Ikm1(0:np), Ik(0:np))
Ik(0)= trapez_rom(f, a, b, 0)
Ikm1(0)= trapez_rom(f, a, b, 1)
Ikm1(1)= (four*Ikm1(0) - Ik(0))/three
k= 2
do
   if(k > np)then !Dobrar a alocação atual dos vetores
      allocate(temp1(0:2*np), temp2(0:2*np))
      temp1(0:np)= Ikm1
      temp2(0:np)= Ik
      call move_alloc(temp1,Ikm1)
      call move_alloc(temp2,Ik)
      np= 2*np
   end if
! Realiza laços ao longo das diagonais.
   Ik(0)= trapez_rom(f, a, b, k)
   quatroi= one
   do i= 1, k
      quatroi= four*quatroi
      quatroim1= quatroi - one
      Ik(i)= (quatroi*Ik(i-1) - Ikm1(i-1))/quatroim1
   end do
! Calcula e compara erro
   errabs= (Ik(k-1) - Ikm1(k-1))/quatroim1
   errest= abs(errabs/Ik(k))
   if(errest <= errrel)then
      reslt= Ik(k)
      exit
   else
      k= k + 1
      Ikm1= Ik
   end if
end do
return
end subroutine quad_rom
