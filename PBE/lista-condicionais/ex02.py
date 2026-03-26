lado1 = float(input('Informe o primeiro lado do triângulo: '))
lado2 = float(input('Informe o segundo lado do triângulo: '))
lado3 = float(input('Informe o terceiro lado do triângulo: '))

print()

if not lado1 + lado2 > lado3:
    print('Este triângulo não é válido! Utilize outros valores!')
else:
    if lado1 == lado2 and lado2 == lado3:
        print('O triângulo digitado é equilátero!')
    elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
        print('O triângulo digitado é isósceles!')
    else:
        print('O triângulo digitado é escaleno!')

    ehTrianguloRetangulo = lado1 ** 2 + lado2 ** 2 == lado3 ** 2

    if ehTrianguloRetangulo:
        print('E além disso, é um triângulo retângulo!')