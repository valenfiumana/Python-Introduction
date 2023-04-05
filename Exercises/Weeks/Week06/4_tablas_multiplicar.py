#  a. Crear un array conteniendo todos los números pares del 0 al 1000.
# b. Crear un array de (10, 10) conteniendo las tablas de multiplicar.
# Es decir, la primer fila es la tabla del 1, la segunda la del 2, etc.

import numpy as np

pares = np.arange(2, 1002, 2)

def mult_table(n):
    rng = np.arange(1, n+1) # [ 1  2  3  4  5  6  7  8  9 10]
    return rng * rng[:, None]
    # rng[:, None] =
    # [[ 1]
    #  [ 2]
    #  [ 3]
    #  [ 4]
    #  [ 5]
    #  [ 6]
    #  [ 7]
    #  [ 8]
    #  [ 9]
    #  [10]]

print(mult_table(10))