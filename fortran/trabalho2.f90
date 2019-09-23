program trabalho2
implicit none

integer :: com !Variável de comando
integer :: pri, seg, ter, qua, xaxis, yaxis !Variáveis exercício 1
real :: input1, input2 !Variáveis de input
character(len=3) :: ninput !Número que será digitado pelo usuário no Exercício 2
character(len=12) :: result !Número romano convertido, Exercício 2

print *, "1 - Pontos no Plano Cartesiano"
print *, "2 - Coversão Decimal-Romana"

com = 1 
do while (com .GT. 0) !Escolhendo qual parte do código rodar.
print *, "Digite o número do exercício. (Digite 0 para sair)"
read *, com

!
if (com .LE. 0) then
exit !Medida de segurança
!

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!Exercício 1!
else if (com .EQ. 1) then
pri = 0
seg = 0
ter = 0 !É necessário reiniciar as variáveis cada 
qua = 0
xaxis = 0
yaxis = 0
input1 = 1
input2 = -1
do while (input1 .NE. 0 .OR. input2 .NE. 0)
print *, "Digite um valor para X e Y respectivamente."
print *, "Digite (0,0) para sair."
read *, input1, input2

if (input1 .EQ. 0 .AND. input2 .EQ. 0) then !X=0, Y=0 -> Para de pedir inputs
print *, "Primeiro Quadrante:", pri
print *, "Segundo Quadrante:", seg
print *, "Terceiro Quadrante:", ter
print *, "Quarto Quadrante:", qua
print *, "Eixo X:", xaxis
print *, "Eixo Y:", yaxis
print *, " "
print *, " "
exit

else if (input1 .EQ. 0 .AND. input2 .NE. 0) then !X = 0
xaxis = xaxis + 1

else if (input1 .NE. 0 .AND. input2 .EQ. 0) then !Y = 0
yaxis = yaxis + 1

else if (input1 .GT. 0) then !Quando X > 0
	if (input2 .GT. 0) then ! Y > 0, Primeiro Quadrante
		pri = pri + 1
	else if (input2 .LT. 0) then ! Y < 0, Quarto Quadrante
		qua = qua + 1
	endif

else if (input1 .LT. 0) then !Quando X < 0
	if (input2 .GT. 0) then ! Y > 0, Segundo Quadrante
		seg = seg + 1
	else if (input2 .LT. 0) then ! Y < 0, Terceiro Quadrante
		ter = ter + 1
	endif
endif
enddo
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!Exercício 2!
else if (com .EQ. 2) then
print *, "Digite um número de no máximo 3 digitos."
read *, ninput

print *, ninput(1), ninput(2), ninput(3)









!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
endif
enddo
print *, "Terminando programa..."
end program trabalho2