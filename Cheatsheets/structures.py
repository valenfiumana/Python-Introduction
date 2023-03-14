## STRUCTURES
# 1. Data Types
#   1.1 Tuple
#   1.2 Dictionary
#   1.3 Container
#   1.4 Sets
# 2. Zip function
# 3. Comprehension
# 4.  References and mutability

# TODO: - - - - - - - - - -  1. TIPOS DE DATOS  - - - - - - - - - - #
# type None
email_address = None
if(email_address):
    print('En condicionales, None evalúa como False')

#  . . . . . . 1.1 TUPLAS . . . . . . .
# para representar registros o estructuras simples (un solo objeto con múltiples partes)
# Contienen una serie de elementos ordenados (indexados), que pueden ser repetidos.
# Son inmutables, no están pensadas para ser modificadas

t = ('Manzanas', 100, 490.1)
nombre = t[0]                   # 'Manzana'
cantidad = t[1]                 # 100
precio = t[2]                   # 490.1

# Desempaquetar
#cantiad de variables  a la izq == estructura tupla
fruta, cajones, precio = s
print('Costo: ', cajones * precio)

# El contenido de las tuplas no puede ser modificado.
t[1] = 75 #TypeError: object does not support item assignment

# Nueva tupla a partir de esa
t = (t[0], 75, t[2])

# función enumerate(): nos va entregando tuplas (índice, elemento)
lista = ['a', 20, 17.5, 'b']

for i, e in enumerate(lista):
    print('nº:', i, 'Elemento:', e)

for e in enumerate(lista):
    print('tupla:', e)

# iterar sobre elemento de tuplas
puntos = [
    (1, 4),(10, 40),(23, 14),(5, 6),(7, 8)
]
for x, y in puntos:
    print('x =', x, '\t y =', y)

# Tupla vs Lista
apple = ('Manzanas', 100, 490.1)                # Una tupla representando un registro dentro de un pedido de frutas (un solo ítem que consiste de múltiples partes)
fruits = [ 'Manzanas', 'Peras', 'Mandarinas' ]  # Una lista representando tres frutas diferentes ( colección de diferentes elementos, típicamente del mismo tipo).

#list to tuple
tuple(fruits)

# Combinar tuplas y listas
frutas = [('Manzanas', 100, 490.1), ('Peras', 120, 582.5), ('Mandarinas',50,345.2)]

for tupla in frutas:
    fruta, cajones, precio = tupla
    print("Costo", fruta, "=", cajones * precio)
print(frutas[2][0])

# zip
names = ['Meredith', 'Derek']
birthdays = ['07/09', '11/11']
lista_tup = list(zip(names, birthdays)) # [('Meredith', '07/09'), ('Derek', '11/11')]

# unzip
unzip = list(zip(*t)) #[('Meredith', 'Derek'), ('07/09', '11/11')]
firstNames = list(unzip[0])  #['Meredith', 'Derek']
dates = list(unzip[1]) #['07/09', '11/11']


# TODO:  . . . . . . 1.2 DICCIONARIOS . . . . . . .
# Función que manda claves en valores. Las claves sirven como índices para acceder a los valores.
# Son útiles cuando hay muchos valores diferentes y esos valores pueden ser modificados o manipulados.
# Dado que el acceso a los elementos se hace por clave, no es necesario recordar una posición para cierto dato:
# hacer que el código sea más legible (y con esto menos propenso a errores).
d = {
    'fruta': 'Manzana',
    'cajones': 100,
    'precio': 490.1
}

#obtener valor --> vs a[2] en una lista, acá veo lo que estoy pidiendo
print(d['fruta']) #Manzana

#agregar o modificar
d['cajones'] = 75
d['fecha'] = '27/2/2023'

#borrar
del s['fecha']

#Si usás el comando for para iterar sobre el diccionario, obtenés las claves:
for k in d:
    print('k =', k) # k = nombre
                    # k = cajones

for k in d:
    print(k, '=', d[k]) # nombre = 'Lima'
                        # cajones = 75

#Si pasás un diccionario a una lista, obtenés sus claves.
list(d) #['nombre', 'cajones', 'precio', 'fecha', 'cuenta']

