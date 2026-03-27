salario_bruto = float(input('Qual seu salário bruto? R$'))
imposto_total = 0

print()

if salario_bruto <= 2000:
    print('Classificação: Isento')
elif salario_bruto <= 4000:
    print('Classificação: 10%')
    imposto_total = (salario_bruto - 2000) * 0.1
elif salario_bruto <= 8000:
    print('Classificação: 20%')
    imposto_total = (salario_bruto - 4200) * 0.2
else:
    print('Classificação: 30%')
    imposto_total = (salario_bruto - 9000) * 0.3

salario_liquido = salario_bruto - imposto_total
print(f'Salário bruto: R${salario_bruto:.2f}')

if imposto_total != 0:
    print(f'Imposto total: R${imposto_total:.2f}')
    print(f'Salário líquido: R${salario_liquido:.2f}')