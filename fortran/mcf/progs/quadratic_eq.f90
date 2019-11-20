!*************************** PROGRAMA QUADRATIC_EQ ***************************
! Calcula as raízes da equação quadrática
!       @\color{orange}{$a x^2 + b x + c = 0$}@
! Para o caso de coeficientes reais (precisão dupla).
!
! Autor: Rudi Gaelzer, IF-UFRGS
! Data: Agosto/2019.
!
program quadratic_eq
use Metodos_Computacionais_Fisica, only: dp, zero, half, one, four
implicit none
real(dp) :: a, b, c, disc, qr, x1, x2
complex(dp) :: qc, z1, z2

print*, 'Entre com os coeficientes da equação:'
write(*, fmt= '(a)', advance= 'no')'a= ' ; read*, a
write(*, fmt= '(a)', advance= 'no')'b= ' ; read*, b
write(*, fmt= '(a)', advance= 'no')'c= ' ; read*, c
disc= b*b - four*a*c
print*, 'As raízes são:'
if(disc >= zero)then ! Raízes reais.
   qr= -half*(b + sign(one, b)*sqrt(disc))
   x1= qr/a ; x2= c/qr
   print'(2(a,g0))', 'x1= ', x1, '  x2= ', x2
else
   qc= -half*(b + sqrt(cmplx(disc, kind= dp)))
   z1= qc/a ; z2= c/qc
   print'(2(a,g0),a)', 'z1= (', real(z1,dp), ',', aimag(z1),')'
   print'(2(a,g0),a)', 'z2= (', real(z2,dp), ',', aimag(z2),')'
end if
end program quadratic_eq
