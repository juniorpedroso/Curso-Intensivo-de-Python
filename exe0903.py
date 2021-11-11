class Usuario():
    """[Classe criando um usuário]
    """

    def __init__(self, nome, sobrenome, nivel_acesso, linguagem):
        """[Inicializa os atribuitos da classe]

        Args:
            nome ([str]): [primeiro nome]
            sobrenome ([str]): [sobrenome]
            nivel_acesso ([str]): [master, normal, visitante]
            linguagem ([str]): [tipo de linguagem]
        """
        self.nome = nome
        self.sobrenome = sobrenome
        self.nivel_acesso = nivel_acesso
        self.linguagem = linguagem

    def descreva_usuario(self):
        """[Descreve o usuário]"""

        print(f'Usuário: {self.nome.title()} {self.sobrenome.title()}')
        print(f'Nível de acesso: {self.nivel_acesso.upper()}')
        print(f'Linguagem: {self.linguagem.title()}')

    def boas_vindas(self):
        """[Exibe uma mensagem de boas vindas]  """

        print(f'Olá {self.nome.title()}! É ótimo ver você!')


eu = Usuario('junior', 'pedroso', 'master', 'python')
dani = Usuario('dani', 'pedroso', 'normal', 'excell')
jose = Usuario('josé', 'de julio', 'visitante', 'clash')

usuarios = [eu, dani, jose]

for i in usuarios:
    print()
    i.descreva_usuario()
    i.boas_vindas()
    print()
