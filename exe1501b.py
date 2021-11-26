import matplotlib.pyplot as plt

# x_valores = [x for x in range(1, 5001)]
x_valores = list(range(5001))
y_cubo = [x**3 for x in x_valores]

# Criando o plot
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_valores, y_cubo, edgecolors='none', s=40)

# Define o título do gráfico e nomeia os eixos
plt.title('Números Cubos', fontsize=24)
plt.xlabel('Valores', fontsize=14)
plt.ylabel('Cubo dos valores', fontsize=14)

# Define o tamanho dos rótulos das marcações
plt.tick_params(axis='both', labelsize=14)

# Define o intervalo para cada eixo
plt.axis([0, 5100, 0, 5100**3])

plt.show()