import numpy as np
import matplotlib.pyplot as plt

n = int(input('Qual o valor de n desejado? ' ))
l = 100

x = np.linspace(0, 100)
y = (2/l) * (np.sin((n*np.pi*x)/l)) * (np.sin((n*np.pi*x)/l))

plt.title('Gráfico da função de onda ao quadrado para n = {}'.format(n))
plt.plot(x,y, color = 'Red')
plt.xlabel('x (pm)')
plt.ylabel('$\psi²$', rotation = 0)
plt.savefig('graf_onda{}.jpg'.format(n))
plt.show()
