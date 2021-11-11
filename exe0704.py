active = True
while active:
    recheio = input('Digite o recheio de sua pizza: (Tecle sair para sair) ')
    if recheio == 'sair':
        active = False
    else:
        print(f'Vamos acrescentar {recheio} em sua pizza.\n')
print('Sua pizza já está no forno. Volte Sempre!\n')