# EXEMPLO IF-ELIF-ELSE
# nota = float(input("Digite uma nota entre 0 e 10: "))
#
# if 0 < nota <= 7 and nota > 6:
#     print("Você foi aprovado!")
# elif nota >= 8:
#     print("Você foi aprovado com uma nota acima da média!")
# elif nota == 6:
#     print("Você está de recuperação!")
# else:
#     print("Você foi reprovado!")


# EXERCÍCIO 1
# idade = int(input("Qual a sua idade?: "))
#
# if idade >= 18:
#     print("Você é maior de idade!")
# else:
#     print("Você é menor de idade!")


# EXERCÍCIO 2
# nota = float(input("Digite a sua nota: "))
#
# if nota >= 9:
#     print("Sua nota é excelente!")
# elif nota >= 7:
#     print("Sua nota é boa!")
# elif nota >= 5:
#     print("Sua nota está na média!")
# else:
#     print("Sua nota é insuficiente!")


# EXERCÍCIO 3
# num = float(input("Digite um número: "))
#
# if num % 2 == 0:
#     print("\nO número é par!")
# else:
#     print("\nO número é ímpar!")
#
# if num % 3 == 0 and num % 5 == 0:
#     print("E é múltiplo de 3 e de 5!")
# elif num % 3 == 0:
#     print("E é múltiplo de 3!")
# elif num % 5 == 0:
#     print("E é múltiplo de 5!")
# else:
#     print("E não é múltiplo de 3 e nem 5!")


# EXERCÍCIO 4
# num1 = int(input("Digite um número: "))
# num2 = int(input("Digite mais um número: "))
#
# if num1 == num2:
#     print("Os números são iguais!")
# elif num1 > num2:
#     print(f"{num1} é maior que {num2}")
# else:
#     print(f"{num2} é maior que {num1}")

# print(max(1, 1))


# EXERCÍCIO 5
print("========= MENU =========")
print("1 - Abrir arquivo")
print("2 - Salvar arquivo")
print("3 - Fechar arquivo")
print("4 - Copiar")
print("5 - Colar")
print("6 - Recortar")
print("7 - Desfazer")
print("8 - Refazer")
print("9 - Imprimir")
print("10 - Sair do programa")
print("=======================")

opcao = int(input("\nDigite uma opção: "))

match opcao:
    case 1:
        print("\nAbrindo arquivo...")
    case 2:
        print("\nSalvando arquivo...")
    case 3:
        print("\nFechando arquivo...")
    case 4:
        print("\nCopiando...")
    case 5:
        print("\nColando...")
    case 6:
        print("\nRecortando...")
    case 7:
        print("\nDesfazendo...")
    case 8:
        print("\nRefazendo...")
    case 9:
        print("\nImprimindo...")
    case 10:
        print("\nSaindo do programa...")


# EXEMPLO MATCH CASE
# nota = int(input("Digite sua nota (0 a 10): "))
#
# match nota:
#     case 9 | 10:
#         print("Nota excelente. Aprovado!")
#     case 8:
#         print("Nota boa. Aprivado!")
#     case 7:
#         print("Nota média. Aprovado!")
#     case _: # Essa daqui é o equivalente ao default do switch case
#         print("Reprovado.")