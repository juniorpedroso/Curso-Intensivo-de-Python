from random import randint


class Die():

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        resultado = randint(1, self.sides)
 #       print(f'Jogando um dado de {self.sides} lados.')
        print(f'O resultado foi {resultado}')


dado_6 = Die(6)
dado_10 = Die(10)
dado_20 = Die(20)

print()
print('Vou jogar um dado de 6 lados')
for i in range(1, 10):
    dado_6.roll_die()
print()
print('Vou jogar um dado de 10 lados')
for i in range(1, 10):
    dado_10.roll_die()
print()
print('Vou jogar um dado de 20 lados')
for i in range(1, 10):
    dado_20.roll_die()
