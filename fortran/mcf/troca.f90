module procedure troca
real(dp) :: mudo
mudo= a
a= b
b= mudo
return
end procedure troca
