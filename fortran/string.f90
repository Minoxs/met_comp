program caracteres
implicit none
character, parameter :: cl = 'v'
character(len=*), parameter :: tda = 'Tromba d"água'
character(len=15) :: str_read
print *, 'imprimindo strings na tela'
print *, 'Constante cl: ->|', cl, '<-'
print *, 'Constante tda: ', tda,'<-'
print*, "entre com texto (sem aspas ou apóstrofes):"
read '(a)', str_read
print *, "Texto lido: ", str_read,'<-'
end program caracteres
