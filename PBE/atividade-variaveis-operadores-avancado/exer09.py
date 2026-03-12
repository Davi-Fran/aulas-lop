tamanho_arquivo = int(input("Digite o tamanho, em MB, do arquivo: "))
qtd_arquivos = int(input("Digite a quantidade de arquivos baixados: "))

tamanho_gb = qtd_arquivos * tamanho_arquivo / 1024

print(f"\nO tamanho total dos arquivos é: {tamanho_gb:.2f} GB")