dia = int(input('Insira o dia: '))
mes = int(input('Insira o mês: '))
ano = int(input('Insira o ano: '))

is_ano_bissexto = ano % 4 == 0 and ano % 100 != 0 or ano % 100 == 0 and ano % 400 == 0

print()

if is_ano_bissexto and mes == 2 and dia > 29:
    print('A data inserida é inválida!')
elif mes == 2 and dia > 28:
    print('A data inserida é inválida!')
elif mes > 12:
    print('A data inserida é inválida!')
elif ano < 1900 or ano > 2026:
    print('Data inserida é inválida!')
else:
    print(f'A data digitada foi: {dia:02d}:{mes:02d}:{ano:02d}')