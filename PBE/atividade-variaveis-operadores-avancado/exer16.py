consumo_energia_servidor = float(input("Qual é o consumo de energia, em Watts, do servidor?: "))
qtd_servidores = int(input("Quantos servidores estão no data center?: "))

print(f"\nO total de consumo desse data center é de {consumo_energia_servidor * qtd_servidores:.0f}W")