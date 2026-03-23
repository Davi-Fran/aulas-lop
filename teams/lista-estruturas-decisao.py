# EXERCÍCIO 1
# ano = int(input("Digite algum ano: "))
#
# print()
#
# if ano % 4 == 0 and not ano % 100 == 0:
#     print(f"{ano} é bissexto!")
# elif ano % 100 == 0 and ano % 400 == 0:
#     print(f"{ano} é bissexto!")
# else:
#     print(f"{ano} não é bissexto!")


# EXERCÍCIO 2
# peso = float(input('Digite seu peso: '))
# altura = float(input('Digite sua altura: '))
#
# imc = peso / altura ** 2
#
# print(f'\nSeu IMC é {imc:.2f} kg/m²')
#
# if imc >= 40:
#     print('Classificação: Obesidade Mórbida')
# elif imc > 35:
#     print('Classificação: Obesidade Mórbida')
# elif imc > 30:
#     print('Classificação: Obesidade')
# elif imc > 25:
#     print('Classificação: Sobrepeso')
# elif imc > 18.5:
#     print('Classificação: Normal')
# else:
#     print('Classificação: Baixo peso')


# EXERCÍCIO 3
# qtd_produto = int(input('Digite qual a quantidade de produtos: '))
# valor_unidade = float(input('Digite o valor da unidade: '))
#
# if qtd_produto > 100:
#     desconto_unidade = valor_unidade * 0.1
# else:
#     desconto_unidade = valor_unidade * 0.05
#
# valor_final = valor_unidade * qtd_produto - desconto_unidade * qtd_produto
#
# print(f'\nValor inicial da unidade: R$ {valor_unidade:.2f}')
# print(f'Quantidade solicitada: {qtd_produto}')
# print(f'Desconto por unidade: R$ {desconto_unidade:.2f}')
# print(f'Valor final a ser pago: R$ {valor_final:.2f}')


# EXERCÍCIO 4
# idade = int(input('Digite sua idade: '))
#
# if not idade > 0:
#     print('Valor inválido!')
# elif idade >= 18 and idade <= 70:
#     print('Seu tipo de voto é: Obrigatório')
# elif idade >= 16 or idade > 70:
#     print('Seu tipo de voto é: Facultativo')
# else:
#     print('Você foi identificado como Não Eleitor!')


# EXERCÍCIO 5
# idade_pessoa1 = int(input('Digite a idade da primeira pessoa: '))
# idade_pessoa2 = int(input('Digite a idade da segunda pessoa: '))
# idade_pessoa3 = int(input('Digite a idade da terceira pessoa: '))
#
# maior_idade = max(idade_pessoa1, idade_pessoa2, idade_pessoa3)
# menor_idade = min(idade_pessoa1, idade_pessoa2, idade_pessoa3)
#
# print()
#
# if maior_idade == idade_pessoa1:
#     print(f'Maior idade: Pessoa 1 ({idade_pessoa1})')
# elif maior_idade == idade_pessoa2:
#     print(f'Maior idade: Pessoa 2 ({idade_pessoa2})')
# else:
#     print(f'Maior idade: Pessoa 3 ({idade_pessoa3})')
#
# if menor_idade == idade_pessoa1:
#     print(f'Menor idade: Pessoa 1 ({idade_pessoa1})')
# elif menor_idade == idade_pessoa2:
#     print(f'Menor idade: Pessoa 2 ({idade_pessoa2})')
# else:
#     print(f'Menor idade: Pessoa 3 ({idade_pessoa3})')


# EXERCÍCIO 6
# horas = int(input('Digite as horas: '))
# minutos = int(input('Digite os minutos: '))
# segundos = int(input('Digite os segundos: '))
#
# print()
#
# if horas >= 0 and horas <= 24:
#     if minutos >= 0 and minutos < 60:
#         if segundos >= 0 and segundos < 60:
#             print(f'Horário digitado: {horas:02d}:{minutos:02d}:{segundos:02d}')
#         else:
#             print('O horário digitado está inválido!')
#     else:
#         print('O horário digitado está inválido!')
# else:
#     print('O horário digitado está inválido!')