# También podés obtener todas las claves del diccionario usando el método keys():
claves = d.keys()
print(claves) #dict_keys(['nombre', 'cajones', 'precio', 'fecha', 'cuenta'])


# TODO:  . . . . . . 1.3 CONTENEDORES . . . . . . .
# . . . listas como contenedores
# Usá listas cuando el orden de los datos importe. Acordate de que las listas pueden contener cualquier tipo de objeto.
# Son mutables, pueden ser modificadas sin definir una nueva lista.3
camion = [
    ('Pera', 100, 490.1),
    ('Naranja', 50, 91.3),
    ('Limon', 150, 83.44)
]
camion[0]   # ('Pera', 100, 490.1)
camion[2]   # ('Limon', 150, 83.44)

# construcción de lista
registros = []  # Empezamos con una lista vacía
registros.append(('Pera', 100, 490.10)) # .append() para agregar elementos
registros.append(('Naranja', 50, 91.3))

#cargar registros desde un archivo.
registros = []  # Empezamos con una lista vacía
with open('camion.csv', 'rt') as f:
    next(f) # Saltear el encabezado
    for line in f:
        row = line.split(',')
        registros.append((row[0], int(row[1]), float(row[2])))


# . . . diccionarios como contenedores
precios = {
    'Pera': 513.25,
    'Limon': 87.22,
    'Naranja': 93.37,
    'Mandarina': 44.12
}
precios['Naranja']
precios['Pera']

# armado de un diccionario desde cero.
precios = {} # diccionario vacío
precios['Pera'] = 513.25
precios['Limon'] = 87.22
precios['Naranja'] = 93.37

# cómo armar un diccionario a partir del contenido de un archivo.
precios = {}  #diccionario vacío
with open('camion.csv', 'rt') as f:
    for line in f:
        row = line.split(',')
        precios[row[0]] = float(row[1])

# comprobar pertenencia claves
if key in d:
    print('Yes')
else:
    print('No')

# borrar valor
del precios['Pera']

# longitud
len(d)

# iterar diccionario
# . . sobre las claves
for clave in d.keys():
    print(d[clave])

# . . sobre los valores
for val in d.values():
    print(val)

# . . items son tuplas (clave, valor)
for item in d.items():
    print(item)

# Claves compuestas
# Casi cualquier valor puede usarse como clave en un diccionario de Python.
# La principal restricción es que una clave debe ser de tipo inmutable (NO listas, conjuntos ni diccionarios)

feriados = {
    (1, 1) : 'Año nuevo',
    (1, 5) : 'Día del trabajador',
    (13, 9) : "Día del programador",
}

feriados[(1, 5)] #'Día del trabajador'

# TODO:  . . . . . . 1.4 CONJUNTOS . . . . . . .
#Un conjunto es una colección de elementos únicos sin orden y sin repetición.
citricos = { 'Naranja','Limon','Mandarina' } #set literal
citricos = set(['Naranja', 'Limon', 'Mandarina']) #set

print(citricos) #set(['Naranja', 'Limon', 'Mandarina'])

#Los conjuntos son útiles para evaluar pertenencia.
print('Naranja' in citricos) #True
print('Manzana' in citricos) #False

#útiles para eliminar duplicados --> lista a conjunto
nombres = ['Naranja', 'Manzana', 'Pera', 'Naranja', 'Pera', 'Banana']
unicos = set(nombres) # unicos = {'Manzana', 'Banana', 'Naranja', 'Pera'}

#Más operaciones
s1 = {'Valen', 'Fiu'}
s2 = {'Friends', 'Greys Anatomy'}
citricos.add('Banana')        # Agregar un elemento
citricos.remove('Limon')    # Eliminar un elemento
s1 | s2                 # Unión de conjuntos s1 y s2
s1 & s2                 # Intersección de conjuntos
s1 - s2                 # Diferencia de conjuntos


# TODO:  . . . . . . 2. FUNCIÓN ZIP . . . . . . .
# trabajar sobre dos listas al mismo tiempo
nombres = ['Juan', 'Elsa', 'Ingrid', 'Carlos', 'Federico']
apellidos = ['Pérez', 'Gómez', 'Muller', 'Tacha', 'Higgins']
pares = zip(nombres, apellidos)

