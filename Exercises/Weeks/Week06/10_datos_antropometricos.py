# Explore los datos ANSUR I para mujeres y hombres
# Cree funciones para poder trabajar con los dos conjuntos de datos de la misma forma para:
# <br> a. Leer los datos con NumPy y armar un nuevo array que contenga solamente los pesos y alturas.
# <br> b. Determinar cuáles son los valores máximo, mínimo y promedio de los pesos y alturas para hombres y mujeres por separado.
# <br> c. Estudie si hay correlación entre el peso y la altura para cada conjunto de datos.
#
# Calcular la relación entre altura del torso (sitting height) y longitud de las piernas (se puede calcular como la resta de la altura del torso y la altura total.
# <br> a. ¿Cómo es ese cociente?
# <br> b. ¿Que valores minimo, maximo, promedio, desvio tiene?
# <br> c. ¿Hay correlación entre los dos valores (longitud torso vs longitud de las piernas) para hombres y mujeres?
import numpy as np
ansurWomen = np.genfromtxt('../../../Data/ansurWomen.csv', delimiter=",", skip_header=1)

# explorar los datos: dimensiones, forma, filas, columnas, etc.
print("Shape:", ansurWomen.shape, "Dim:", ansurWomen.ndim)
print(ansurWomen[:,0])
print(ansurWomen[0,:])

# donde está el peso? (weight?) → Index = 124
pesos = ansurWomen[:,124]
print("Pesos de las primeras 10 mujeres de la base de datos:\n", pesos[:10])

# donde está la altura? (stature) → Index = 99
alturas = ansurWomen[:,99]
print("Alturas de las primeras 10 mujeres de la base de datos:\n", alturas[:10])


peso_stats = (pesos.min(), pesos.max(), round(pesos.mean(),4))
altura_stats = (alturas.min(), alturas.max(), round(alturas.mean(),4))
nombres_stats = ('Mínimo','Máximo','Promedio')
print('\n')
print("{:>10} {:>6} {:>8} {:>12}".format("  ", *nombres_stats))
print("{:>10} {:>6} {:>8} {:>12}".format("PESO:", *peso_stats))
print("{:>10} {:>6} {:>8} {:>12}".format("ALTURA:", *altura_stats))


# 2.
# A ansur_file hay que asignarle el path del archivo que se desea analizar.

def ansur(ansur_file):
    ansur = np.genfromtxt(ansur_file, delimiter=",", skip_header=1)
    # Creo la variable datos con:  Columna 1: peso, Columna 2: alturas
    datos = np.transpose(np.stack((ansur[:,124], ansur[:,99])))
    # Tupla con el valor mínimo, máximo y promedio de los pesos respectivamente
    peso_stats = (datos[:,0].min(), datos[:,0].max(), round(datos[:,0].mean(),2))
    # Tupla con el valor mínimo, máximo y promedio de las alturas respectivamente
    altura_stats = (datos[:,1].min(), datos[:,1].max(), round(datos[:,1].mean(),2))
    # Calculo el coeficiente de correlación
    corr = np.corrcoef(datos[:,0], datos[:,1])
    return ansur, datos, peso_stats, altura_stats, corr # la función devuelve 5 variables (valores).

# Ejemplo para ejecutar sobre las mujeres:
asur, datos, peso_stats, altura_stats, corr = ansur('../../../Data/ansurWomen.csv')
# Imprimo una tabla con los datos. (No era necesario mostrarlo de esta forma)
print("Para las Mujeres")
print("{:>15} {:>8} {:>8} {:>10}".format("Característica", "Min", "Máx", "Promedio"))
print("{:>15} {:>8} {:>8} {:>10}".format("PESO:", *peso_stats))
print("{:>15} {:>8} {:>8} {:>10}".format("ALTURA:", *altura_stats))
print(f"Correlación: {corr[0,1]}")


# 3.a.
import matplotlib.pyplot as plt
ansurWomen = np.genfromtxt('../../../Data/ansurWomen.csv', delimiter=",", skip_header=1)

altura_torso = ansurWomen[:,93]
long_piernas = ansurWomen[:,99] - altura_torso
relacion = altura_torso / long_piernas

plt.figure(figsize=(15,5))
plt.plot(relacion)
# Al mirar los valores del cociente "relacion" podemos ver que es ligeramente mayor a 1 para toda la población.
# Esto muestra que la tendencia es que no importa cuales sean la altura del torso y la longitud de las piernas, su cociente se mantiene
# El desvio cuantifica la afirmación "el cociente se mantiene"

# 3.b.
print(f"Promedio: {round(relacion.mean(),2)}, Max: {round(relacion.max(),2)}, Min: {round(relacion.min(),2)}, Desvio: {round(relacion.std(),2)}")

# 3.c.
corr = np.corrcoef(altura_torso, long_piernas)
print(f"Correlación: {round(corr[0,1],4)}")