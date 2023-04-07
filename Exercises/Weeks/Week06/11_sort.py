import numpy as np

# altura en metros de personas
alturas = [1.73, 1.68, 1.71, 1.89, 1.79, 1.76, 1.67]
# peso en Kg de personas
pesos = [65.4, 59.2, 63.6, 88.4, 68.7, 89.7, 73.2]

# ap es el array de pesos y alturas
ap = np.array([ alturas, pesos ])
print("original: \n", ap, "\n")

#       0     1     2     3     4     5     6     <--- Columnas
#  [[ 1.73  1.68  1.71  1.89  1.79  1.76  1.67]]   --- Fila 0
#  [[65.4  59.2  63.6  88.4  68.7  89.7  73.2 ]]]  --- Fila 1


# obtengo los indices ordenados usando argsort()
indices_ordenados_alturas = ap[0,:].argsort()
indices_ordenados_pesos   = ap[1,:].argsort()
print("Alturas ordenadas (indices): \n", indices_ordenados_alturas )
print("Pesos ordenados (indices): \n", indices_ordenados_pesos )

# ahora ordenamos el array usando estos indices ordenados
# por altura
personas_ordenadas_por_altura = ap[ :, indices_ordenados_alturas ]
print("Ordenadas por altura:\n", personas_ordenadas_por_altura)

# por peso
personas_ordenadas_por_peso = ap[ :, indices_ordenados_pesos ]
# == ap[ :, ap[1,:].argsort() ]
# == ap[ :, np.argsort(ap[1,:]) ]
print("Ordenadas por peso:\n", personas_ordenadas_por_peso)
