!***************************** SUBROTINA RK4 *******************************
! Resolve um Problema de Valor Inicial pelo Método de Runge-Kutta 
!   de quarta ordem com passo fixo.
! Dados o vetor y(:) que contém as variáveis e o vetor das derivadas
!   dydx(:) no ponto x, a rotina invoca a subrotina derivs(y,x,dydx)
!   que será usada para avançar o vetor das soluções ysai(:) até o
!   ponto x + h.
! Argumentos de entrada:
!   x:      Ponto inicial do intervalo.
!   y:      Vetor de forma assumida contendo as soluções do PVI no ponto x. 
!   h:      Tamanho do passo.
!   derivs: Subrotina que calcula as derivadas dydx no ponto x.
! Argumento de saída:
!   ysai: Vetor de forma assumida contendo as soluções do PVI no ponto x + h.
!         O vetor ysai pode ser o próprio vetor y.
! Autor: Rudi Gaelzer, IF-UFRGS.
! Data: Julho/2010.
! (Obs: Baseada na subrotina RK4 do Numerical Recipes).
subroutine rk4(x, y, h, ysai, derivs)
use Metodos_Computacionais_Fisica, only: dp, half, two, six, &
                                         vfdfabst, verifica_tamanhos
implicit none
real(dp), intent(in)                :: x, h
real(dp), dimension(:), intent(in)  :: y
real(dp), dimension(:), intent(out) :: ysai
procedure(vfdfabst)                  :: derivs
real(dp) :: h6, hh, xh
real(dp), dimension(size(y)) :: dydx, dym, dyt, yt
call verifica_tamanhos([size(y),size(ysai)], 'rk4')
hh= h*half ; h6= h/six
call derivs(x,y,dydx)
xh= x + hh
yt= y + hh*dydx
call derivs(xh,yt,dyt)
yt= y + hh*dyt
call derivs(xh,yt,dym)
yt= y + h*dym
dym= dyt + dym
call derivs(x+h,yt,dyt)
ysai= y + h6*(dydx + dyt + two*dym)
return
end subroutine rk4
