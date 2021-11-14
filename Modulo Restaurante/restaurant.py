class Restaurante():
    """[Minha primeira Classe em Python]
    """

    def __init__(self, nome_restaurante, tipo_cozinha):
        """[Inicializa os atributos nome_restaurante e tipo_cozinha]

        Args:
            nome_restaurante ([type]): [description]
            tipo_cozinha ([type]): [description]
        """
        self.nome_restaurante = nome_restaurante
        self.tipo_cozinha = tipo_cozinha
        self.number_served = 0

    def descreva_restaurante(self):
        """[Exibir informações: nome e tipo]
        """
        print(f'Nome do Restaurante: {self.nome_restaurante.title()}')
        print(f'Tipo de cozinha: {self.tipo_cozinha.title()}')

    def abrir_restaurante(self):
        """[Mensagem informando que o restaurante está aberto]
        """
        print(f'O restaurante {self.nome_restaurante.title()}' +
              ' está aberto!')
        print(f'Foram servidos {self.number_served} clientes.')

    def set_number_served(self, clients):
        self.number_served = clients

    def increment_number_served(self, clients):
        self.number_served += clients


class IceCreamStand(Restaurante):
    """[Representa aspectos específicos de uma sorveteria]

    Args:
        Restaurante ([type]): [description]
    """

    def __init__(self, nome_restaurante, tipo_cozinha):
        """[Inicializa os atributos da classe-pai]

        Args:
            nome_restaurante ([type]): [description]
            tipo_cozinha ([type]): [description]
        """
        super().__init__(nome_restaurante, tipo_cozinha)
        self.flavors = ['abacaxi', 'baunilha', 'chocolate', 'limão',
                        'morango', 'napolitano', 'passas ao rum']

    def show_flavors(self):
        print('Sabores de sorvetes')
        for flavor in self.flavors:
            print(f'- {flavor.title()}')

