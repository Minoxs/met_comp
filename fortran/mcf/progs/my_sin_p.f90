!*************************** PROGRAMA MY_SIN ***************************
! Calcula uma aproximação para a função sen(x)
!
! Autor: Rudi Gaelzer, IF-UFRGS
! Data: Setembro/2019.
!
program my_sin_p
use Metodos_Computacionais_Fisica, only: dp, zero, one, two
implicit none
real(dp) :: x
do
   write(*,'(a)',advance='no')'x= ' ; read*, x
   print'(a,g0)', 'my_sin(x)= ', my_sin(x)
   print'(a,g0)', 'F_sin(x)=  ', sin(x)
end do
CONTAINS
   function my_sin(x)
   real(dp) :: my_sin
   real(dp), intent(in) :: x
   real(dp), parameter :: tol= epsilon(one)
   real(dp) :: x2
   real(dp), dimension(2) :: f2np1
   real(dp), dimension(0:2) :: vs, vt
   x2= x*x
   vt= [ one, -x2/6.0_dp, zero ]
   vs= [ one, one + vt(1), zero ]
   f2np1= [ 5.0_dp, 4.0_dp ]
   do ! Inicia laço a partir do termo n = 2
      vt(2)= -vt(1)*x2/product(f2np1)
      vs(2)= vs(1) + vt(2)
      if(all(abs(vt) <= tol*abs(vs)))exit
      f2np1= f2np1 + two
      vt= eoshift(vt, 1) ; vs= eoshift(vs, 1) ! vs(1) -> vs(0), vs(2) -> vs(1)
   end do
   my_sin= x*vs(2)
   return
   end function my_sin
end program my_sin_p
