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


class Admin(Usuario):
    """[Representa aspectos específicos de um Usuário]

    Args:
        Usuario ([type]): [description]
    """
    def __init__(self, nome, sobrenome, nivel_acesso, linguagem):
        """[Inicializa os atributos da classe-pai]

        Args:
            nome ([type]): [description]
            sobrenome ([type]): [description]
            nivel_acesso ([type]): [description]
            linguagem ([type]): [description]
        """
        super().__init__(nome, sobrenome, nivel_acesso, linguagem)
        self.privileges = ['can add post',
                            'can delete post',
                            'can ban user',
                            ]
    def show_privileges(self):
        for privilege in self.privileges:
            print(f'- {privilege}')


eu = Usuario('junior', 'pedroso', 'admin', 'python')
dani = Usuario('dani', 'pedroso', 'normal', 'excell')
jose = Usuario('josé', 'de julio', 'visitante', 'clash')

usuarios = [eu, dani, jose]

for i in usuarios:
    print()
    i.descreva_usuario()
    i.boas_vindas()
    print()

print()
me = Admin('junior', 'pedroso', 'master', 'python')
print('privileges')
me.show_privileges()