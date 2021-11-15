
try:
    num1 = input('\nDigite um número: ')
    num1 = int(num1)
    num2 = input('Digite outro número: ')
    num2 = int(num2)

except ValueError:
    print('Erro!!! Você precisa digitar um número!')

else:
    sum = num1 + num2
    print(f'O resultado de  {num1} + {num2} é {sum}.\n')
