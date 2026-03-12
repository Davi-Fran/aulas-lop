tempo_tarefa_segundos = int(input("Informe o tempo de execução da tarefa em segundos: "))
qtd_tarefas = int(input("Agora informe a quantidade de tarefas a serem feitas: "))

tempo_total_minutos = tempo_tarefa_segundos * qtd_tarefas / 60

print(f"\nO tempo total é de {tempo_total_minutos:.0f} minutos")