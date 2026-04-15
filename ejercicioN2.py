# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Prof.Ing.Jesús González
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
import numpy as np
import matplotlib.pyplot as plt

def multi_plot():
    # Dibujar múltiples líneas en un mismo gráfico
    
    x = list(np.linspace(-4, 4, 20))

    y1 = []
    for i in x:
        y1.append(i**2)

    y2 = []
    for i in x:
        y2.append(i**3)
    
    fig = plt.figure()
    ax = fig.add_subplot()

    ax.plot(x, y1, color='green', marker='^', label='y1 = x**2')
    ax.plot(x, y2, color='red', marker='+', label='y2 = x**3')
    
    ax.set_facecolor('whitesmoke')
    ax.set_title("Dos funciones juntas")
    ax.set_ylabel("Y[amplitud]")
    ax.set_xlabel("X[rads]")
    ax.set_xlim([-4, 4])
    ax.set_ylim([-64, 64])
    ax.legend()
      
    plt.show()


if __name__ == '__main__':
    print("Bienvenidos a otra clase con Python")
    print("Line Plot")

    # NOTA: aproveche los ejemplos "multi_line_plot" de clase

    # Se desea graficar varias funciones en un mismmo gráfico (axe)

    # Las funciones que se desean implementar y graficar son:
    # y1 = x**2
    # y2 = x**3

    x = list(np.linspace(-4, 4, 20))

    y1 = []
    for i in x:
        y1.append(i**2)

    y2 = []
    for i in x:
        y2.append(i**3)

    # Crear figura
    fig = plt.figure()
    ax = fig.add_subplot()

    # Graficar ambas funciones
    ax.plot(x, y1, color='blue', marker='o', label='y = x**2')
    ax.plot(x, y2, color='orange', marker='x', label='y = x**3')

    # Estética
    ax.set_title("Funciones y = x^2 e y = x^3")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_facecolor('whitesmoke')
    ax.grid()

    # Leyenda
    ax.legend()

    # Mostrar
    plt.show()

    print("terminamos")