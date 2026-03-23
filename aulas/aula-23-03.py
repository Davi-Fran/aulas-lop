nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 9:
    resultado = 'Excelente'
elif media >= 7:
    resultado = 'Aprovado'
else:
    resultado = 'Reprovado'

print(f'Média: {media}')
print(f'Resultado: {resultado}')


""" TESTES DE MESA BASEADOS NO ALGORITMO ACIMA """
# Massa de dados: nota1 = 10 e nota2 = 9

# +-----------------+-------+-------+-------+-----------+
# | Linha Executada | nota1 | nota2 | media | resultado |
# +-----------------+-------+-------+-------+-----------+
# | 1               | 10    | -     | -     | -         |
# | 3               | 10    | 9     | -     | -         |
# | 5               | 10    | 9     | 9.5   | -         |
# | 6               | 10    | 9     | 9.5   | -         |
# | 7               | 10    | 9     | 9.5   | Excelente |
# | 8               | 10    | 9     | 9.5   | Excelente |
# | 9               | 10    | 9     | 9.5   | Excelente |
# | 10              | 10    | 9     | 9.5   | Excelente |
# | 11              | 10    | 9     | 9.5   | Excelente |
# | 12              | 10    | 9     | 9.5   | Excelente |
# | 13              | 10    | 9     | 9.5   | Excelente |
# +-----------------+-------+-------+-------+-----------+

# Saída:
# Média: 9.5
# Resultado: Excelente



# Massa de dados: nota1 = 7 e nota2 = 6

# +-----------------+-------+-------+-------+-----------+
# | Linha Executada | nota1 | nota2 | media | resultado |
# +-----------------+-------+-------+-------+-----------+
# | 1               | 7     | -     | -     | -         |
# | 3               | 7     | 6     | -     | -         |
# | 5               | 7     | 6     | 6.5   | -         |
# | 6               | 7     | 6     | 6.5   | -         |
# | 7               | 7     | 6     | 6.5   | -         |
# | 8               | 7     | 6     | 6.5   | -         |
# | 9               | 7     | 6     | 6.5   | -         |
# | 10              | 7     | 6     | 6.5   | -         |
# | 11              | 7     | 6     | 6.5   | Reprovado |
# | 12              | 7     | 6     | 6.5   | Reprovado |
# | 13              | 7     | 6     | 6.5   | Reprovado |
# +-----------------+-------+-------+-------+-----------+

# Saída:
# Média: 6.5
# Resultado: Reprovado