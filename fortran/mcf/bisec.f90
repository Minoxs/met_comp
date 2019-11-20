!**************************** SUBROTINA BISEC ****************************
! Busca uma raiz da função F(X) pelo Método da Bisecção.
! Argumentos:
!   F: Nome da função cuja raiz é desejada                    (Entrada).
!   A,B: Pontos extremos do intervalo onde a raiz é procurada (Entrada).
!   XTOL: Tolerância máxima para a aproximação da raiz        (Entrada).
!   XM: Melhor resultado obtido para a raiz de F(X)           (Saida).
!   IFLAG: Um inteiro:                                        (Saida).
!         = -1, Método falhou, uma vez que F tem o mesmo sinal em A e B.
!         =  0, Encerrou, uma vez que ABS(A-B)/2 <= XTOL.
!         =  1, Encerrou, uma vez que ABS(A-B)/2 é tao pequeno que
!                 novos valores para a raiz não são possíveis.
! Autor: Rudi Gaelzer, IF-UFRGS
! Data: Maio/2008.
subroutine bisec (f, a, b, xtol, xm, iflag)
use Metodos_Computacionais_Fisica, only: dp, zero, half, fabst
implicit none
integer, intent(out)    :: iflag
real(dp), intent(inout) :: a, b
real(dp), intent(in)    :: xtol
real(dp), intent(out)   :: xm
procedure(fabst)        :: f
real(dp) :: erro,fa,fm
iflag= 0
fa= f(a)
if (fa*f(b) > zero) then
  iflag= -1
  print'(a,2(x,e15.7))', 'f(x) tem o mesmo sinal nos dois pontos extremos:', &
                         a , b
  return
end if
erro= abs(b - a)
do  ! Execute enquanto erro > xtol.
   erro= half*erro
   if (erro <= xtol) exit
   xm= half*(a + b)
   if (xm + erro == xm) then ! Teste para tolerância muito pequena.
      iflag= 1
      return
   end if
   fm= f(xm)
   if (fa*fm > zero) then ! Determine novo intervalo.
      a= xm
      fa= fm
   else
      b= xm
   end if
end do
end subroutine bisec
