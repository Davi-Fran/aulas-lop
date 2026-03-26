salario_bruto = float(input('Qual seu salário bruto? R$'))
imposto_total = 0

print()

if salario_bruto <= 2000:
    print('Classificação: Isento')
elif salario_bruto <= 4000:
    print('Classificação: 10%')

    faixa_imposto_aplicado = salario_bruto - 2000
    imposto_total += faixa_imposto_aplicado * 0.1
elif salario_bruto <= 8000:
    print('Classificação: 20%')

    faixa_20_imposto_aplicado = salario_bruto - 4000
    imposto_total += faixa_20_imposto_aplicado * 0.2

    faixa_10_imposto_aplicado = salario_bruto - faixa_20_imposto_aplicado - 2000
    imposto_total += faixa_10_imposto_aplicado * 0.1
else:
    print('Classificação: 30%')

    faixa_30_imposto_aplicado = salario_bruto - 8000
    imposto_total += faixa_30_imposto_aplicado * 0.3

    faixa_20_imposto_aplicado = salario_bruto - faixa_30_imposto_aplicado - 6000
    imposto_total += faixa_20_imposto_aplicado * 0.2

    faixa_10_imposto_aplicado = salario_bruto - faixa_30_imposto_aplicado - 4000
    imposto_total += faixa_10_imposto_aplicado * 0.1

salario_liquido = salario_bruto - imposto_total
print(f'Salário bruto: R${salario_bruto:.2f}')

if imposto_total != 0 and salario_liquido != 0:
    print(f'Imposto total: R${imposto_total:.2f}')
    print(f'Salário líquido: R${salario_liquido:.2f}')