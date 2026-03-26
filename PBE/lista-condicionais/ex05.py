velocidade = int(input('Informe a velocidade do carro: '))
limite_via = int(input('Informe o limite da via: '))
tolerancia = 0

if 0 < limite_via <= 100:
    tolerancia = limite_via + 7
elif limite_via > 100:
    tolerancia = limite_via * 1.07
else:
    print('Valor inserido inválido!')

if velocidade > (tolerancia * 1.5):
    print('Multa aplicada: Gravíssima + Suspensão')
elif velocidade > (tolerancia * 1.2):
    print('Multa aplicada: Grave')
elif velocidade > tolerancia:
    print('Multa aplicada: Média')
else:
    print('Isento de Multa')