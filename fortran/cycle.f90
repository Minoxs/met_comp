program do_cycle
implicit none
integer :: indic=0
do
    indic = indic + 1
    if(indic == 100) print *, "INDICE 100"
    if(indic == 100) print *, "DENOVOOOO"
    if(mod(indic,2) == 0) cycle
    if(indic == 101) exit
    print *, "Valor do índice:",indic
end do
print *, "Saiu do laço. Fim do programa."
end program do_cycle
