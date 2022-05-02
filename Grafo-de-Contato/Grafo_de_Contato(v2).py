tamanho_grafo = int(input('Quantas pessoas tem no grafo? '))
while True:
  pessoa_contaminada = int(input('Quem está contaminado? '))
  if 0 <= pessoa_contaminada < tamanho_grafo:
   break
  else:
    pessoa_contaminada = int(input('Quem está contaminado? '))

preenche_grafo = input('Insira: ').split()
grafo = [[0 for x in range(tamanho_grafo)]for y in range(tamanho_grafo)]
index = 0
for x in range(tamanho_grafo):
  for y in range(tamanho_grafo):
    grafo[x][y] = int(preenche_grafo[index])
    index += 1

contaminados = [1]
p_aux = 0
for y in range(0, tamanho_grafo):
  if grafo[y][pessoa_contaminada] == 1:
    contaminados.append(y)

for y in range(tamanho_grafo):
  if grafo[y][pessoa_contaminada] == 1:
    p_aux = y
    for z in range(tamanho_grafo):
      if grafo[z][p_aux] == 1:
        contaminados.append(z)
        z = pessoa_contaminada
      if len(contaminados) >= tamanho_grafo:
        break
        
print(len(contaminados))