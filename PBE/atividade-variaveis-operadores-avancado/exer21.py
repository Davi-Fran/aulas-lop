import math

a = int(input("Digite o valor do primeiro lado do triângulo: "))
b = int(input("Digite o valor do segundo lado do triângulo: "))
c = int(input("Digite o valor do terceiro lado do triângulo: "))

semiperimetro = (a + b + c) / 2
area = math.sqrt(semiperimetro * (semiperimetro - a) * (semiperimetro - b) * (semiperimetro - c))

if a == b and b == c:
    print("\nO triângulo digitado é equilátero!")
elif a == b or b == c or a == c:
    print("\nO triângulo digitado é isósceles!")
else:
    print("\nO triângulo digitado é escaleno!")

print(f"E sua área é {area:.2f}")