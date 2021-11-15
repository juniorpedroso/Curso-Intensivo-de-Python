file_name = 'exe1004_usuarios.txt'

continua = True

while continua:
    usuario = input('Nome do usuário: (s para sair) ')
    if usuario.upper() == 'S':
        continua = False
    else:
        print(f'Bem vindo {usuario.title()}!')
        with open(file_name, 'a') as file_object:
            file_object.write(f'{usuario}\n')


with open(file_name) as file_object:
    lines = file_object.readlines()

print('\nUsuários Cadastrados')
for line in lines:
    print(f'- {line.strip()}')