# EXERCÍCIO 7
# nota = float(input("Digite a nota obtida na prova: "))
#
# if nota > 10 or nota < 0:
#     print("Valor invalido")
# elif nota >= 9 and nota <= 10:
#     print("Menção obtida: A")
# elif nota >= 7:
#     print("Menção obtida: B")
# elif nota >= 5:
#     print("Menção obtida: C")
# elif nota >= 3:
#     print("Menção obtida: D")
# else:
#     print("Menção obtida: E")


# EXERCÍCIO 8
# lado1 = float(input("Digite o valor do primeiro lado: "))
# lado2 = float(input("Digite o valor do segundo lado: "))
# lado3 = float(input("Digite o valor do terceiro lado: "))
# lado4 = float(input("Digite o valor do quarto lado: "))
#
# print()
#
# if lado1 == lado2 and lado1 == lado3 and lado1 == lado4:
#     print('A forma digitada é um quadrado')
# elif lado1 == lado2 and lado3 == lado4 or lado1 == lado3 and lado2 == lado4:
#     print('A forma digitada é um retângulo')
# else:
#     print('A forma digitada não é nem um quadrado e nem um retângulo')


# EXERCÍCIO 9
# num1 = float(input('Digite um número decimal: '))
# num2 = float(input('Digite um segundo número decimal: '))
# op = input('Selecione a operação aritmética (+, -, *, /): ')
#
# print()
#
# if op == '+':
#     print(f'Resultado: {num1 + num2}')
# elif op == '-':
#     print(f'Resultado: {num1 - num2}')
# elif op == '*':
#     print(f'Resultado: {num1 * num2}')
# elif op == '/':
#     print(f'Resultado: {num1 / num2}')
# else:
#     print('Operação inválida')


# EXERCÍCIO 10
# nota1 = float(input("Digite a primeira nota: "))
# nota2 = float(input("Digite a segunda nota: "))
# nota3 = float(input("Digite a terceira nota: "))
#
# menor_nota = min(nota1, nota2, nota3)
#
# media = (nota1 + nota2 + nota3 - menor_nota) / 2
#
# print(f'A média é {media}')


# EXERCÍCIO 11
# +-----------------+---+---+
# | Linha executada | a | b |
# +-----------------+---+---+
# | 1               | 8 | - |
# | 2               | 8 | 3 |
# | 3               | 8 | 3 |
# | 4               | 6 | 3 |
# | 5               | 6 | 9 |
# | 6               | 6 | 9 |
# +-----------------+---+---+

# Saída: 6 9


# EXERCÍCIO 12
# +-----------------+----+----+----+
# | Linha executada | x  | y  | z  |
# +-----------------+----+----+----+
# | 1               | 12 | -  | -  |
# | 2               | 12 | 5  | -  |
# | 3               | 12 | 5  | 3  |
# | 5               | 12 | 5  | 3  |
# | 6               | 12 | 5  | 15 |
# | 7               | 12 | 10 | 15 |
# | 9               | 8  | 10 | 15 |
# | 10              | 8  | 10 | 15 |
# +-----------------+----+----+----+

# Saída: 8 10 15


# DESAFIO
# import random
#
# numero_sorteado = random.randint(1, 10)
#
# palpite1 = int(input('Qual seu primeiro palpite?: '))
#
# if palpite1 == numero_sorteado:
#     print('Você acertou!')
# else:
#     if palpite1 > numero_sorteado:
#         print('Seu palpite é maior do que o número sorteado!')
#     else:
#         print('Seu palpite é menor do que o número sorteado!')
#
#     palpite2 = int(input('Qual seu segundo palpite?: '))
#
#     if palpite2 == numero_sorteado:
#         print('Você acertou!')
#     else:
#         print(f'Acabaram suas chances! O número digitado era {numero_sorteado}')