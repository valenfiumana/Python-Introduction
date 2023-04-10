# a) Cargá el contenido del archivo 'portafolio_juan.csv' en un DataFrame de pandas. Llamalo portafolio.
# b) Agregale a portafolio dos columnas nuevas, 'costo_compra' y 'valor_actual', que contengan el costo total de la compra de las acciones de cada fila, y su valor actual. (Recordá que podés operar entre columnas del dataframe (Series) como con arrays de numpy).
# c) Calculá lo que pedía el segundo inciso del ejercicio original (el costo de compra de todas las acciones, el valor actual y la diferencia). ¡Ahora lo podés hacer con por ejemplo con portafolio['costo_compra'].sum(), etc.!
# d) Carga el archivo 'cer-uva-uvi-diarios.csv' en otro dataframe, llamalo df_uvas. Vas a notar que a las fechas las toma por defecto como cadenas. Para convertir la columna a formato datetime usá el método to_datetime() especificando correctamente el formato en que están las fechas. En este caso:
import pandas as pd
import matplotlib.pyplot as plt

portfolio = pd.read_csv('../../../Data/portafolio_juan.csv')

portfolio['costo_compra'] = portfolio['cantidad'] * portfolio['precio_compra']
portfolio['valor_actual'] = portfolio['cantidad'] * portfolio['precio_actual']
print(portfolio, '\n')

costo_total = portfolio['costo_compra'].sum()
valor_total = sum(portfolio['valor_actual'])
print(round(valor_total - costo_total, 2),  '\n')


df_uvas = pd.read_csv('../../../Data/cer-uva-uvi-diarios.csv')
df_uvas['indice_tiempo'] = pd.to_datetime(df_uvas['indice_tiempo'])
print(df_uvas)

df_uvas[-500:].plot.line(x='indice_tiempo', y='cer_diario')
plt.show()