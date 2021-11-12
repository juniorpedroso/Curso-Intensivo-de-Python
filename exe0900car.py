class Car():
    """[Uma tentativa simples de representar um carro] 
    """

    def __init__(self, make, model, year):
        """[Inicializa os atribuitos que descrevem um carro]

        Args:
            make ([type]): [description]
            model ([type]): [description]
            year ([type]): [description]
        """
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """[Devolve um nome descritivo, formatado de modo elegante] """

        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()


my_new_car = Car('audi', 'a4', 2016)
meu_jeep = Car('jeep', 'renegade', 2018)
carro_zé = Car('toyota', 'corolla', 2020)

carros = [my_new_car, meu_jeep, carro_zé]

for carro in carros:
    print()
    print(carro.get_descriptive_name())
    print()
