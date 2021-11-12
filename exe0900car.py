class Car():
    """[Uma tentativa simples de representar um carro] """

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
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    my_new_car = Car('audi', 'a4', 2016)
    print(my_new_car.get_descriptive_name())
