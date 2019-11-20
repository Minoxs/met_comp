!**************************** SUBROTINA QPMI_ROM ****************************
! Calcula a quadratura numérica de uma função f(x) usando o Método de Romberg
!    no intervalo de integração [a,Infinito).
! O integrando não possui pontos singulares no intervalo de integração.
! Argumentos:
!   f: Função na forma f(x) a ser integrada            (Entrada).
!   a: Limite inferior de integração                   (Entrada).
!   errrel: Valor máximo admitido para o erro relativo (Entrada).
!   reslt: Valor obtido para a quadratura numérica    (Saida).
!   errest: Valor estimado para o erro relativo        (Saida).
! Rotinas usadas: pntmed_inf_rom.
! Autor: Rudi Gaelzer, IF-UFRGS.
! Data: Junho/2010.
subroutine qpmi_rom(f, a, errrel, reslt, errest)
use Metodos_Computacionais_Fisica, only: dp, one, eight, nine, &
                                         fabst, pntmed_inf_rom
implicit none
real(dp), intent(in)  :: a, errrel
real(dp), intent(out) :: reslt, errest
procedure(fabst)      :: f
integer  :: k, i, np
real(dp) :: novei, noveim1, errabs
real(dp), dimension(:), allocatable :: Ikm1, Ik, temp1, temp2
np= 200
allocate(Ikm1(0:np), Ik(0:np))
Ik(0)= pntmed_inf_rom(f, a, 0)
Ikm1(0)= pntmed_inf_rom(f, a, 1)
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
   Ik(0)= pntmed_inf_rom(f, a, k)
   novei= one
   do i= 1, k
      novei= nine*novei
      noveim1= novei - one
      Ik(i)= (novei*Ik(i-1) - Ikm1(i-1))/noveim1
   end do
! Calcula e compara erro
   errabs= (Ik(k-1) - Ikm1(k-1))/noveim1
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
end subroutine qpmi_rom
