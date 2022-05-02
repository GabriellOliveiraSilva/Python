#Import da Função que divide string com multiplos comparadores
import re

#Inserção de dados
Input = input('Insira seu CPF: ')

# Separação 1
CPF = re.split("[,\.|-]",Input)
CPF_Verificar = []
#Separação 2
matriz = [list(number) for number in CPF]

#Variaveis
contador = 10
contador2 = 11
soma_valores = 0
soma_valores2 = 0
digito1 = 0
digito2 = 0

#Definir Primeiro Digito
for x in range(3):
    for y in range(3):
        soma_valores += int(matriz[x][y]) * contador
        contador -= 1
digito1 = 11 -(soma_valores % 11)
if digito1 > 9:
    digito1 = 0


#Define Segundo Digito
#Adiciona todos os digitos numa lista auxiliar e depois envia para a lista definitiva, formando assim uma matriz
for x in range(3):
    matriz_aux = []
    for y in range(3):
        soma_valores2 += int(matriz[x][y]) * contador2
        contador2 = contador2 - 1
        valor = matriz[x][y]
        matriz_aux.append(valor)
    CPF_Verificar.append(matriz_aux)
    matriz_aux = []
    if x == 2:
     soma_valores2 += digito1 * 2
     digito2 = 11 - (soma_valores2 % 11)
     if digito2 > 9:
       digito2 = 0
     matriz_aux.append(str(digito1))
     matriz_aux.append(str(digito2))
     CPF_Verificar.append(matriz_aux)

   

soma_valores2 += digito1 * 2
digito2 = 11 - (soma_valores2 % 11)
if digito2 > 9:
    digito2 = 0


if CPF_Verificar == matriz:
    print('CPF VÁLIDO')
else:
    print('CPF INVÁLIDO')
