""" EXEMPLOS """
from email.encoders import encode_noop

# EXEMPLO 1
# cores = ['vermelho', 'verde', 'azul', 'amarelo']
# for cor in cores:
#     print(f'Cor selecionada: {cor}')

# EXEMPLO 2
# msg = 'Hello World!'
# for caractere in msg:
#     print(caractere)

# EXEMPLO 3
# pessoa = {
#     'nome': 'Ana',
#     'idade': 30,
#     'profissão': 'Engenheira'
# }
#
# print(pessoa['nome'])
# for chave, valor in pessoa.items():
#     print(f'{chave}: {valor}')

# EXEMPLO 4
# animais = {'gato', 'cachorro', 'elefante', 'girafa'} # conjunto
# for animal in animais:
#     print(animal)

# EXEMPLO 5
# nome_arquivo = './aula-30-03.txt'
# with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
#     for linha in arquivo:
#         print(linha.strip())

# EXEMPLO 6
# m = 8
# n = 2
#
# while m > 2:
#     n += 2
#     m -= 1
#
# print(m, n)



""" EXERCÍCIOS """

# EXERCÍCIO 1
# for numero in range(0, 11):
#     if numero % 2 == 0:
#         print(numero)

# OU

# for numero in range(0, 11, 2):
#     print(numero)


# EXERCÍCIO 2
# soma = 0
# for numero in range(1, 101):
#     soma += numero
#
# print(soma)

# EXERCÍCIO 3
# numero = int(input('Digite um número para fazer a tabuada: '))
#
# print()
#
# for fator in range(1, 11):
#     print(f'{numero} x {fator:2} = {numero * fator}')

# EXERCÍCIO 4
# qtd_notas = int(input('Quantas notas serão inseridas?: '))
# notas = []
#
# print()
#
# for i in range(1, qtd_notas + 1):
#     nota = float(input(f'Informe a nota {i}: '))
#     notas.append(nota)
#
# print()
#
# media = sum(notas) / len(notas)
#
# print(f'A média das notas inseridas é {media:.1f}')

# EXERCÍCIO 5
numero = int(input('Digite um número entre 5 e 10: '))

if 5 <= numero <= 10:
    contagem = numero

    while contagem > 0:
        print(contagem)
        contagem -= 1
else:
    print('O número digitado não está no intervalo de 5 e 10')