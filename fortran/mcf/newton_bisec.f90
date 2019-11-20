!*************************** SUBROTINA NEWTON_BISEC ***************************
! Busca uma raiz da função F(X) atraves de uma combinação dos métodos de
!   Newton-Raphson e da bisecção.
!****** Argumentos de entrada ******
! F_DFDX: Nome da subrotina que retorna os valores de F(X) e F'(X).
! x1,x2: Dois valores iniciais para o início da iteração.
! ERRABS: Primeiro critério de parada.  Se ABS(F(Xn)) <= FTOL,
!         então Xn é aceito como raiz
! ERRREL: Segundo critério de parada: erro relativo.
!         Se ABS(Xn - Xn-1) <= XTOL*ABS(Xn), então Xn é aceito como raiz.
! NTOL: Numero máximo de iterações admitidas.
!****** Argumentos de saída ******
! RAIZ:  Melhor estimativa para a raiz.
! IFLAG: Um inteiro,
!      = -2, Método falhou.  Não existe raiz em [x1,x2].
!      = -1, Método falhou.  Nenhuma raiz foi encontrada em NTOL
!            iterações.  O último valor encontrado para X é retornado.
!      = 0,  Encerrou devido ao primeiro critério de parada ou por novas
!            iterações não alterarem o resultado.
!      = 1,  Encerrou devido ao segundo critério de parada.
! Autor: Rudi Gaelzer, IF-UFRGS.
! Data: Junho/2008.
! (Baseado na função rtsafe do Numerical Recipes).
subroutine newton_bisec(f_dfdx, x1, x2, errabs, errrel, ntol, raiz, iflag)
use Metodos_Computacionais_Fisica, only: dp, zero, half, two, fdfabst
implicit none
integer, intent(in)   :: ntol
integer, intent(out)  :: iflag
real(dp), intent(in)  :: x1, x2, errabs, errrel
real(dp), intent(out) :: raiz
procedure(fdfabst)    :: f_dfdx
integer  :: j
real(dp) :: df, dx, dxold, f, fh, fl, temp, xh, xl
call f_dfdx(x1, fl, df)
call f_dfdx(x2, fh, df)
if (fl*fh > zero)then
   iflag= -2
   return
end if
if (fl == zero) then
   raiz= x1
   iflag= 0
   return
else if (fh == zero) then
   raiz= x2
   iflag= 0
   return
else if (fl < zero) then ! Oriente o intervalo tal que f(x1) < 0.
   xl= x1 ; xh= x2
else
   xh= x1 ; xl= x2
end if
raiz= half*(x1 + x2)
dxold= abs(x2 - x1)
dx= dxold
call f_dfdx(raiz, f, df)
do j= 1, ntol                   ! Laço sobre o número permitido de iterações.
   if (((raiz-xh)*df-f)*((raiz-xl)*df-f) >= zero & ! Se a iteração estiver
       .or. abs(two*f) > abs(dxold*df) ) then      ! fora de [x1,x2],
      dxold= dx                                    ! ou se não estiver
      dx= half*(xh - xl)                           ! convergindo rapidamente,
      raiz= xl + dx                                ! use bisecção.
      if (xl == raiz) then
         iflag= 0
         return
      end if
   else  ! Iteração está dentro de [x1, x2].
      dxold= dx
      dx= f/df
      temp= raiz
      raiz= raiz - dx
      if (temp == raiz) then
         iflag= 0
         return
      end if
   end if
   call f_dfdx(raiz, f, df)
   if(abs(f) <= errabs) then            ! Primeiro critério de parada.
      iflag= 0
      return
   end if
   if(abs(dx) <= errrel*abs(raiz)) then ! Segundo critério de parada.
      iflag= 1
      return
   end if
   if (f < zero) then
      xl=raiz
   else
      xh=raiz
   end if
end do
iflag= -1
return
end subroutine newton_bisec

