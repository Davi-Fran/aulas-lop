# EXERCÍCIO 1
# num1 = int(input("Digite um número: "))
# num2 = int(input("Digite outro número: "))
#
# soma = num1 + num2
#
# print(f"A soma entre {num1} e {num2} é igual a {soma}")


# EXERCÍCIO 2
# num = int(input("Digite um número: "))
#
# print(f"O número {num} é ímpar? Resposta: {num % 2 != 0}")


# EXERCÍCIO 3
# valor1 = int(input("Digite um número: "))
# valor2 = int(input("Digite outro número: "))
#
# print(f"{valor1} é maior que 3 ou {valor2} é menor que 4? Resposta: {valor1 > 3 or valor2 < 4}")


# EXERCÍCIO 4
# num = int(input("Digite um número: "))
#
# print(f"O valor absoluto de {num} é {abs(num)}")


# EXERCÍCIO 5
# valor1 = int(input("Digite um número: "))
# valor2 = int(input("Digite outro número: "))
#
# print(f"{valor1} e {valor2} são pares? Resposta: {valor1 % 2 == 0 and valor2 % 2 == 0}")


# EXERCÍCIO 6
# valor1 = int(input("Digite um número: "))
# valor2 = int(input("Digite outro número: "))
#
# print(f"\n{valor1} ou {valor2} são negativos? Resposta: {valor1 < 0 or valor2 < 0}")


# EXERCÍCIO 7
# valor1 = int(input("Digite um número: "))
# valor2 = int(input("Digite outro número: "))
# valor3 = int(input("Digite um terceiro número: "))
#
# media = (valor1 + valor2 + valor3) / 3
#
# print(f"\nA média aritmética entre {valor1}, {valor2} e {valor3} é igual a {media:.2f}")


# EXERCÍCIO 8
# valor1 = int(input("Digite um número: "))
# valor2 = int(input("Digite outro número: "))
#
# print(f"\nO resultado da expressão ({valor1} + 15 é igual a {valor2} x 3) é: {(valor1 + 15) == (valor2 * 3)}")


# EXERCÍCIO 9
# dividendo = int(input("Digite o valor do dividendo: "))
# divisor = int(input("Digite o valor do divisor: "))
#
# print(f"\nO dividendo é {dividendo} e o divisor é {divisor}")
# print(f"O resultado da divisão é {dividendo / divisor}")
# print(f"O resto da divisão é {dividendo % divisor}")


# EXERCÍCIO 10
# celsius = float(input("Digite uma temperatura (Em celsius): "))
#
# fahrenheit = celsius * 1.8 + 32
#
# print(f"{celsius} °C é equivalente à {fahrenheit:.1f} °F")


# EXERCÍCIO 11
# peso = float(input("Digite seu peso em kg: "))
# altura = float(input("Digite sua altura em metros: "))
#
# imc = peso / (altura ** 2)
#
# print(f"\nSeu IMC é {imc:.2f} kg/m²")


# EXERCÍCIO 12
# nota1 = float(input("Digite a primeira nota: "))
# nota2 = float(input("Digite a segunda nota: "))
# nota3 = float(input("Digite a terceira nota: "))
#
# PESO1 = 4
# PESO2 = 6
# PESO3 = 8
#
# media = ((nota1 * PESO1) + (nota2 * PESO2) + (nota3 * PESO3)) / (PESO1 + PESO2 + PESO3)
#
# print(f"\nA média ponderada das notas {nota1}, {nota2} e {nota3} é igual a {media:.1f}")


# EXERCÍCIO 13
# numero = int(input("Digite um número: "))
# expoente = int(input("Agora digite o expoente desse número: "))
#
# print(f"\n{numero} elevado a {expoente} é igual a {numero ** expoente}")


# DESAFIO 1
# numero = int(input("Digite um número: "))
#
# print(f"A raiz cúbica de {numero} é {numero ** (1/3)}")


# DESAFIO 2
# capital = float(input("Digite quanto há de capital (em R$): "))
# taxa_juros = int(input("Digite a taxa de juros: "))
# tempo_anos = int(input("Digite quantos anos o capital está aplicado: "))
#
# montante_final = capital * ((1 + taxa_juros / 100) ** tempo_anos)
#
# print(f"\nO montante final, após {tempo_anos} anos da aplicação de R$ {capital:.2f}, a uma taxa de juros de {taxa_juros}%, é igual a R$ {montante_final:.2f}")