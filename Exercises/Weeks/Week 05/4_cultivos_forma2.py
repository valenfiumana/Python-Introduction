# Otra forma de resolverlo podria ser crear un diccionario por cultivo y guardar todas las informaciones relevantes
# en una lista de diccionarios. De esta forma, podemos acceder a las informaciones por el nombre de las columnas
# y no necesitamos conocer los indices.
# Nota: este ejercicio se puede resolver con Pandas, en la semana 8 veremos Pandas!
import csv

with open("../../../Data/estimaciones-agricolas-PBA-1969-2022.csv") as f:
    filas = csv.reader(f)
    encabezados = next(filas)
    datos = []
    for fila in filas:
        datos.append(fila)
    # Crear un diccionario con los datos agrupados por tipo de cultivo
    datos_por_cultivo = {}
    for fila in datos:
        cultivo = fila[1]
        if cultivo not in datos_por_cultivo:
            datos_por_cultivo[cultivo] = []
        datos_por_cultivo[cultivo].append(dict(zip(encabezados[2:10],fila[2:10])))
    print(datos_por_cultivo['Ajo'])

    # i: contar los tipos de cultivos diferentes
    num_cultivos = len(datos_por_cultivo)
    print(f'Hay {num_cultivos} tipos de cultivos diferentes registrados en la Provincia de Buenos Aires.')

    #ii: encontrar el principal municipio productor de Ajo y los años de mayor superficie sembrada y rendimiento
    cultivo_ajo = 'Ajo'
    mayor_superficie_sembrada_ajo = None
    mayor_rendimiento_ajo = None
    municipio_productor_ajo = None

    for fila in datos_por_cultivo[cultivo_ajo]:
    # ATENCION:  Por como está construido el archivo, cuando hacemos en encabezado superficie_sembrada queda con
    # espacio a mas, y por eso no funciona... hay que llamarla así: 'superficie_sembrada ' y no 'superficie_sembrada'
    # porque no es la misma cadena.
        if mayor_superficie_sembrada_ajo is None or float(fila['superficie_sembrada ']) > float(mayor_superficie_sembrada_ajo['superficie_sembrada ']):
            mayor_superficie_sembrada_ajo = fila
            municipio_productor_ajo = fila['municipio_nombre']
        if mayor_rendimiento_ajo is None or float(fila['rendimiento']) > float(mayor_rendimiento_ajo['rendimiento']):
            mayor_rendimiento_ajo = fila
    print(f'El principal municipio productor de {cultivo_ajo} en la Provincia es {municipio_productor_ajo}.')
    print(f'El año de mayor superficie sembrada fue {mayor_superficie_sembrada_ajo["campania_nombre"]}.')
    print(f'El año de mayor rendimiento fue {mayor_rendimiento_ajo["campania_nombre"]}.')


    # Consulta iii: encontrar los mejores años para cada cultivo
    mejor_superficie_sembrada = {}
    mejor_rendimiento = {}
    for cultivo in datos_por_cultivo:
        mayor_superficie_sembrada = None
        mayor_rendimiento_cultivo = None
        for fila in datos_por_cultivo[cultivo]:
            if mayor_superficie_sembrada is None or float(fila['superficie_sembrada ']) > float(mayor_superficie_sembrada['superficie_sembrada ']):
                mayor_superficie_sembrada = fila
            if mayor_rendimiento_cultivo is None or float(fila['rendimiento']) > float(mayor_rendimiento_cultivo['rendimiento']):
                mayor_rendimiento_cultivo = fila
        mejor_superficie_sembrada[cultivo] = mayor_superficie_sembrada['campania_nombre']
        mejor_rendimiento[cultivo] = mayor_rendimiento_cultivo['campania_nombre']
    print('Los mejores años para cada cultivo son:')
    for cultivo in mejor_superficie_sembrada:
        print(f'{cultivo:<20} Superficie sembrada - {mejor_superficie_sembrada[cultivo]:<20} Rendimiento - {mejor_rendimiento[cultivo]}')

