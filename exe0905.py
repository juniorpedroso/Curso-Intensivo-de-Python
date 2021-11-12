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
        self.login_attempts = 0

    def descreva_usuario(self):
        """[Descreve o usuário]"""

        print(f'Usuário: {self.nome.title()} {self.sobrenome.title()}')
        print(f'Nível de acesso: {self.nivel_acesso.upper()}')
        print(f'Linguagem: {self.linguagem.title()}')

    def boas_vindas(self):
        """[Exibe uma mensagem de boas vindas]  """

        print(f'Olá {self.nome.title()}! É ótimo ver você!')

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0


eu = Usuario('junior', 'pedroso', 'master', 'python')

print()
eu.descreva_usuario()
eu.increment_login_attempts()
eu.boas_vindas()
print(f'Este é o seu {eu.login_attempts}º acesso hoje.')
print()

eu.descreva_usuario()
eu.increment_login_attempts()
eu.boas_vindas()
print(f'Este é o seu {eu.login_attempts}º acesso hoje.')
print()

eu.descreva_usuario()
eu.increment_login_attempts()
eu.boas_vindas()
print(f'Este é o seu {eu.login_attempts}º acesso hoje.')
print()

print('Hoje é um novo dia!')
eu.reset_login_attempts()
eu.descreva_usuario()
eu.increment_login_attempts()
eu.boas_vindas()
print(f'Este é o seu {eu.login_attempts}º acesso hoje.')
print()
