
import numpy as np

import matplotlib.pyplot as plt

def sigmoid(z):
    #return 1.0/(1.0+np.exp(-z))
    return 1.0/(1.0+np.exp(-z))

# Função para retornar as derivadas da função Sigmóide
def sigmoid_prime(z):
    return sigmoid(z)*(1-sigmoid(z))

lista1=np.arange(0.0, 30.0, 0.1)
lista2=[]
lista3=[]
print(lista1)

num=sigmoid(np.arange(0.0, 30.0, 0.1))
print(num)
lista2=(num)

num_derivada=sigmoid_prime(np.arange(0.0, 30.0, 0.1))
print(num_derivada)
lista3=(num_derivada)

plt.plot(lista1,lista2)
plt.plot(lista1,lista3)
plt.show()
