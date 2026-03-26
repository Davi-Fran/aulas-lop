ano = int(input('Digite algum ano: '))

if ano % 4 == 0 and not ano % 100 == 0:
    print('O ano é bissexto')
elif ano % 100 == 0 and ano % 400 == 0:
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')