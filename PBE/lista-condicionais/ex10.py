senha = input('Crie uma senha: ')

if len(senha) < 8:
    print('Senha inválida! Ela deve ter ao menos 8 caracteres!')
elif senha.isalpha() and senha.islower() or senha.isnumeric():
    print('Senha fraca')
elif senha.isalnum() and senha.islower():
    print('Senha média')
elif '!@#$%&*()_-/\\' in senha:
    print('Senha forte')