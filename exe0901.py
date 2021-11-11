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


meu_restaurante = Restaurante('velho madalosso', 'italiana')
seu_restaurante = Restaurante('mix cookery', 'oriental')
print()
meu_restaurante.descreva_restaurante()
meu_restaurante.abrir_restaurante()
print()
seu_restaurante.descreva_restaurante()
seu_restaurante.abrir_restaurante()
print()
