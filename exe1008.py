gatos_txt = 'exe1008_cats.txt'
cachorros_txt = 'exe1008_dogs.txt'

try:
    with open(gatos_txt) as file_object:
        gatos = file_object.readlines()

except FileNotFoundError:
    print(f'Erro! Arquivo {gatos_txt} não encontrado.')

else:
    print('\nNomes de gatos:')
    for gato in gatos:
        print(gato.strip())

try:
    with open(cachorros_txt) as file_object:
        cachorros = file_object.readlines()

except FileNotFoundError:
    print(f'Erro! Arquivo {cachorros_txt} não encontrado.')
    
else:
    print('\nNomes de cachorros:')
    for cachorro in cachorros:
        print(cachorro.strip())
