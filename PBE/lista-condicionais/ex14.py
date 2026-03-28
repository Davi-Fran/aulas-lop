numero = int(input('Digite um número de 5 dígitos: '))

if not 10000 <= numero <= 99999:
    print('Valor inválido! O número deve ter 5 dígitos!')
else: # 54345
    primeiro_digito = numero // 10000
    segundo_digito = (numero // 1000) % 10
    quarto_digito = (numero // 10) % 10
    quinto_digito = numero % 10

    if primeiro_digito == quinto_digito and segundo_digito == quarto_digito:
        print('O número é um palíndromo!')
    else:
        print('O número não é um palíndromo!')