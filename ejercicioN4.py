# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Prof.Ing.Jesús González
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

import numpy as np
import matplotlib.pyplot as plt

def grid():
    x = np.linspace(0, 10, 40)

    y1 = x**2
    y2 = x**3
    y3 = x**4
    y4 = np.sqrt(x)

    fig = plt.figure()
    fig.suptitle('Grilla con 4 funciones', fontsize=16)

    # Crear 4 subplots (2 filas, 2 columnas)
    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2)
    ax3 = fig.add_subplot(2, 2, 3)
    ax4 = fig.add_subplot(2, 2, 4)

    # Gráfico 1
    ax1.plot(x, y1, color='blue', label='y = x^2')
    ax1.set_title("y = x^2")
    ax1.grid()
    ax1.legend()

    # Gráfico 2
    ax2.plot(x, y2, color='green', label='y = x^3')
    ax2.set_title("y = x^3")
    ax2.grid()
    ax2.legend()

    # Gráfico 3
    ax3.plot(x, y3, color='red', label='y = x^4')
    ax3.set_title("y = x^4")
    ax3.grid()
    ax3.legend()

    # Gráfico 4
    ax4.plot(x, y4, color='purple', label='y = sqrt(x)')
    ax4.set_title("y = sqrt(x)")
    ax4.grid()
    ax4.legend()

    plt.show()


if __name__ == '__main__':
    print("Bienvenidos a otra clase con Python")
    print("Line Plot: Figura con múltiples gráficos")

    x = np.linspace(0, 10, 40)

    y1 = x**2
    y2 = x**3
    y3 = x**4
    y4 = np.sqrt(x)

    # Crear figura
    fig = plt.figure()
    fig.suptitle('4 funciones en grilla', fontsize=16)

    # Subplots 2x2
    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2)
    ax3 = fig.add_subplot(2, 2, 3)
    ax4 = fig.add_subplot(2, 2, 4)

    # Graficar
    ax1.plot(x, y1, color='blue', label='y = x^2')
    ax2.plot(x, y2, color='green', label='y = x^3')
    ax3.plot(x, y3, color='red', label='y = x^4')
    ax4.plot(x, y4, color='purple', label='y = sqrt(x)')

    # Estética
    for ax in [ax1, ax2, ax3, ax4]:
        ax.grid()
        ax.set_facecolor('whitesmoke')
        ax.legend()

    plt.show()

    print("terminamos")