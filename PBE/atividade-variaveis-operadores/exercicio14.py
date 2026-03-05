a = input("Digite algo: ")
b = input("Digite outra coisa: ")

print("\nValores antes da troca:")
print(f"A = {a}\nB = {b}")

a, b = b, a

print("\nValores depois da troca:")
print(f"A = {a}\nB = {b}")