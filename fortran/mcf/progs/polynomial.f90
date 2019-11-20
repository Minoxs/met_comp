program polynomial
use Metodos_Computacionais_Fisica, only: dp
implicit none
integer :: i
real(dp) :: x, dx, px
open(unit=10, file='pol.dat')
dx= 0.016_dp/real(500-1, dp)
x= 0.992_dp
do i= 1, 500
   px= x**6 - 6*x**5 + 15*x**4 - 20*x**3 + 15*x**2 - 6*x + 1.0_dp
   write(10,*)x,px,px*1.0e13_dp
   x= x + dx
end do
end program polynomial
