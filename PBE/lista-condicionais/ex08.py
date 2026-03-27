valor = float(input('Informe o valor a ser sacado: R$'))

print()

tipos_notas = [100, 50, 20, 10, 5, 2]
qtd_notas = {
    '100': 0,
    '50': 0,
    '20': 0,
    '10': 0,
    '5': 0,
    '2': 0
}

for nota in tipos_notas:
    qtd_notas[str(nota)] = valor // nota
    valor %= nota

if not valor == 0:
    print('Valor impossível de sacar com as notas disponíveis!')
else:
    for nota, qtd in qtd_notas.items():
        print(f'Quantidade de notas de R${int(nota):.2f} é: {qtd:.0f}')