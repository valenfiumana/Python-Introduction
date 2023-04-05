# Se quiere calcular la circunferencia, la superficie y el volumen de varios tanques australianos en diferentes campos:
# a. Tanque campo 1: radio = 3 m, altura = 1 m
# b. Tanque campo 2: radio = 4 m, altura = 1.5 m
# c. Tanque campo 3: radio = 2.6 m, altura = 1.2 m
# Escribir una o más funciones para que podamos hacer estos cálculos. Imprimí para cada caso los resultados obtenidos.
import math
def superficie(radio):
    return round(math.pi * radio**2, 2)

def circunferencia(radio):
    return round(2 * radio * math.pi, 2)

def volumen(radio, h):
    return round(h * math.pi * radio * 2, 2)

def datos(r, h):
    print(f'Circunferencia: {circunferencia(r)}')
    print(f'Superficie: {superficie(r)}')
    print(f'Volumen: {volumen(r, h)} \n')

datos(3, 1)
datos(4, 1.5)
datos(2.6, 1.2)
