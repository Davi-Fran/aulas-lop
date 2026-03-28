linha_atual = int(input('Linha em que o cavalo está: '))
coluna_atual = int(input('Coluna em que o cavalo está: '))

print()

linha_destino = int(input('Linha de destino do cavalo: '))
coluna_destino = int(input('Coluna de destino do cavalo: '))

print()

if not (0 < linha_atual <= 8 and 0 < coluna_atual <= 8 and
    0 < linha_destino <= 8 and 0 < coluna_destino <= 8):
    print('Os valores digitados inválidos!')
else:
    diferenca_linha = abs(linha_destino - linha_atual)
    diferenca_coluna = abs(coluna_destino - coluna_atual)

    if (diferenca_linha == 2 and diferenca_coluna == 1 or 
        diferenca_linha == 1 and diferenca_coluna == 2):
        print('Movimento válido!')
    else:
        print('Movimento inválido!')