# a) Hacer un código que cree una lista con las alturas de los arboles (columna 'altura_tot') de una determinada especie (por ejemplo, probar con 'Jacarandá' de la columna 'nombre_com').
# b) ¿Cuántos espacios verdes diferentes podemos encontrar en CABA?
# c) Crear un DataFrame que contenga solo los Ceibos del parque 'CENTENARIO'. Reajustá los índices del mismo.

import pandas as pd

arboles = pd.read_csv('../../../Data/arbolado-en-espacios-verdes.csv')

jacarandas = arboles[ arboles['nombre_com'] == 'Jacarandá'] #
jacarandasH = jacarandas['altura_tot'].unique() # creo lista con alturas no repetidas
print(jacarandasH)

esp_verdes = len(arboles['espacio_ve'].unique())
print(esp_verdes)

df = arboles[(arboles['nombre_com'] == 'Ceibo') & (arboles['espacio_ve'] == 'CENTENARIO')]
print(df)