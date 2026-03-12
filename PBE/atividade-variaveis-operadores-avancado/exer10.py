valor_mensal = float(input("Digite o valor mensal pago pelo serviço de hospedagem: "))
qtd_meses_contratados = int(input("Digite a quantidade de meses em que o serviço foi contratado: "))

print(f"\nO preço total a ser pago será de R$ {valor_mensal * qtd_meses_contratados:.2f}")