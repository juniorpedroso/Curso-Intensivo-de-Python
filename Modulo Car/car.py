"""[Uma Classe que pode ser usada para representar um carro]"""


class Car():
    """[Uma tentativa simples de representar um carro]"""

    def __init__(self, make, model, year):
        """[Inicializa os atribuitos que descrevem um carro] """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """[Devolve um nome descritivo, formatado de modo elegante] """
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def read_odometer(self):
        """[Exibe uma frase que mostra a milhagem do carro]"""
        print(f'Este carro está com {self.odometer_reading} Km.')

    def update_odometer(self, kilometragem):
        """[Define o valor de leitura do hodometro com o valor especificado
        Rejeita a alteração se for tentativa de definir um valor menor
            para o hodômetro]"""
        if kilometragem >= self.odometer_reading:
            self.odometer_reading = kilometragem
        else:
            print('Você não pode voltar o hodômetro!')

    def increment_odometer(self, kilometragem):
        """[Soma a quantidade especificada ao valor de leitura
        do hodômetro]"""
        if kilometragem > 0:
            self.odometer_reading += kilometragem
        else:
            print('Você não pode voltar o hodômetro!')


class Battery():
    """[Uma tentativa simples de modelar uma bateria para um carro elétrico]"""

    def __init__(self, battery_size=70):
        """[Inicializa os atributos da bateria]

        Args:
            battery_size (int, optional): [description]. Defaults to 70.
        """
        self.battery_size = battery_size

    def describe_battery(self):
        """[Exibe uma frase que descreve a capacidade da bateria.]"""
        print(f'This car has a {self.battery_size}-kWh battery.')

    def get_range(self):
        """[Exibe uma frase sobre a distância que o carro é summary]
        """
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = f'This car can go approximately {range} ' + \
            'miles on a full charge.'
        print(message)

    def upgrade_battery(self):
        """[Este método faz um upgrade na bateria aumentando para 85]"""
        if self.battery_size == 70:
            self.battery_size = 85
            print("Upgraded the battery to 85 kWh.")
        else:
            print("The battery is already upgraded.")


class EletricCar(Car):
    """[Representa aspectos específicos de veículos elétricos]"""

    def __init__(self, make, model, year):
        """[Inicializa os atributos da classe-pai]

        Args:
            make ([type]): [description]
            model ([type]): [description]
            year ([type]): [description]
        """
        super().__init__(make, model, year)
        self.battery = Battery()
