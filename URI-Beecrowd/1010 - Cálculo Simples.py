lista = []
for x in range(2):
  entrada = input().split()
  lista.append(entrada)
 
total = []
for x in range(2):
  aux1 = float(lista[x][1]) * float(lista[x][2])
  total.append(aux1)

print(f'VALOR A PAGAR: R$ {sum(total):.2f}')
