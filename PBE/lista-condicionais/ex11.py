x1 = int(input('Coordenada x do ponto superior esquerdo do retângulo 1: '))
y1 = int(input('Coordenada y do ponto superior esquerdo do retângulo 1: '))

x2 = int(input('Coordenada x do ponto inferior direito do retângulo 1: '))
y2 = int(input('Coordenada y do ponto inferior direito do retângulo 1: '))

print()

x3 = int(input('Coordenada x do ponto superior esquerdo do retângulo 2: '))
y3 = int(input('Coordenada y do ponto superior esquerdo do retângulo 2: '))

x4 = int(input('Coordenada x do ponto inferior direito do retângulo 2: '))
y4 = int(input('Coordenada y do ponto inferior direito do retângulo 2: '))

print()

if not y1 > y2 and not y3 > y4:
    print('Valores inválidos! O Y superior esquerdo deve ser maior que o Y inferior direito!')
else:
    if x2 < x3 or x1 > x4 or y2 > y3 or y1 < y4:
        print('Os triângulos não se sobrepõem!')
    else:
        print('Os triângulos se sobrepõem!')