for nombre, apellido in pares:
    print('Nombre:', nombre, ' Apellido:', apellido)


# crear una lista de tuplas o para crear diccionarios a partir de ellas
# Creo lista de tuplas
lista_tup = list(zip(nombres, apellidos))
print(lista_tup)

# Creo un diccionario
dic = dict(zip(nombres, apellidos))
print(dic)

# zip() también se puede usar de manera de inversa usando un * en el argumento
# lista de tuplas (nombre, dni, nota) --> a lista de tres tuplas: una con nombres, otra con dni y otra con notas
# filas de una base de datos -->  columnas de la misma
alumnos = [
    ('Carlos Gómez', 41008418, 5),
    ('Gabriela Torres', 45790918, 8),
    ('Juan Pérez', 48327044, 9),
    ('Éric Guay', 35360531, 7),
    ('Juana Monte', 31583398, 10),
    ('Carla Díaz', 43772387, 6)]

print(list(zip(*alumnos))) # [('Carlos Gómez', 'Gabriela Torres', 'Juan Pérez', 'Éric Guay', 'Juana Monte', 'Carla Díaz'), (41008418, 45790918, 48327044, 35360531, 31583398, 43772387), (5, 8, 9, 7, 10, 6)]


# TODO:  . . . . . . 3. COMPRENSIÓN LISTAS Y DICCIONARIOS  . . . . . . .
# La comprensión de listas crea un una nueva lista aplicando una operación a cada elemento de una secuencia
a = [1, 2, 3, 4, 5]
b = [2*x for x in a] # Creo una lista con el doble de los elementos de a
print(b) #[2, 4, 6, 8, 10]

# Versión más cómoda y compacta:
b = []
for x in a:
    b.append(2*x)

# con palabras
nombres = ['Edmundo', 'Juana']
a = [nombre.lower() for nombre in nombres]
print(a) # ['edmundo', 'juana']

# para filtrar datos
a = [1, -5, 4, 2, -2, 10]
b = [2*x for x in a if x > 0] # uso sólo los números positivos
print(b) # [2, 8, 4, 20]

# definicion de diccionarios por comprensión
numeros = [i for i in range(10)]
dic2 = {n:n**2 for n in numeros}
print(dic2)

#Casos de uso
#Podés recolectar los valores de un campo específico de un diccionario:
frutas = [s['nombre'] for s in camion]

#Podés hacer consultas (queries) como si las secuencias fueran bases de datos.
a = [s for s in camion if s['precio'] > 100 and s['cajones'] > 50]

#Podés combinar la comprensión de listas con reducciones de secuencias:
costo = sum([s['cajones'] * s['precio'] for s in camion])

#Podés sumar solamente los números pares de la siguiente lista de números:
numeros = [1, 2, 4, 5, 8, 10, 13, 17]
suma_pares = sum(n for n in numeros if (n%2)==0)
print(suma_pares) # 24

# TODO: - - - - - - - - 4. REFERENCIAS Y MUTABILIDAD  - - - - - - - - - - #
# enteros inmutables
a = 10
b = a
a = 11
print(a) #11
print(b) #10

# listas mutables
a = [1, 2]
b = a
a.append(3)
print(a) #[1, 2, 3]
print(b) #[1, 2, 3]

# evitar mutabilidad listas
a = [1, 2]
b = a.copy()
a.append(3)
print(a) #[1, 2, 3]
print(b) #[1, 2]

# funcion id()
a = [1, 2]
print(a, id(a)) #[1, 2] 2006518605056 <--
b = [a, 'hola']
print(b, id(b)) #[[1, 2], 'hola'] 2006518555584
print(b[0], id(b[0])) #[1, 2] 2006518605056 <--
a.append(3)
print(a, id(a)) #[1, 2, 3] 2006518605056 <--
print(b[0], id(b[0])) #[1, 2, 3] 2006518605056 <--

# ojo con variables mutables dentro de listas
lista_a = [1, "a"]
lista_b = [5.5, lista_a]
lista_c = lista_b.copy()
print(lista_c) #[5.5, [1, 'a']]
lista_a.append('agrego a lista_a')
lista_b.append('agrego a lista_b')
print(lista_c) #[5.5, [1, 'a', 'agrego a lista_a']]

