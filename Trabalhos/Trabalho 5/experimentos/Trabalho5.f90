program trabalho
implicit none
real(kind=16) :: step = 0.0000001, res_sum, f, a, b
print *, "Digite o Limite Inferior"
read *, a
print *, "Digite o Limite Superior"
read *, b

res_sum = 0
do while (a .LE. b)
f = a
a = a + step
res_sum = res_sum + f
end do
res_sum = res_sum * step
print *, res_sum


end program trabalho