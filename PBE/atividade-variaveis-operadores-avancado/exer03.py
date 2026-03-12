preco_produto = float(input("Informe o preço do produto: "))
frete = float(input("Informe o valor do frete: "))
qtd_comprada = int(input("Informe a quantidade comprada: "))

total_compra = preco_produto * qtd_comprada + frete

print(f"\nO valor total da compra foi de R$ {total_compra:.2f}")