import numpy as np
import matplotlib.pyplot as plt

def calcula_media(x):
    x_media = sum(x) / len(x)
    return x_media

def calcula_coeficientes(x, y):
    x_media = calcula_media(x)
    y_media = calcula_media(y)
    soma_xy = 0
    soma_x = 0
    for i in range(len(x) - 1):
        soma_xy += (x[i] - x_media) * y[i]
        soma_x += (x[i] - x_media)**2

    a = soma_xy / soma_x
    b = y_media - (a * x_media)
    return a, b

def imprime_equacao(a, b, n):
    print(">>A equação linear para o capacitor {} é:".format(n))
    print("         v = {:0.3f}t + {:0.3f}".format(a2, b2))
    return

def imprime_grafico(a, b, x, n):
    f = a*x + b

    plt.title('Gráfico do capacitor {}'.format(n))
    plt.plot(x,f, color = 'Red')
    plt.xlabel('t (s)')
    plt.ylabel('v (V)', rotation = 0)
    plt.savefig('graf_cap{}.jpg'.format(n))
    plt.show()
    return

if __name__ == '__main__':
    #Capacitor 2
    t2 = np.array([0.5, 1.0, 1.5, 1.90, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 11.0, 14, 17, 20])
    v2 = np.array([1.12, 2.03, 3.63, 4.33, 6.08, 7.40, 8.22, 9.20, 9.7, 10.13, 10.51, 11.04, 11.47, 11.65, 11.75])

    a2, b2 = calcula_coeficientes(t2, v2)
    imprime_equacao(a2, b2, 2)
    imprime_grafico(a2, b2, t2, 2)
    print("\n")
    
    #Capacitor 1
    t1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 20, 25, 30])
    v1 = np.array([1.4, 2.28, 3.46, 4.48, 5.37, 6.14, 6.82, 7.41, 7.75, 8.29, 8.7, 9, 9.3, 9.57, 10, 10.53, 10.53, 10.88, 11.03])

    a1, b1 = calcula_coeficientes(t1, v1)
    imprime_equacao(a1, b1, 1)
    imprime_grafico(a1, b1, t1, 1)
