# Juan quiere comprar todos los bombones posibles con el dinero que tiene.
# Crear una función para calcular el número de bombones que puede comprar y el cambio (vuelto) que va a recibir.
# La función tiene que poder calcular esto para distintos montos de dinero y distinto precio de los bombones.
# Inventar ejemplos y probar la función creada.

def cantBombones(presu, precioBombon):
    cant = int(presu/precioBombon)
    vuelto = presu % precioBombon
    print(f'Puede comprar {cant} y recibe ${vuelto} de vuelto')
    return cant, vuelto

cantBombones(100, 10)
cantBombones(107, 10)