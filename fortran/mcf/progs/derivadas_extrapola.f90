program derivadas_extrapola
use Metodos_Computacionais_Fisica, only: dp, half, one, two, three
implicit none
integer :: i
real(dp) :: h= 0.1_dp          ! h inicializado a 1/10.
real(dp), parameter :: x= half ! Valor de x fixo.
real(dp) :: df1, df2, df, erro_est, fl
fl= two*x*cos(x*x) ! Valor correto da derivada em x.
open(unit= 10,file= 'derivs_ext.dat')
do i= 1, 45
   df1= fp3(x, h)  ! Derivada diferença centrada
   df2= fp3(x, half*h)
   erro_est= (df2 - df1)/three
   df= df2 + erro_est
   print *, one/h, abs(erro_est), abs(df2 - fl), abs(df - fl)
   h= half*h       ! h é dividido por 2.
end do
CONTAINS
   function f(x)
   real(dp) :: f
   real(dp), intent(in) :: x
   f= sin(x*x)
   return
   end function f
!***
   function fp3(x,h)
   real(dp) :: fp3
   real(dp), intent(in) :: x,h
   fp3= half*(f(x+h) - f(x-h))/h
   return
   end function fp3
end program derivadas_extrapola
