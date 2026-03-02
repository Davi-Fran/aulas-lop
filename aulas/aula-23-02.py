# Exemplo Prático 1
"""
nome = "Davi"
idade = 18
altura = 1.73

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Altura: {altura}")
"""

# Exemplo Prático 2
"""
nome = "Davi"
idade = 18

print("Olá, meu nome é", nome, "e tenho", idade, "anos.")
print(f"Olá, meu nome é {nome} e tenho {idade} anos.")
"""


# Exercício 1
"""
nome1 = "aula"
nome2 = "Python"

nome1, nome2 = nome2, nome1

print(f"O valor de nome1 é: {nome1}")
print(f"O valor de nome2 é: {nome2}")
"""


# Exercício 2
"""
Nome = "Davi"
Sobrenome = "França de Oliveira Silva"
NomeCompleto = f"{Nome} {Sobrenome}"

print(NomeCompleto)
"""


# Exercício 3
"""
NumeroInteiro = 10
NumeroConvertidoFloat = float(NumeroInteiro)

print(NumeroConvertidoFloat)
"""


# Exercício 4
"""

"""
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

data = f"{dia:02d}/{mes:02d}/{ano}" # Exemplo com operador ternário

print(f"A data digitada foi: {data}")