from restaurant import Restaurante


class Pizzaria(Restaurante):
    def __init__(self, nome_restaurante, tipo_cozinha):
        super().__init__(nome_restaurante, tipo_cozinha)
        self.flavors = []

    def show_flavors(self, sabores):
        self.flavors = sabores
        print('Sabores disponíveis')
        for flavor in self.flavors:
            print(f'- {flavor.title()}')


dandy = Pizzaria('pizzaria dandy', 'pizzaria')
dandy.abrir_restaurante()
sabores = ['calabreza', 'siciliana', 'quatro queijos',
           'a moda da casa', 'rúcula com tomate seco'
           ]
dandy.show_flavors(sabores)
print()
