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
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """[Devolve um nome descritivo, formatado de modo elegante] """

        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def read_odometer(self):
        """[Exibe uma frase que mostra a milhagem do carro]
        """
        print(f'Este carro está com {self.odometer_reading} Km.')

    def update_odometer(self, kilometragem):
        """[Define o valor de leitura do hodometro com o valor especificado
        Rejeita a alteração se for tentativa de definir um valor menor
            para o hodômetro]

        Args:
            kilometragem ([int]): [km atual]
        """
        if kilometragem >= self.odometer_reading:
            self.odometer_reading = kilometragem
        else:
            print('Você não pode voltar o hodômetro!')

    def increment_odometer(self, kilometragem):
        """[Soma a quantidade especificada ao valor de leitura
        do hodômetro]

        Args:
            kilometragem ([type]): [description]
        """
        if kilometragem > 0:
            self.odometer_reading += kilometragem
        else:
            print('Você não pode voltar o hodômetro!')


class EletricCar(Car):
    """[Representa aspectos específicos de veículos elétricos]

    Args:
        Car ([type]): [description]
    """

    def __init__(self, make, model, year):
        """[Inicializa os atributos da classe-pai]

        Args:
            make ([type]): [description]
            model ([type]): [description]
            year ([type]): [description]
        """
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """[Exibe uma frase que descreve a capacidade da bateria.]
        """
        print(f'This car has a {self.battery_size}-kWh battery.')


my_tesla = EletricCar('tesla', 'model s', 2016)

print()
print(my_tesla.get_descriptive_name())
print(my_tesla.describe_battery())
print()
