#Recebe a quantidade de pessoas no grafo
tamanho_grafo = int(input('Quantas pessoas tem no grafo? '))

#Recebe a pessoa contaminada e verifica se tal pessoa esta no grafo
while True:
  pessoa_contaminada = int(input('Quem esta cotaminado? '))
  if 0 <= pessoa_contaminada < tamanho_grafo:
   break
else:
  pessoa_contaminada = int(input('Quem esta contaminado?'))

#Cria o grafo
grafo = [[0 for x in range(tamanho_grafo)]for y in range(tamanho_grafo)]

contaminados = 1
aux_contaminado = 0

#Preenche o grafo
for y in range(tamanho_grafo):
  for x in range(tamanho_grafo):
    aux = int(input(f'Insira para [{y}][{x}] = '))
    while True:
      if aux == 1 or aux ==0:
        break
      else:
        aux = int(input(f'Insira para [{y}][{x}] = '))
    grafo[y][x] = aux

contaminados = []
p_aux = 0
for y in range(0, tamanho_grafo):
  if grafo[y][pessoa_contaminada] == 1:
    contaminados.append(y)

for y in range(0, tamanho_grafo):
  if grafo[y][pessoa_contaminada] == 1:
    p_aux = y
    for z in range(0, tamanho_grafo):
      if grafo[z][p_aux] == 1:
        contaminados.append(z)
        z = pessoa_contaminada
        print(contaminados)

       


      
print(contaminados)

