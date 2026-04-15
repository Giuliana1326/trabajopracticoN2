# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Prof.Ing.Jesús González
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
import numpy as np
import matplotlib.pyplot as plt

def scatter_plot():
    # Demostración de la utilidad del scatter plot
    sample_size = 20
    x = np.arange(-np.pi, np.pi, 0.1)
    y = np.tanh(x)

    fig = plt.figure()
    fig.suptitle('Scatter', fontsize=16)
    ax2 = fig.add_subplot(1, 2, 2)

    ax2.scatter(x, y, c='darkcyan')
    ax2.set_facecolor('whitesmoke')
    ax2.grid('solid')
    plt.show()
    

if __name__ == '__main__':
    print("Bienvenidos a otra clase con Python")
    print("Scatter Plot")

    # NOTA: aproveche los ejemplos "scatter_plot" de clase

    x = np.arange(-np.pi, np.pi, 0.1)
    y = np.tanh(x)

    # Crear figura
    fig = plt.figure()
    fig.suptitle('Grafico Scatter y = tanh(x)', fontsize=12)

    # Crear eje
    ax = fig.add_subplot()

    # Graficar scatter
    ax.scatter(x, y, color='blue', marker='o', label='y = tanh(x)')

    # Etiquetas
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    # Estilo
    ax.set_facecolor('whitesmoke')
    ax.grid()

    # Leyenda
    ax.legend()

    # Mostrar gráfico
    plt.show()

    print("terminamos")