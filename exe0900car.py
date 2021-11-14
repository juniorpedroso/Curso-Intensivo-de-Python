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


my_new_car = Car('audi', 'a4', 2016)
my_new_car.update_odometer(50000)
meu_jeep = Car('jeep', 'renegade', 2018)
meu_jeep.update_odometer(30000)
carro_zé = Car('toyota', 'corolla', 2020)
carro_zé.update_odometer(5000)

carros = [my_new_car, meu_jeep, carro_zé]

for carro in carros:
    print()
    print(carro.get_descriptive_name())
    carro.read_odometer()
    print()

print('Tentando voltar o hodômetro do Audi.')
my_new_car.update_odometer(10000)
print()

print('Adicionando 500 km no Jeep')
meu_jeep.increment_odometer(500)
meu_jeep.read_odometer()
print()

print('Tentando diminuir 300 km no Toyota')
carro_zé.increment_odometer(-300)
carro_zé.read_odometer()
print()
