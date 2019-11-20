Module M_mha
use Metodos_Computacionais_Fisica, only: dp
implicit none
real(dp), parameter :: g= 9.8_dp
real(dp) :: alfa, beta
CONTAINS
   subroutine S_mha(t, y, dydt)
   real(dp), intent(in) :: t
   real(dp), dimension(:), intent(in) :: y
   real(dp), dimension(:), intent(out) :: dydt
   dydt(1)= y(2)
   dydt(2)= -g - alfa*y(1) - sign(1.0_dp,y(2))*beta*y(2)**2
   return
   end subroutine S_mha
end module M_mha
!***
! Resolve exercício 5.1 da Apostila: Movimento Harmônico Amortecido.
program Mov_Har_Amor
use M_mha
use Metodos_Computacionais_Fisica, only: dp, zero, rk4
implicit none
integer :: npt, i
real(dp) :: t_final, dt, t= zero
real(dp), dimension(2) :: y
write(*,'(a)',advance='no')'Entre com k/m= '
read(*,*)alfa
write(*,'(a)',advance='no')'Entre com C/m= '
read(*,*)beta
write(*,*)'Entre com as condições iniciais:'
write(*,'(a)',advance='no')'y_0= '
read(*,*)y(1)
write(*,'(a)',advance='no')'v_0= '
read(*,*)y(2)
write(*,'(a)',advance='no')'Instante final= '
read(*,*)t_final
write(*,'(a)',advance='no')'# de pontos= '
read(*,*)npt
dt= t_final/real(npt - 1,dp)
open(10,file='mha_arq.dat')
write(10,'(3(e12.5,x))')t, y
do i= 1, npt
   call rk4(t, y, dt, y, S_mha)
   t= t + dt
   write(10,'(3(e12.5,x))')t, y
end do
end program Mov_Har_Amor
