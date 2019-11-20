!*************************** SUBROTINA FAL_POS_MOD ***************************
! Busca uma raiz da função F(X) pelo Método da Falsa Posição Modificado.
!****** Argumentos de entrada ******
! F: Nome da função cuja raiz é desejada
! A,B: Pontos extremos do intervalo onde a raiz é procurada.
! XTOL: Tolerância máxima para o intervalo que contém a raiz.
! FTOL: Tolerância máxima para o valor absoluto de F(W).
! NTOL: Número máximo de iterações admitidas (opcional).
!       Se NTOL está ausente, permite infinitas iterações.
!****** Argumentos de saída ******
! A,B: Pontos extremos do intervalo que contém a matriz.
! W:  Melhor estimativa para a raiz.
! IFLAG: Um inteiro,
!      =-1, Método falhou, uma vez que F(x) tem o mesmo sinal em A e B.
!      = 0, Encerrou, porque ABS(A-B) <= XTOL.
!      = 1, Encerrou, porque ABS(F(W)) <= FTOL.
!      = 2, Encerrou, porque NTOL iterações foram realizadas.  
!****** Método ******
! O método da falsa posição modificado é empregado.  Isto significa que
!   a cada passo, interpolação linear entre os pontos (A,FA) e
!   (B ,FB) é empregada, com FA*FB < 0, para um novo ponto (W,F(W))
!   que substitui um dos pontos A ou B de tal forma que novamente FA*FB < 0.
!   Adicionalmente, a ordenada de um ponto que é repetido em mais de uma 
!   iteração é dividida por 2 a cada passo subsequente.
! Autor: Rudi Gaelzer, IF-UFRGS
! Data: Junho/2008.
subroutine fal_pos_mod(f, a, b, xtol, ftol, w, iflag, ntol)
use Metodos_Computacionais_Fisica, only: dp, zero, half, one, fabst
implicit none
integer, intent(in), optional :: ntol
integer, intent(out)          :: iflag
real(dp), intent(inout)       :: a, b
real(dp), intent(in)          :: xtol, ftol
real(dp), intent(out)         :: w
procedure(fabst)              :: f
integer  :: n
real(dp) :: fa, fb, fw, signfa, prvsfw
fa= f(a) ; fb= f(b) ; signfa= sign(one, fa)
if (signfa*fb > zero) then
   print'(a,2(x,e15.7))','f(x) tem o mesmo sinal nos dois pontos extremos:', &
                         a, b
   iflag= -1
   return
end if
w= a ; fw= fa ; n= 1
do
   if (abs(a-b) <= xtol) then   ! Verifica se intervalo é menor que xtol.
      iflag= 0
      return
   end if
   if (abs(fw) <= ftol) then    ! Verifica se ABS(f(w)) é menor que ftol.
      iflag= 1
      return
   end if
   w= (fa*b - fb*a)/(fa - fb)  ! Calcula novo w por interpolação.
   prvsfw= sign(one,fw)
   fw= f(w)
   if (signfa*fw > zero) then ! Altera o intervalo.
      a= w ; fa= fw
      if (fw*prvsfw > zero) fb= half*fb
   else
      b= w ; fb= fw
      if (fw*prvsfw > zero) fa= half*fa
   end if
   if(present(ntol) .and. (n >= ntol))then
      print'("Não houve convergência em ", i5, " iterações.")',ntol
      iflag= 2
      return
   end if
   n= n + 1
end do
return
end subroutine fal_pos_mod
