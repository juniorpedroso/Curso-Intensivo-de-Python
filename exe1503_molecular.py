import matplotlib.pyplot as plt

from exe1500_random_walk import RandomWalk

# Continua criando novos passeios enquanto o programa estiver ativo
while True:
    # Cria um passeio aleatório e plota os pontos

    # Removendo os eixos
    plt.rcParams['axes.spines.right'] = False
    plt.rcParams['axes.spines.top'] = False

    rw = RandomWalk(5000)
    rw.fill_walk()

    # Define o tamanho da janela de plotagem
    plt.figure(figsize=(10, 6))

    # Plota os pontos e mostra o gráfico

    plt.plot(rw.x_values, rw.y_values, linewidth=1)

    # Enfatiza o primeiro e o último ponto
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red',
                edgecolors='none', s=100)

    plt.show()

    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break
