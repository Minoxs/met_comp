program expo
use Metodos_Computacionais_Fisica, only: dp, one
implicit none
integer :: j, n
real(dp), dimension(2), parameter :: x= [ one, -12.0_dp ], &
               ex= [ 2.7182818284590452353602874713527_dp, &
                     6.1442123533282097586823081788055e-6_dp ]
real(dp), dimension(2) :: soma, fator
!
open(unit= 10, file= 'expo.dat')
do n= 1, 100
   soma= one
   fator= soma
   do j= 1, n
      fator= fator*x/real(j,dp)
      soma= soma + fator
   end do
   write(10, *)n, abs(soma - ex)
end do
end program expo
