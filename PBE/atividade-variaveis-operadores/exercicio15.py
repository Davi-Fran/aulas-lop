nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 5)) / 10

print(f"\nA média ponderada entre {nota1}, {nota2} e {nota3} é igual a {media:.1f}")