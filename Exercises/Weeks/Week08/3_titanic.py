# Un conjunto de datos (dataset) muy usado para ejercitar Pandas es el archivo [titanic.csv](../Data/titanic.csv), que contiene información sobre los pasajeros del Titanic, con la descripción de las variables que se puede encontrar aquí. Para este dataset hacer un programa que:
# * Carge los datos en un DataFrame y explorarlos
# * Muestre en pantalla las dimensiones, el número de datos que contiene y que muestre los tipos de datos de cada columna.
# * Muestre en pantalla los datos del pasajero con identificador 148.
# * Encuentre los nombres de las personas que iban en primera clase y los muestre ordenados alfabéticamente.
# * Elimine del DataFrame los pasajeros/as con edad desconocida.
# * Determine la edad media de las mujeres que viajaban en la clase 1.
# * Haga un histograma de la distribución de edades de los sobrevivientes sin distinguir el genero.

import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv('../../../Data/titanic.csv')

titanic.info()

print('\n\n', titanic.shape) # dimensiones

id148 = titanic[ titanic['IdPasajero'] == 148] # pasajeros con id 148
print('\n\n', id148)

primeraClase = titanic[titanic['Clase']==1]['Nombre'].sort_values() # nombres alfabeticos de primera clase
print('\n\n', primeraClase)

titanic.dropna(inplace=True, axis=0) # eliminar edades no nulas
print('\n\n', titanic['Edad'])

mujeresPrimeraClase = titanic[(titanic['Clase']==1) & (titanic['Genero']=='female')]['Edad'].mean() # edad promedio mujeres 1 clase
print('\n\n', round(mujeresPrimeraClase, 2))

plt.hist(titanic['Edad'], bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 99])
plt.show()