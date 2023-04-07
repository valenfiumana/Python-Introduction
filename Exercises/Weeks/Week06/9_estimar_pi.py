# En este ejercicio vamos a estimar π generando puntos al azar.
# La idea consiste en generar puntos al azar (todos con valores de x e y ubicados entre 0 y 1), y ver cuántos de ellos están contenidos dentro del círculo de radio 1 alrededor del punto central (0, 0).
# a) Usando la función de Numpy numpy.random.rand(), generá un array de números al azar de tamaño (10000, 2), que representa 10000 puntos generados al azar.
# b) Usando el array del inciso anterior, contá la cantidad de puntos que caen dentro del cículo (es decir, contá cuántos cumplen que x**2 + y**2 < 1). Luego estimá el valor de π dividiendo ese valor por la cantidad de puntos (o sea, en este caso 10000), y multiplicando el resultado por 4. ¿Dió similar al valor conocido de π?
# c) Creá una función estimar_pi(n) que devuelva una estimación del valor de π como la que hiciste antes pero usando n puntos, donde n es el parámetro de entrada.

import numpy as np
puntos = np.random.rand(10000, 2) # a. array numeros al azar

cantidad = np.count_nonzero(puntos[:,0]**2 + puntos[:,1]**2 < 1) # b. cuántos cumplen que x**2 + y**2 < 1
print('La estimación de Pi dio:', cantidad*4/10000)

# es igual que:
# cantidad = 0
# for punto in puntos:
#   if punto[0]**2 + punto[1]**2 < 1:
#     cantidad += 1

def estimar_pi(n): # c. estimar pi con n puntos
    puntos = np.random.rand(n, 2)
    cantidad = np.count_nonzero(puntos[:, 0] ** 2 + puntos[:, 1] ** 2 < 1)

    return cantidad * 4 / n
print(estimar_pi(10000000))