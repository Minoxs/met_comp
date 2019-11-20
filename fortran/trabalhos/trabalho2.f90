program trabalho2
implicit none

integer :: com !Variável de comando
integer :: pri, seg, ter, qua, xaxis, yaxis !Variáveis exercício 1
real :: input1, input2 !Variáveis de input
character(len=3) :: ninput  !Número que será digitado pelo usuário no Exercício 2
character(len=4), dimension(3) :: res_piece !Fortran é chato de lidar com strings
character(len=12) :: result !Número romano convertido, Exercício 2
integer :: j !Variável do "do" no exercício 2.

print *, "--. ..- .. .-.. .... . .-. -- ."
print *, "1 - Pontos no Plano Cartesiano"
print *, "2 - Coversão Decimal-Romana"
print *, ".-- .- --. -. . .-. -.-. --- .-. .-. . .-"

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
ter = 0 !É necessário reiniciar as variáveis cada vez que for rodar essa parte do programa
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
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Como funciona: O número é colocado em uma STRING, assim, posso manipular dígito por dígito.
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!Exercício 2!
else if (com .EQ. 2) then
result = "ba"
ninput = ""
do while (ninput .NE. "000")
print *, "Digite um número de no máximo 3 digitos. (Digite '000' para sair)"
read *, ninput

if (ninput .EQ. "000") then
print *, "Voltando à seleção de exercício."
print *, " "
exit
endif

do while (ninput(3:3) .EQ. " ") !Essa parte move o número para a casa apropriada, exemplo: 12 é lido como 120
ninput(3:3) = ninput(2:2)       !Esse "do" move para que o 1 fique na dezena, e o 2 na unidade.
ninput(2:2) = ninput(1:1)
ninput(1:1) = " "
enddo

do j = 1, 3 !Esse "do" que é responsável por realmente converter os números
SELECT CASE (ninput(j:j))
case (" ")
res_piece(j) = " "
cycle
case ("0")
res_piece(j) = " "
cycle
case ("1")
	if (j .EQ. 1) then
		res_piece(1) = "c"
	else if (j .EQ. 2) then
		res_piece(2) = "x"
	else if (j .EQ. 3) then
		res_piece(3) = "i"
	endif
case ("2")
	if (j .EQ. 1) then
		res_piece(1) = "cc"
	else if (j .EQ. 2) then
		res_piece(2) = "xx"
	else if (j .EQ. 3) then
		res_piece(3) = "ii"
	endif
case ("3")
	if (j .EQ. 1) then
		res_piece(1) = "ccc"
	else if (j .EQ. 2) then
		res_piece(2) = "xxx"
	else if (j .EQ. 3) then
		res_piece(3) = "iii"
	endif
case ("4")
	if (j .EQ. 1) then
		res_piece(1) = "cd"
	else if (j .EQ. 2) then
		res_piece(2) = "xl"
	else if (j .EQ. 3) then
		res_piece(3) = "iv"
	endif
case ("5")
	if (j .EQ. 1) then
		res_piece(1) = "d"
	else if (j .EQ. 2) then
		res_piece(2) = "l"
	else if (j .EQ. 3) then
		res_piece(3) = "v"
	endif
case ("6")
	if (j .EQ. 1) then
		res_piece(1) = "dc"
	else if (j .EQ. 2) then
		res_piece(2) = "lx"
	else if (j .EQ. 3) then
		res_piece(3) = "vi"
	endif
case ("7")
	if (j .EQ. 1) then
		res_piece(1) = "dcc"
	else if (j .EQ. 2) then
		res_piece(2) = "lxx"
	else if (j .EQ. 3) then
		res_piece(3) = "vii"
	endif
case ("8")
	if (j .EQ. 1) then
		res_piece(1) = "dccc"
	else if (j .EQ. 2) then
		res_piece(2) = "lxxx"
	else if (j .EQ. 3) then
		res_piece(3) = "viii"
	endif
case ("9")
	if (j .EQ. 1) then
		res_piece(1) = "cm"
	else if (j .EQ. 2) then
		res_piece(2) = "xc"
	else if (j .EQ. 3) then
		res_piece(3) = "ix"
	endif 
END SELECT
enddo
result = trim(res_piece(1))//trim(res_piece(2))//trim(res_piece(3))
print *, result
print *, " "
print *, " "
print *, " "
enddo
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
endif
enddo
print *, "Terminando programa..."
end program trabalho2
!Guilherme Wagner Correa
!Instituto de Física, UFRGS.