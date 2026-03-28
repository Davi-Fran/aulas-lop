from math import sqrt

x_centro = float(input('Coordenada x do centro do círculo: '))
y_centro = float(input('Coordenada y do centro do círculo: '))
raio = float(input('Informe o raio do círculo: '))

print()

x_ponto = float(input('Coordenada x de um ponto P: '))
y_ponto = float(input('Coordenada y de um ponto P: '))

print()

distancia = sqrt(((x_ponto - x_centro) ** 2) + ((y_ponto - y_centro) ** 2))

if distancia > raio:
    print('O ponto P está fora do círculo!')
elif distancia == raio:
    print('O ponto P está na borda do círculo!')
else:
    print('O ponto P está dentro do círculo!')