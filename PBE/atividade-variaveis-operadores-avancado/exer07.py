qtd_pecas = int(input("Informe a quantidade de peças que são montadas por minuto: "))
tempo_operacao_minutos = int(input("Informe o tempo de operação em minutos: "))

print(f"\nA quantidade total de peças produzidas no período de {tempo_operacao_minutos} minutos é de: {qtd_pecas * tempo_operacao_minutos}")