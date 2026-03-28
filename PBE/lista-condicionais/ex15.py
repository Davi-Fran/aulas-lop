peso = float(input('Informe o peso, em kg, da encomenda: '))

print('\n~ Escolha entre as regiões: sudeste, sul, norte, nordeste ou centro-oeste ~')
regiao = input('Para qual região será feita a entrega: ')
regiao = regiao.strip().upper()

verificao_assinante = input('Você é assinante premium? [s/n]: ')
verificao_assinante = verificao_assinante.strip().upper()

if verificao_assinante == 'S' or verificao_assinante == 'SIM':
    eh_assiante_premium = True
else:
    eh_assiante_premium = False

preco_final = 0
fixo = 0

if peso > 20:
    fixo += 30

if regiao == 'SUDESTE':
    fixo += 10
    preco_final = fixo + 2 * peso
elif regiao == 'SUL':
    fixo += 15
    preco_final = fixo + 3 * peso
elif regiao == 'NORTE' or regiao == 'NORDESTE':
    fixo += 25
    preco_final = fixo + 5 * peso
elif regiao == 'CENTRO-OESTE':
    fixo += 20
    preco_final = fixo + 4 * peso

if eh_assiante_premium:
    preco_final *= 0.8

print()

print(f'O valor final a ser pago é: R${preco_final:.2f}')