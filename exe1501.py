import matplotlib.pyplot as plt

# Define dados
x_valores = [1, 2, 3, 4, 5]
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

# Exibe o plot
plt.show()
