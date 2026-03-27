from math import sqrt

a = float(input('Coeficiente a: '))
b = float(input('Coeficiente b: '))
c = float(input('Coeficiente c: '))

print()

if a == 0:
    print('Não é uma equação do segundo grau!')
else:
    delta = (b ** 2) - 4 * a * c

    if delta < 0:
        print('A equação não possui raízes reais!')
    elif delta == 0:
        raiz_unica = (-b + sqrt(delta)) / (2 * a)
        print(f'Delta = {delta}')
        print(f'A raiz única é {raiz_unica}')
    else:
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)

        print(f'Delta = {delta}')
        print(f'x\' = {x1}')
        print(f'x" = {x2}')