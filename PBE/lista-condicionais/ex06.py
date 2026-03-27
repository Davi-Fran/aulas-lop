dia = int(input('Insira o dia: '))
mes = int(input('Insira o mês: '))
ano = int(input('Insira o ano: '))

is_ano_bissexto = ano % 4 == 0 and ano % 100 != 0 or ano % 100 == 0 and ano % 400 == 0
is_data_valida = True

print()

if ano > 1900 and ano < 2026:
    if (mes == 1 or mes == 3 or 
        mes == 5 or mes == 7 or
        mes == 8 or mes == 10 or mes == 12):
        
        if dia > 31:
            is_data_valida = False
    elif mes == 2:
        if is_ano_bissexto:
            if dia > 29:
                is_data_valida = False
        else:
            if dia > 28:
                is_data_valida = False
    else:
        if dia > 30:
            is_data_valida = False
else:
    is_data_valida = False
    
    
if is_data_valida:
    print(f'A data digitada foi {dia:02d}/{mes:02d}/{ano:02d}')
else:
    print('A data digitada é inválida!')