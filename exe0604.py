cores = {
    'white': 'branco',
    'yellow': 'amarelo',
    'black': 'preto',
    'brown': 'marrom',
    'purple': 'roxo',
}

for ing, port in cores.items():
    print(f'A cor {ing} em português é {port}')

cores['orange'] = 'laranja'
cores['beige'] = 'bege'
cores['blue'] = 'azul'

print()
for ing, port in cores.items():
    print(f'A cor {ing} em português é {port}')
