import re

senha = input('Crie uma senha: ')

tem_maiusculas = re.search(r'[A-Z]', senha)
tem_minusculas = re.search(r'[a-z]', senha)
tem_numeros = re.search(r'\d', senha)
tem_caracteres_especiais = re.search(r'[^A-Za-z0-9]', senha)

if len(senha) < 8:
    print('Senha inválida! Ela deve ter ao menos 8 caracteres!')
elif (tem_maiusculas and tem_minusculas and 
      tem_numeros and tem_caracteres_especiais):
    print('Senha Forte')
elif re.fullmatch(r'[a-z]+|\d+', senha):
    print('Senha fraca')
elif (re.fullmatch(r'[A-Za-z0-9]+', senha) and 
      re.search(r'[A-Za-z]', senha) and tem_numeros):
    print('Senha média')
else:
    print('Senha inválida! Ela não se enquadrou em nenhuma das categorias existentes!')