qtd_arquivos = int(input("Digite a quantidade de arquivos armazenados: "))
tamanho_medio = int(input("Digite o tamanho médio, em MB, dos arquivos: "))

tamanho_gb = qtd_arquivos * tamanho_medio / 1024

print(f"\nO espaço total ocupado é: {tamanho_gb:.2f} GB")