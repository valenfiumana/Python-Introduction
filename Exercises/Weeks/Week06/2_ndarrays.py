# a. Crear un array de 1D con los números del 0 al 9
# b. Crear un array de 3x3 booleano con el valor True
# c. Extraer todos los números impares en el array creado en el punto a.
# d. Substituir todos los números imapares en el array creado en el punto a por -1.
# e. Convierta el array creado en el punto a. para un array de 2D con 2 lineas.
import numpy as np

a = np.arange(10) # [0 1 2 3 4 5 6 7 8 9]

b = np.full((3, 3), True)
# [[ True  True  True]
#  [ True  True  True]
#  [ True  True  True]]

b2 = np.ones((3, 3), dtype=bool) # Al ser tipo bool, muestra los 1 como True y los 0 como False

c = np.array( a[a % 2 != 0] ) # [1 3 5 7 9]

d = np.where(a % 2 != 0, -1, a) # [ 0 -1  2 -1  4 -1  6 -1  8 -1]
d2 = a[a % 2 == 1] = -1

e = np.reshape(a, (2, 5)) # [[0 1 2 3 4]
                        # [5 6 7 8 9]]

e2 = np.reshape(arr_a, (2, -1)) # Cambiamos la forma del array. (2,-1) es el nuevo tamaño que se le quiere dar.
                                # El primer número de la tupla (2) pide que el primer eje tenga dos elementos.
                                # El segundo número de la tupla (-1) indica que numpy calcule el tamaño del segundo eje, teniendo en cuenta el tamaño original de arra_a