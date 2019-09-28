program zeta
implicit none

integer :: s, cur, n
real(kind=16) :: sum, piece

print *, "Choose 's' for zeta(s)"
read *, s
print *, "Choose 'n' for how far to calculate"
read *, n

sum = 0
do cur=1,n
piece = 1./(real(cur)**s) 
sum = sum + piece
enddo

end program zeta