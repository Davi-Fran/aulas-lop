import math

x1 = float(input("Digite o X do primeiro ponto: "))
y1 = float(input("Digite o Y do primeiro ponto: "))
x2 = float(input("Digite o X do segundo ponto: "))
y2 = float(input("Digite o Y do segundo ponto: "))

distanciaEuclidiana = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f"\nA distância entre os dois pontos é igual a {distanciaEuclidiana}")