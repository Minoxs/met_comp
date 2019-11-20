program derivadas
use Metodos_Computacionais_Fisica, only: dp, half, one, two
implicit none
integer :: i
real(dp) :: h= 0.02_dp            ! h inicializado a 1/50.
real(dp), parameter :: x= half  ! Valor de x fixo.
real(dp) :: df1, df2, fl
!
fl= two*x*cos(x*x) ! Valor correto da derivada em x.
open(unit= 10, file= 'derivs.dat')
do i= 1, 45
   df1= (f(x+h) - f(x))/h        ! Cálculo método 1.
   df2= half*(f(x+h) - f(x-h))/h ! Cálculo método 2.
   write(10, *)one/h, abs(df1-fl), abs(df2-fl)
   h= half*h                     ! h é dividido por 2.
end do
CONTAINS
   function f(x)
   real(dp) :: f
   real(dp), intent(in) :: x
   f= sin(x*x)
   return
   end function f
end program derivadas
