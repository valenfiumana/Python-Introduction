# * Crear un par de arrays de 3 x 3 y de 256 x 256 con valores enteros usando ones and zeros, respectivamente.
# * Leer la documentación de los métodos numpy para ndarrays itemsize y size – numpy.ndarray.itemsize, numpy.ndarray.size.
# * Para los arrays creados antes, qué información me da itemsize? Y size? En qué unidades está cada uno?
# * Sabiendo esto, calcular el espacio que ocupan en memoria, sabiendo que
# 1024 bytes = 1 kilobyte; 1024 kilobytes = 1 megabyte; 1024 megabytes = [...] etc. Expresar en la unidad más conveniente y razonable.

import numpy as np

a = np.ones((3, 3), dtype=int)
b = np.zeros((256, 256), dtype=int)

print(a.itemsize) # 8 bytes
print(a.size) # 3 x 3 = 9 elements

print(b.itemsize) # 8 bytes
print(b.size) # 256 x 256 = 65536 elements

