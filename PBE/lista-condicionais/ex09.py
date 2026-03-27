hora_inicial = int(input('Informe a hora inicial: '))
minuto_inicial = int(input('Informe o minuto inicial: '))
hora_final = int(input('Informe a hora final: '))
minuto_final = int(input('Informe o minuto final: '))

print()

if (not 0 <= hora_inicial <= 23 or not 0 <= hora_final <= 23 or
    not 0 <= minuto_inicial <= 59 or not 0 <= minuto_final <= 59):
    
    print('Algum dos valores inseridos é inválido!')
else:
    duracao_minutos = (hora_final * 60 + minuto_final) - (hora_inicial * 60 + minuto_inicial)

    if duracao_minutos == 0:
        duracao_minutos = 1440
    elif duracao_minutos < 0:
        duracao_minutos += 1440

    duracao_horas = duracao_minutos // 60
    duracao_minutos %= 60

    print(f'O jogo durou {duracao_horas:02d} hora(s) e {duracao_minutos:02d} minuto(s)')