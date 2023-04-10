# Leer el archivo de datos llamado [estaciones_metereologicas.csv] como un un dataframe de Pandas. A partir de este vamos a:
# * Mostrar las primeras filas del dataframe.
# * Mostrar el número total de filas y columnas.
# * Calcular la media, desviación estándar, valor mínimo y valor máximo de la columna 'altura'.
import pandas as pd
df_est = pd.read_csv('../../../Data/estaciones_metereologicas.csv')
print(df_est.head(1))

print(df_est.shape)

altMax = df_est['ALTURA'].max() # 3459
altMin = df_est['ALTURA'].min() # 5
altAvg = round(df_est['ALTURA'].mean(), 2) # 331.51
altStd = round(df_est['ALTURA'].std(), 2) # 456.74
