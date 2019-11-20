program conversor 
implicit none
integer, parameter :: base= 2
integer :: i, j, qn, rn, num, num_abs
real, parameter :: log2= 0.69314718055994530942
integer, DIMENSION(:), ALLOCATABLE :: b
!
write(*,fmt= '(a)',advance= 'no')'Número na base 10: '
read*, num
select case (num)
case (0)
allocate(b(1))
   b= 0
case (:-1)
!
!Neste caso, o vetor irá alocar um digito a mais e atribuir o valor 1 
! ao último dígito, como convenção para sinal negativo.
!
   num_abs= abs(num)
   j= log(real(num_abs))/log2
   allocate(b(0:j + 1))
   qn= num_abs
   do i= 0, j
      rn= mod(qn,base)
      qn= qn/base
      b(j - i + 1)= rn
   end do
   b(0)= 1
case(1:)
   j= log(real(num))/log2
   allocate(b(0:j))
   qn= num
   do i= 0, j
      rn= mod(qn,base)
      qn= qn/base
      b(j - i)= rn
   end do
end select
j= size(b)
write(*, fmt= '("A forma binaria é: ")', advance= 'no')
do i= 1, j - 1
   write(*,fmt= '(i1)', advance= 'no')b(i - 1)
end do
write(*,fmt= '(i1)')b(j - 1)
end program conversor
