file_name = 'exe1005_enquete.txt'

continua = True

while continua:
    resposta = input('Porque você gosta de programação? (s para sair): ')
    if resposta.upper() == 'S':
        continua = False
    elif resposta == '':
        print('Você não digitou nada!')
    else:
        with open(file_name, 'a') as file_object:
            file_object.write(f'{resposta}\n')


with open(file_name) as file_object:
    lines = file_object.readlines()

print('\nUsuários Cadastrados')
for line in lines:
    print(line.strip())
