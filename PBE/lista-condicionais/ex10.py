senha = input('Crie uma senha: ')

tem_especial = not senha.isalnum()

if len(senha) < 8:
    print('Senha inválida! Ela deve ter ao menos 8 caracteres!')
else:
    if tem_especial and senha.isupper() and senha.isalnum():
        print('Senha forte')
    elif senha.isalnum():
        print('Senha média')
    elif senha.isalpha() and senha.islower() or senha.isnumeric():
        print('Senha fraca')