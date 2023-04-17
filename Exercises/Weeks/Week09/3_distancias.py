# Teniendo en cuenta las distancias de los planetas al Sol - que son en unidades relativas, la distancia Tierra-Sol es 1 (unidades astronómicas), los periodos de sus órbitas (cuanto tardan en dar la vuelta al Sol, en años) y los nombres de los planetas:
#
# * Plotear los períodos vs las distancias de los planetas como puntos y en una escala doble logarítmica (log X, log Y)
# * Escribir el nombre del planeta cerca del punto correspondiente a ese planeta en el plot (puntos adicionales si el texto no se superpone y se lee claro, más puntos adicionales si usan flechas)
# * Trazar dos líneas punteadas (una vertical, una horizontal) que se crucen en el punto de la Tierra en el gráfico.

import matplotlib.pyplot as plt
import numpy as np

distancias = np.array([0.39, 0.72, 1.00, 1.52, 5.20, 9.54, 19.22, 30.06, 39.48])
periodos = np.array([0.24, 0.62, 1.00, 1.88, 11.86, 29.46, 84.01, 164.8, 248.09])
planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Jupiter", "Saturno",
            "Urano", "Neptuno", "Plutón"]

fig, ax = plt.subplots()
ax.scatter(distancias, periodos, facecolor="olive", edgecolor="grey")
ax.set_xlabel("Distancias relativas a la tierra")
ax.set_ylabel("Periodos (años)")
ax.set_xscale("log")
ax.set_yscale("log")

# agrandamos un poco el rango del eje Y para hacer lugar al texto
ax.set_ylim(1, 1000)
# fijo el rango del eje x
ax.set_xlim(1, 50)

# lineas que se cruzan con eje en la tierra: uso los valores máximos de los ejes para que las líneas atraviesen todo el gráfico
ax.vlines(1, color="grey", ymin=0, ymax=1000, linestyle="dashed", alpha=0.5)
ax.hlines(1, color="grey", xmin=0, xmax=50, linestyle="dashed", alpha=0.5)

# hacemos un loop para agregar anotaciones
for i in range(len(planetas)):
    # movemos el texto un poco para que el texto no se superponga
    xtext = distancias[i] - (distancias[i] * 0.2)  # lo corremos 20% a la izquierda
    ytext = periodos[i] + (periodos[i] * 1.2)  # lo corremos 120% hacia arriba
    # agregamos las anotaciones
    ax.annotate(planetas[i], xy=(distancias[i], periodos[i]), xytext=(xtext, ytext),
                size=7, arrowprops=dict(shrink=0.2, width=2, headwidth=7, headlength=4, facecolor="tab:purple"))

    # anotaciones explicadas con comentarios
    # ax.annotate(
    #  planetas[i],                     # <=== el texto
    #  xy=(distancias[i], periodos[i]), # <=== el punto que es el ancla/foco (las coordenadas de los puntos del scatter)
    #  xytext=(xt,yt),                  # <=== la posicion del texto
    #  size=7,                          # <=== tamaño del texto
    #  arrowprops=dict(
    #    shrink=0.05,     # <=== achicamos la flecha esta fraccion de la longitud total (de ambos lados)
    #    width=3,         # <=== el ancho de la flecha (en puntos)
    #    headwidth=7,     # <=== el ancho de la cabeza de la flecha (en puntos)
    #    headlength=4,    # <=== la longitud de la cabeza de la flecha (en puntos)
    #    facecolor="") # retocamos la flecha con este diccionario de propiedades de flecha(arrowprops)
    #  )

plt.show()