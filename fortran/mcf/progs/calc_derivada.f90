! Calcula derivada da função sin(x**2) usando extrapolação de Richardson
! Autor: Rudi Gaelzer, IF-UFRGS
! Data: Novembro/2019
program calc_derivada
use Metodos_Computacionais_Fisica, only: dp, zero, one, two, dfdx_rich
implicit none
integer :: npts, i
real(dp), parameter :: hi= 1.0e-2_dp
real(dp) :: xf, dx, tol, der, errr, ff, dff, errc
real(dp) :: x= 1.0e-2_dp, mee= -one, mer= -one
write(*, '(a)', advance= 'no')'x(final)= ' ; read*, xf
write(*, '(a)', advance= 'no')'Nº pontos= ' ; read*, npts
write(*, '(a)', advance= 'no')'Tolerância= ' ; read*, tol
open(unit= 10, file= 'dsenx2.csv')
dx= (xf - x)/(npts - 1)
do i= 1, npts
   call dfdx_rich(senx2, x, hi, tol, der, errr)
   ff= senx2(x) ; dff= dsenx2(x)
   errc= abs(one - der/dff)
   write(10, '(6(g13.6,:,","))')x, ff, der, dff, errr, errc
   if(errr > mee)mee= errr
   if(errc > mer)mer= errc
   x= x + dx
end do
print'(/,a,g0)','Maior erro estimado: ', mee
print'(a,g0)',  'Maior erro real:     ', mer
CONTAINS
   pure function senx2(x)
   real(dp) :: senx2
   real(dp), intent(in) :: x
   senx2= sin(x*x)
   return
   end function senx2
!***
   function dsenx2(x)
   real(dp) :: dsenx2
   real(dp), intent(in) :: x
   dsenx2= two*x*cos(x*x)
   return
   end function dsenx2
end program calc_derivada
