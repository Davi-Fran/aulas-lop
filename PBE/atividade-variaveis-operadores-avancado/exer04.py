velocidade_internet = int(input("Informe a velocidade da internet em Mbps: "))
tempo_download_segundos = int(input("Informe a tempo de download em segundos: "))

total_dados_tranferidos = velocidade_internet * tempo_download_segundos

print(f"O total de dados transferidos foi de: {total_dados_tranferidos} Megabits")