! Calcula a derivada numérica de uma função analítica pelo 
!  Método da Extrapolação de Richardson.
! Argumentos:
! f: Função externa a ser derivada                          (entrada).
! x: Ponto onde calcular a derivada                         (entrada).
! h_ini: Valor inicial para o intervalo de diferença finita (entrada).
! errest: Valor máximo solicitado para o erro relativo      (entrada).
! dfdx:   Valor da derivada numérica                        (saida).
! err_sai: Valor estimado do erro relativo da derivada      (saida).
! Obs.: Caso parâmetro errest seja menor que a estimativa de
!       erro relativo mínimo para o método, a rotina interrompe
!       automaticamente o processamento.
subroutine dfdx_rich(f, x, h_ini, errest, dfdx, err_sai)
use Metodos_Computacionais_Fisica, only: dp, half, three, fabst
implicit none
real(dp), intent(in)  :: x, h_ini, errest
real(dp), intent(out) :: dfdx, err_sai
procedure(fabst) :: f
! Variáveis locais
integer        :: i
real(dp), parameter :: errrel_min= 3.0e-13_dp
real(dp) :: h, df1, df2, err_abs

if(errest <= errrel_min)then
   print'("O erro relativo solicitado é muito pequeno."     ,/, &
          "Erros de arredondamento irão impedir que a rotina",/, & 
          " atinja a precisão solicitada.")'
   STOP
end if
h= h_ini
df1= df_cent(x, h)
do
   df2= df_cent(x, half*h)
   err_abs= (df2 - df1)/three
   dfdx= df2 + err_abs
   err_sai= abs(err_abs/dfdx)
   if(err_sai <= errest)exit
   df1= df2
   h= half*h
end do
return
CONTAINS
   function df_cent(x, h)
   real(dp)             :: df_cent
   real(dp), intent(in) :: x, h
   df_cent= half*(f(x+h) - f(x-h))/h
   return
   end function df_cent
end subroutine dfdx_rich
