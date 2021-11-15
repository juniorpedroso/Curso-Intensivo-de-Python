while True:
    try:

        num1 = input('\nDigite um número (S para sair): ')
        if num1.upper() == 'S':
            break
        num1 = int(num1)
        
        num2 = input('Digite outro número (S para sair):')
        if num2.upper() == 'S':
            break
        num2 = int(num2)

    except ValueError:
        print('Erro!!! Você precisa digitar um número!')

    else:
        sum = num1 + num2
        print(f'O resultado de  {num1} + {num2} é {sum}.\n')