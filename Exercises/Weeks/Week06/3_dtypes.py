# * Leer la documentación sobre las capacidades de los distintos tipos (dtypes) numéricos que ofrece numpy
# * Con esta información crear arrays de 256x256 usando np.ones (o zeros) usando los siguientes dtypes:
#     * uint8
#     * uint16
#     * uint32
#     * uint64
# * Cuanto ocupan en memoria estos arrays? Expresar en la unidad más conveniente y razonable.
# * Para cada uno de estos arrays, asignar estos valores al primer elemento de cada array (ej array[0][0]) y evaluar el array.
# * Qué pasa en cada caso? Por qué?
#     * 255, 256, 32535, 32536, 4294967295, 4294967296, 18446744073709551615, 18446744073709551616

import numpy as np

a = np.ones((256, 256), dtype=np.uint8)
b = np.ones((256, 256), dtype="uint16")
c = np.ones((256, 256), dtype="uint32")
d = np.ones((256, 256), dtype="uint64")

print(a.itemsize) # 1
print(b.itemsize) # 2
print(c.itemsize) # 4
print(d.itemsize) # 8

# Leo cuanto ocupan en la memoria y lo paso a kilobytes
print("===> Memoria")
print("a %d kilobytes" % ((a.size * a.itemsize) / 1024))
print("b %d kilobytes" % ((b.size * b.itemsize) / 1024))
print("c %d kilobytes" % ((c.size * c.itemsize) / 1024))
print("d %d kilobytes" % ((d.size * d.itemsize) / 1024))
