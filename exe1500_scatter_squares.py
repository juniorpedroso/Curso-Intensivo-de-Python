import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
    edgecolor='none', s=40)


# Define o título do gráfico e nomeia os eixos
plt.title('Números Quadrados', fontsize = 24)
plt.xlabel('Valores', fontsize=14)
plt.ylabel('Quadrado dos valores', fontsize=14)

# Define o tamanho dos rótulos das marcações
plt.tick_params(axis='both', which='major', labelsize=14)

# Define o intervalo para cada eixo
plt.axis([0, 1100, 0, 1100000])

plt.show()