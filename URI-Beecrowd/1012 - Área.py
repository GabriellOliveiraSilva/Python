entrada = input().split()
triangulo = (float(entrada[0]) * float(entrada[2]))/2
circulo = ((float(entrada[2])**2) * 3.14159)
trapezio = ((float(entrada[0]) + float(entrada[1])) * float(entrada[2]))/2
quadrado = (float(entrada[1])** 2)
retangulo = float(entrada[0]) * float(entrada[1])

print(f'TRIANGULO: {triangulo:.3f}')
print(f'CIRCULO: {circulo:.3f}')
print(f'TRAPEZIO: {trapezio:.3f}')
print(f'QUADRADO: {quadrado:.3f}')
print(f'RETANGULO: {retangulo:.3f}')
