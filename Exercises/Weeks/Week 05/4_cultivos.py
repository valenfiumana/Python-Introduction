import csv

with open("../../../Data/estimaciones-agricolas-PBA-1969-2022.csv") as f:
    filas = csv.reader(f)
    encabezados = next(filas)
    datos = []
    for fila in filas:
        datos.append(fila)

print(encabezados)
print(datos[0])
print(len(datos))

# i. Cuántos tipos de cultivos diferentes hay registrados en la Provincia de Buenos Aires?
cultivos = []
for fila in datos:
    cultivos.append(fila[1])

cultivos_unicos = set(cultivos) # Convertir lista en conjunto para obtener cultivos únicos

num_cultivos = len(cultivos_unicos) # Calcular longitud para obtener número de cultivos diferentes
print(f'Hay {num_cultivos} tipos de cultivos diferentes registrados en la Provincia de Buenos Aires.')


# ii. Cuál es el principal municipio productor de Ajo en la Provincia?
# y cuál fue el año de mayor superficie sembrada? Y el año de mayor rendimiento?
mayor_superficie_sembrada = None
mayor_rendimiento = None

for fila in datos:
    if fila[1] == 'Ajo':
        # Encontrar la fila con la mayor superficie sembrada
        if mayor_superficie_sembrada is None or float(fila[6]) > float(mayor_superficie_sembrada[6]):
            mayor_superficie_sembrada = fila
        # Encontrar la fila con el mayor rendimiento
        if mayor_rendimiento is None or float(fila[9]) > float(mayor_rendimiento[9]):
            mayor_rendimiento = fila

print(mayor_superficie_sembrada,mayor_rendimiento)
municipio = mayor_superficie_sembrada[5] # municipio de mayor superficie sembrada
anio_superficie = mayor_superficie_sembrada[3] # campaña de mayor superficie sembrada
anio_rendimiento = mayor_rendimiento[3] # campaña del mayor rendimiento

print(f'El principal municipio productor de Ajo en la Provincia es {municipio} y el año de mayor superficie sembrada fue en {anio_superficie}.')
print(f'El año de mayor rendimiento para el cultivo de Ajo fue en {anio_rendimiento}.')

# iii. Repetí el punto ii para todos los cultivos.
# Cuáles son los mejores años en la Provincia? Coinciden para todos los cultivos?
# Para repetir la consulta ii para todos los cultivos, podemos utilizar un bucle
# que recorra todos los cultivos y luego dentro de ese bucle aplicar la misma lógica que en la consulta ii.

mejor_superficie_sembrada = {}
mejor_rendimiento = {}

for cultivo in cultivos_unicos:
    mayor_superficie_sembrada = None
    mayor_rendimiento_cultivo = None

    for fila in datos:
        if fila[1] == cultivo:
            # Encontrar la fila con la mayor superficie sembrada
            if mayor_superficie_sembrada is None or float(fila[6]) > float(mayor_superficie_sembrada[6]):
                mayor_superficie_sembrada = fila
            # Encontrar la fila con el mayor rendimiento
            if mayor_rendimiento_cultivo is None or float(fila[9]) > float(mayor_rendimiento_cultivo[9]):
                mayor_rendimiento_cultivo = fila
    # Guardar la información del mejor año para este cultivo
    mejor_superficie_sembrada[cultivo] = mayor_superficie_sembrada[3]
    mejor_rendimiento[cultivo] = mayor_rendimiento_cultivo[3]

print('Los mejores años para cada cultivo son:')
for cultivo in cultivos_unicos:
    print(f'{cultivo:<20} Superficie sembrada - {mejor_superficie_sembrada[cultivo]:<20} Rendimiento - {mejor_rendimiento[cultivo]}')


