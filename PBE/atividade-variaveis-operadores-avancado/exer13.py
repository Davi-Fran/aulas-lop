tamanho_medio_log = int(input("Informe o tamanho médio, em MB, de um log gerado: "))
qtd_logs_gerados_por_dia = int(input("Qual a quantidade de logs gerados por dia: "))

print(f"\nO tamanho total de logs gerados em um dia é de {qtd_logs_gerados_por_dia * tamanho_medio_log} MB")