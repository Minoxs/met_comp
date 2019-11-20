!*************************** SUBROTINA SECANTE ***************************
! Busca uma raiz da função F(X) pelo Método da Secante.
!****** Argumentos de entrada ******
! FUNC: Nome da função cuja raiz é desejada
! x1,x2: Dois valores iniciais para o início da iteração.
! ERRABS: Primeiro critério de parada.  Se ABS(F(Xn)) <= FTOL,
!         entao Xn é aceito como raiz
! ERRREL: Segundo critério de parada: erro relativo.
!         Se ABS(Xn - Xn-1) <= XTOL*ABS(Xn), entao Xn é aceito como raiz.
! NTOL: Numero máximo de iterações admitidas.
!****** Argumentos de saída ******
! X:  Melhor estimativa para a raiz.
! IFLAG: Um inteiro,
!      = -1, Método falhou.  Nenhuma raiz foi encontrada em NTOL
!            iterações.  O ultimo valor encontrado para X é retornado.
!      = 0,  Encerrou devido ao primeiro critério de parada.
!      = 1,  Encerrou devido ao segundo critério de parada.
! Autor: Rudi Gaelzer, IF-UFRGS.
! Data: Junho/2008.
subroutine secante(func, x1, x2, errabs, errrel, ntol, x, iflag)
use Metodos_Computacionais_Fisica, only: dp, fabst, troca
implicit none
integer, intent(in)   :: ntol
integer, intent(out)  :: iflag
real(dp), intent(in)  :: x1, x2, errabs, errrel
real(dp), intent(out) :: x
procedure(fabst)      :: func
integer  :: j
real(dp) :: dx, f, fl, xl
fl= func(x1)
f= func(x2)
if (abs(fl) < abs(f)) then ! Tome o valor inicial com o menor valor de
   x= x1 ; xl= x2          ! func(x) como aproximação inicial.
   call troca(fl,f)
else
   xl= x1 ; x= x2
end if
do j= 1, ntol
   dx= (xl-x)*f/(f-fl)
   xl= x ; fl= f
   x= x + dx
   f= func(x)
   if(abs(f) <= errabs)then
      iflag= 0
      return
   end if
   if(abs(dx) <= errrel*abs(x))then
      iflag= 1
      return
   end if
end do
iflag= -1
return
end subroutine secante
