tempo = int(input("Quantos minutos leva para produzir uma peça?: "))
qtd_pecas = int(input("Quantas peças vão ser produzidas?: "))

tempo_total_horas = tempo * qtd_pecas / 60

print(f"\nO tempo total de produção para {qtd_pecas} peças será de: {tempo_total_horas:.1f} horas")