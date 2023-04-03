import csv

with open('../../../Data/portafolio_juan.csv', 'r', encoding='UTF8') as f:
    filas = csv.reader(f)
    keys = next(filas)  # headers
    acciones = []
    for fila in filas:
        # a. lista de diccionarios
        acciones.append(dict(zip(keys, fila)))
    print(acciones)

    # b. precio y cantidad acciones
    costo_compra = 0
    valor_actual = 0
    for accion in acciones:
        valor_actual += int(accion['cantidad']) * float(accion['precio_actual'])
        costo_compra += int(accion['cantidad']) * float(accion['precio_compra'])
    resumen = valor_actual - costo_compra
    if (resumen > 0):
        print(f'Juan tiene una ganancia de ${round(resumen, 2)}')
    else:
        print(f'Juan tiene una perdida de ${round(resumen, 2)}')

# c. diccionario con los valores diarios de las UVA
with open('../../../Data/cer-uva-uvi-diarios.csv', 'r', encoding='UTF8') as f:
    filas = csv.reader(f)
    encabezados = next(filas)
    valores_uva = {}
    index_fecha = encabezados.index("indice_tiempo")
    index_uva = encabezados.index("uva_diario")
    for fila in filas:
        print(fila)
        valores_uva[fila[index_fecha]] = fila[
            index_uva]  # Al diccionario valores_uva le agrego un la fecha como clave (key) y el valor de la UVA correrspondiente como valor (value)
    print(valores_uva)

    # d. Calculá cuantas UVAs podría haber adquirido Juan gastando el mismo dinero que usó en las acciones
    cantidad_uvas = 0
    valor_actual_uvas = 0
    for accion in acciones:
        cantidad_uvas_dia = float(accion["precio_compra"]) * float(accion["cantidad"]) / float(
            valores_uva[accion["fecha"]])
        cantidad_uvas += cantidad_uvas_dia
        valor_actual_uvas += 208.99 * cantidad_uvas_dia

    diferencia_portafolios = valor_actual_uvas - valor_actual

    print(
        f"Si hubiera comprado {int(cantidad_uvas)} UVAs hubiera obtenido un portafolio de {round(valor_actual_uvas, 2)}, mientras que el portafolio de acciones fue de {round(valor_actual_acciones, 2)}.")

    if diferencia_portafolios > 0:
        print(f"La opción que más rindió fue invertir en UVAs por {round(diferencia_portafolios, 2)}")
    elif diferencia_portafolios < 0:
        print(f"La opción que más rindió fue invertir en acciones por {round(-diferencia_portafolios, 2)}")