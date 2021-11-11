active = True

while active:
    idade = input('Informe sua idade: (Tecle sair para sair) ')
    if idade == 'sair':
        active = False
    elif int(idade) < 3:
        preco = 0
    elif 3 <= int(idade) <= 12:
        preco = 10
    else:
        preco = 15
    if active: print(f'O valor do seu ingresso é {preco}. \n')

print('\nVolte Sempre!\n') 

