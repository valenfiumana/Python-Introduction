# Leer estos datos usando Pandas – ojo que no son csv, ni tsv, son de ancho fijo! Tip: ver pd.read_fwf()
# Plotear la representación suavizada del cambio de temperatura como una línea
# Plotear los datos de cambio de temperatura como puntos
# Colorear los puntos en azul si son negativos (< 0) y rojos si son positivos (>=0).

# usando pandas

import pandas as pd

url = 'https://raw.githubusercontent.com/sbu-python-summer/python-tutorial/master/day-4/nasa-giss.txt'
# leemos el archivo directamente con pandas
# fwf = fixed-width format (columnas delimitadas por espaciamiento fijo)
df = pd.read_fwf(url, index_col=0, skiprows=8, header=None)   # index_col = 0 hace que tengamos dicha columna como índice
                                                              #skip_rows ignora ese número de filas antes de los datos
                                                              #header= None evita que use la primera fila de datos como nombres de las columnas

df.rename(columns={1: "Temperatura", 2: "Lowess"}, inplace=True) #renombro las columnas en la misma variable con inplace=True
#print(df.head(5))
#print(len(df.index))

#Generamos dos subconjuntos para luego plotearlos de distintos colores
# temperaturas positivas
pos = df[ df['Temperatura'] >= 0]
# temperaturas negativas
neg = df[ df['Temperatura'] < 0]

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# ploteamos como puntos las temperaturas no-suavizadas
# positivas en rojo
ax.scatter(pos.index, pos["Temperatura"], color="tab:red")
# negativas en azul
ax.scatter(neg.index, neg["Temperatura"], color="tab:blue")

# ploteamos como linea las temperaturas suavizadas
ax.plot(df.index, df["Lowess"], color="black", linewidth=3)

# agregamos algunas etiquetas para decorar
ax.set_xlabel("Años")
ax.set_ylabel("Cambio de Temperatura (°C)")