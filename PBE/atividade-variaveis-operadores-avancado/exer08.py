qtd_cameras = int(input("Digite a quantidade de câmeras: "))
preco_camera = float(input("Qual o preço das câmeras?: "))
preco_instalacao = float(input("Qual o valor para a instalação de cada câmera?: "))

custo_total_sistema = qtd_cameras * preco_camera + qtd_cameras * preco_instalacao

print(f"\nO custo total do sistema será de R$ {custo_total_sistema:.2f}")