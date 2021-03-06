import pygal

from exe1500_die import Die

# Cria um D6
die = Die()

# Faz alguns lançamentos e armazena os resultados em uma lista
results = [die.roll() for i in range(1000)]

# Analisa os resultados
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualiza os resultados
hist = pygal.Bar()

hist.title = 'Results of rolling one D6 1000 times.'
hist.x_labels = ['1', '2', '3', '4', '5', '6']

# Este método também funciona
# hist.x_labels = map(str, range(1, 7)) 

hist.x_title = 'Resultados'
hist.y_title = 'Frequency of Result'

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
