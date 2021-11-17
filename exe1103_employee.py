class Employee():
    """[Criando um funcionário]
    """

    def __init__(self, nome, sobrenome, salario):
        """[Inicializando os atributos da classe]
        """
        self.nome = nome
        self.sobrenome = sobrenome
        self.salario = salario

    def give_raise(self, aumento=5000):
        """[Aumenta o salário do funcionário, por padrão em 5000,
        ou aceita outro valor]

        Args:
            aumento (int, optional): [description]. Defaults to 5000.
        """
        self.salario += aumento

