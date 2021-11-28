import pygal

from exe1500_die import Die

# Cria três dados D6
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Faz alguns lançamentos e armazena os resultados em uma lista
results = [(die_1.roll() + die_2.roll() + die_3.roll())
           for i in range(50000)]

# Analisa os resultados
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualiza os resultados
hist = pygal.Bar()

hist.title = 'Results of rolling thre D6 50000 times.'

# Dois métodos de informar label
# hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

# Este método também funciona
hist.x_labels = list(range(3, 19))

hist.x_title = 'Results'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D6 + D6', frequencies)
hist.render_to_file('dice_visual_thre.svg')
