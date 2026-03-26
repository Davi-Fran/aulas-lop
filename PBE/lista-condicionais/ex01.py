from math import sqrt

altura = float(input('Informe a altura: '))
t = sqrt(altura / 4.9)

if altura < 0:
    print('Altura inválida: a altura não pode ser negativa')
else:
    print(f'O tempo desse objeto em repouso chegar até o solo, numa altura inicial de {altura}m é de {t:.2f}s')