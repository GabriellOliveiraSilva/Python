N = int(input())
while True:
  C = int(input())
  if 0 <= C < N:
   break
  else:
    C = int(input())

preenche_grafo = input().split()
G = [[0 for x in range(N)]for y in range(N)]
index = 0
for x in range(N):
  for y in range(N):
    G[x][y] = int(preenche_grafo[index])
    index += 1

K = [1]
p_aux = 0
for y in range(0, N):
  if G[y][C] == 1:
    K.append(y)

for y in range(N):
  if G[y][C] == 1:
    p_aux = y
    for z in range(N):
      if G[z][p_aux] == 1:
        K.append(z)
        z = C
      if len(K) >= N:
        break
      if G[z][C] == 1 and G[C][z] == 1:
       K.pop(0)

  
print(len(K))