# Realiza una función separar(lista) que tome una lista de números enteros y devuelva dos listas ordenadas.
# La primera con los números pares y la segunda con los números impares.
import numpy as np
def separar(lista):
    a = np.array(lista)
    pares = a[a%2==0]
    impares = a[a%2!=0]

    return pares, impares

print(separar([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))