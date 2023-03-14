### FILES & STRUCTURES
# What's in here:
# 1. Files
# 2. Functions
# 3. Exceptions

# - - - - - - - - - -  1. FILES - - - - - - - - - - #
# abrir
fp1 = open('../bar.txt', 'wt') # 'w' de write, 't' de text
fp2 = open('foo.txt', 'rt') # 'r' de read, 't' de text

#escribir
fp1.write('Un texto')

#leer
data = fp2.read()

#cerrar
fp1.close()
fp2.close()

#leer con comando with (cierre automático)
# 1. archivo entero
with open ('foo.txt', 'rt') as file:
    data = file.read()
    # `data` es una cadena con todo el texto en `foo.txt`

# 2. linea por linea
with open('foo.txt', 'rt') as file:
    for line in file:
        print(line)

# escribir con comando with (cierre automático)
# 1. "x" - Create - will create a file, returns an error if the file exist
# 2. "a" - Append - will create a file if the specified file does not exist
# 3. "w" - Write - will create a file if the specified file does not exist
lines = ['Readme', 'How to write text files in Python']
with open('readme.txt', 'w') as f:
    for line in lines:
        f.write(line) # writes a string to a text file.
        f.write('\n')

# writeLines()
with open('readme.txt', 'w') as f:
    f.writelines(lines) # writes a list of strings to a file at once

# append
with open('readme.txt', 'a') as f:
    f.write('\n'.join(lines))

# csv = "Comma-Separated Values"
# El formato CSV es muy común en la importación y exportación de datos en aplicaciones de hojas de cálculo y bases de datos.
import csv
with open('incendios-cantidad-causas-parques-nacionales_2022.csv') as f:
    filas = csv.reader(f) #  interpreta cada línea como una lista de valores
    encabezados = next(filas)
    lineas = []
    for fila in filas:
        lineas.append(fila)

print(encabezados) # ['incendio_anio', 'incendio_total_numero', 'incendio_negligencia_numero', 'incendio_intencional_numero', 'incendio_natural_numero', 'incendio_desconocida_numero']
print(lineas[20]) # ['2013', '21', '7', '9', '0', '5']

# escribir con comando with (cierre automático)
# cadenas
with open('outfile', 'wt') as out:
    out.write('Hello World\n')

# ver cwd = "current-working-directory"
import os
print(os.getcwd())  # D:\Diplomatura\Modulo 1\Python basics
print(os.listdir()) # ['.git', '.idea', 'bar.txt', 'Cheatsheets', 'Exercises', 'prueba.py', 'README.md', 'Semanas', 'venv']

# . . . archivo texto
# separado por comas
with open('incendios-cantidad-causas-parques-nacionales_2022.csv', 'rt') as incendios:
    lineas = [linea.strip().split(',') for linea in incendios.readlines()]
    for linea in lineas:
        print(linea) # ['1993', '0', '0', '0', '0', '0']

# separado por espacios
with open('incendios-cantidad-causas-parques-nacionales_2022.txt', 'r') as incendios:
    lineas = [linea.strip().split(' ') for linea in incendios.readlines()]
    for linea in lineas:
        print(linea) # ['1993,0,0,0,0,0']

# . . librerías
# # Panda --> dataframe
# import pandas as pd
# df = pd.read_csv('incendios-cantidad-causas-parques-nacionales_2022.csv')
# print(df)
#
# # Numpy --> matriz
# import numpy as np
# matriz = np.loadtxt('incendios-cantidad-causas-parques-nacionales_2022.csv', delimiter=',')
# print(matriz)
# - - - - - - - - - -  2. FUNCTIONS - - - - - - - - - - #
#funcion clásica
def sumcount(n):
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total

a = sumcount(100)
print(a)

# funciones de biblioteca
import math
x = math.sqrt(10)
print(round(x, 2))

# break --> saltear actual iteración y pasar a la siguiente
numeros = [1, 2, 3, 4, 5]
for i in numeros:
    print(i)
    if i == 3:
        break
print('bucle finalizado','ultimo valor de i',i)

# continue
numeros = [1, -5, 2, -8, 10]
# imprimo los cuadrados de los números positivos
for i in numeros:
    if i <= 0:
        continue
    print(i**2)

# modules
# Un módulo en Python es un archivo que contiene definiciones de variables, funciones y clases que se pueden utilizar en otros programas.
# Los módulos tienen que ser importados! O sea, debemos decirle a nuestro código que otros archivos queremos utilizar.
# clasico
import math
a = math.pi
v = math.sqrt(9)

# cambio nombre
import math as m
a = m.pi
v = m.sqrt(25)

# solo algunas funciones
from math import sin, cos
r = 2
theta = m.pi
x = r * cos(theta)


# import urllib.request
# u = urllib.request.urlopen('http://www.python.org/')
# data = u.read()

# - - - - - - - - - -  3. EXCEPCIONES - - - - - - - - - - #
# excepción clásica
num_valido = False
while not num_valido:
    try:
        a = int(input('Ingresa un entero: '))
        num_valido = True
    except ValueError: # atrapo excepcion y repito ciclo
        print('No ingresaste un entero')
print(f'Ingresaste {a}')

# generar excepción
raise RuntimeError('¡Qué cagada!')

