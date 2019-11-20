!********************** SUBROTINA VERIFICA_TAMANHOS ***********************
! Verifica se componentes inteiros de um vetor sao todos iguais.
! Caso contrario, o processamento para com mensagem de erro.
! Autor: Rudi Gaelzer, IF-UFRGS.
! Data: Julho/2009.
module procedure verifica_tamanhos
integer, dimension(size(vint) - 1) :: vdif
integer :: i
do i= 1, size(vint) - 1
   vdif(i)= vint(i) - vint(i + 1)
end do
if(any(vdif /= 0))then
   write (*,*) 'Pelo menos uma verificacao de tamanho falhou em:', string
   stop 'Programa interrompido por VERIFICA_TAMANHOS.'
end if
return
end procedure verifica_tamanhos
