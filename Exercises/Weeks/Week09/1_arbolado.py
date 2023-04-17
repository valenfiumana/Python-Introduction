# Vamos utilizar el archivo 'arbolado-en-espacios-verdes.csv'
# 1. Realizar un gráfico de puntos que relacione las alturas con los diámetros para las especies (nombre_com) 'Ombú', 'Ceibo' y 'Acacia'. ¿Mantienen todos ellos la misma relación?
# 2. Para las 10 especies de origen exótico con mayor número de ejemplares estudiar las distribuciones de altura, discriminando por especie en diferentes subplots.
# 3. Modificar el programa para que guarde el grafico realizado en el punto 1 en un archivo PDF y el del punto 2 en un archivo JPG.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../../../Data/arbolado-en-espacios-verdes.csv')
#df.info()

# 1.
# Filtrar los datos por especies 'Ombú', 'Ceibo' y 'Acacia'
especies = ['Ombú', 'Ceibo', 'Acacia']                # Lista de valores deseados
df_especies = df[df['nombre_com'].isin(especies)]     # Filtro


plt.figure(figsize=(8, 6))

for especie in especies: # Loop para graficar cada espeie con un color distinto y darle el nombre en la leyenda
    df_especie = df_especies[df_especies['nombre_com'] == especie]
    plt.scatter(df_especie['altura_tot'], df_especie['diametro'], label=especie)

plt.xlabel('Altura Árbol (m)')
plt.ylabel('Diámetro Árbol (cm)')
plt.title('Alturas vs Diámetros de Árboles por Especie')
plt.legend()
#plt.savefig('alturas_diametros_especies.pdf')  # Guardar el gráfico en un archivo PDF
plt.show()

# 2.
# Filtrar por especies de origen exótico
especies_exoticas = df[df['origen'] == 'Exótico']

# Obtener las 10 especies con mayor número de ejemplares
especies_top10 = especies_exoticas['nombre_com'].value_counts().head(10).index.tolist() # el índice de ese output son los nombres

# Crear subplots para cada especie
fig, axes = plt.subplots(nrows=5, ncols=2, figsize=(12, 18)) # en total son 10, por eso 5 rows y 2 cols
axes = axes.flatten()

# Iterar sobre las especies y generar los gráficos en los subplots
for i, especie in enumerate(especies_top10):
    ax = axes[i]
    datos_especie = especies_exoticas[especies_exoticas['nombre_com'] == especie]
    ax.hist(datos_especie['altura_tot'], bins=20, color='skyblue')
    ax.set_title(especie)
    ax.set_xlabel('Altura (m)')
    ax.set_ylabel('Frecuencia')

# Ajustar espacio entre subplots y mostrar el gráfico
plt.tight_layout()
# plt.savefig('grafico_exoticas.jpg', dpi=300)   # 3. Guardar el gráfico en un archivo JPG
plt.show()