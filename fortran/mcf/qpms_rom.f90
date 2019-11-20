!**************************** SUBROTINA QPMS_ROM ****************************
! Calcula a quadratura numerica de uma funcao f(x) usando o Metodo de Romberg.
! A funcao pode conter singularidades integraveis nos limites de integracao.
! Argumentos:
!   f: Funcao na forma f(x) a ser integrada            (Entrada)
!   a: Limite inferior de integracao                   (Entrada)
!   b: Limite superior de integracao                   (Entrada)
!   errrel: Valor maximo admitido para o erro relativo (Entrada)
!   reslt: Valor obtido para a quadratura numerica     (Saida)
!   errest: Valor estimado para o erro relativo        (Saida)
! Rotinas usadas: pntmed_rom.
! Autor: Rudi Gaelzer, IF-UFRGS.
! Data: Junho/2010.
subroutine qpms_rom(f, a, b, errrel, reslt, errest)
use Metodos_Computacionais_Fisica, only: dp, zero, one, eight, nine, &
                                         fabst, pntmed_rom
implicit none
real(dp), intent(in ) :: a, b, errrel
real(dp), intent(out) :: reslt, errest
procedure(fabst)      :: f
integer  :: k, i, np
real(dp) :: novei, noveim1, errabs
real(dp), dimension(:), allocatable :: Ikm1, Ik, temp1, temp2
if(b == a)then
   reslt= zero
   errest= zero
   return
end if
np= 200
allocate(Ikm1(0:np), Ik(0:np))
Ik(0)= pntmed_rom(f, a, b, 0)
Ikm1(0)= pntmed_rom(f, a, b, 1)
Ikm1(1)= (nine*Ikm1(0) - Ik(0))/eight
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
   Ik(0)= pntmed_rom(f, a, b, k)
   novei= one
   do i= 1, k
      novei= nine*novei
      noveim1= novei - one
      Ik(i)= (novei*Ik(i-1) - Ikm1(i-1))/noveim1
   end do
! Calcula e compara erro
   errabs= (Ik(k-1) - Ikm1(k-1))/noveim1
   if(abs(errabs) <= errrel*abs(ik(k-1)))then
      reslt= Ik(k)
      exit
   else
      k= k + 1
      Ikm1= Ik
   end if
end do
return
end subroutine qpms_rom
