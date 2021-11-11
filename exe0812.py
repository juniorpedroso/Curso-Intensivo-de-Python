def make_sandwich(*ingredients):
    """[função que cria e exibe os ingredientes de meu sanduíche]
    """
    print('\nO seu sanduíche terá os seguintes ingredientes:')
    for i in ingredients:
        print(f'- {i}')
    print('Bom apetite!\n')


make_sandwich('catupiry', 'mostarda', 'molho de alho')
make_sandwich('mussarela', 'duas salsichas')
make_sandwich('dois hamburguers')
