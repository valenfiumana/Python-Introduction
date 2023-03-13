### INTRODUCCION
# What's in here:
# 1. Conditionals
# 2. Print & Input
# 3. Pass
# 4. Math Operations
# 5. Strings
# 6. Lists

for i in range(5):
    print(i)

# - - - - - - - - - -  1. CONDITIONALS - - - - - - - - - -
a = 5
b = 7

# f-string
if a > b:
    print(f'{a} is greater than {b}')
else:
    print(f'{a} is less than {b}')

# elif
if a < b:
    print('a wins')
elif a == b:
    print('Its a tie')
else:
    print('b wins')


# - - - - - - - - - -  2. PRINT & INPUT - - - - - - - - - -
#print

print('Hello world')

x = 100
print(x)

print('My name is', 'Valen')

name = 'Valen'
print('My name is', name)

print('Learning Python', end=' ') #avoiding the line break
print('basics')


# input
name = input('Enter your name: ')
print('Your name is', name)


# - - - - - - - - - - 3. PASS - - - - - - - - - -
if a > b:
    pass
else:
    print(f'{a} is lower')


# - - - - - - - - - -  FLOAT - - - - - - - - - -
a = 37.47
b = 4e5
c = -1.34e-10

# !!!! floating point arithmetic has limitations
a = 2.1 + 4.2
print(a == 6.3) # False
print(a)        # 6.300000000000001


# - - - - - - - - - - 4. MATH OPERATIONS - - - - - - - - - -
x = 100
y = 20

# basics
r = x / y     # result is a float
r = x // y    # result is an int (it actually is a float but with zeros to the right of the decimal place)
r = x % y     # remainder
r = x ** y    # power
abs(x)        # absolute value

# math
import math
a = math.sqrt(x)
b = math.sin(x)
c = math.cos(x)
d = math.tan(x)
e = math.log(x)

# conversion
a = int(x)     #x to int
b = float(x)   #x to float

# !!! bool() is NOT for parsing
# It returns the boolean value of a specified object (empty strings are False and any string is True)
bool("")          #False
bool("hola")      #True
bool("False")     #True
bool(0)           #False
bool(1)           #True
bool(True)        #True


# - - - - - - - - - - 5. STRINGS - - - - - - - - - -
# slice
a = 'Hello world'
d = a[:5]     # 'Hello'
e = a[6:]     # 'world'
f = a[3:8]    # 'lo wo'
g = a[-5:]    # 'world'

# Sacar ultimos caracteres
string = 'ValenFiuD'
name = string.rstrip(name[-1])
print(name)

# Concatenación (+)
a = 'Hello' + 'World'   # 'HelloWorld'
b = 'Say ' + a          # 'Say HelloWorld'

# Longitud (len)
s = 'Hello'
len(s)      # 5

# Replicación (s * n)
rep = s * 5             # 'HelloHelloHelloHelloHello'

# Test de pertenencia (in, not in)
t = 'e' in s            # True
f = 'x' in s            # False
g = 'hi' not in s       # True


# remove spaces
s = '  Valen '
t = s.strip()     # 'Valen

# to lower/upper case
s = 'Hello'
l = s.lower()  # 'hello'
u = s.upper()  # 'HELLO'

# replace
s = 'Hello world'
t = s.replace('Hello' , 'Hallo')   # 'Hallo world'


# conversion to string
x = 42
str(x)

#string to list
line = 'Pera,100,490.10'
row = line.split(',')
print(row)      # ['Pera', '100', '490.10']

#backward string
string = 'Hello World'
backward = string[::-1] #dlroW olleH

# - - - - - - - - - - 6. LISTS - - - - - - - - - -
names = [ 'Ellen', 'Meredith', 'Taylor' ]
nums = [ 39, 38, 42, 65, 111]

#list length
len(names)

#insert at the end
names.append('Grey')
print(names)

#insert at any position
names.insert(3, 'Swift')
print(names)

# modify a value
names[0] = 'Ellen Pompeo'

#indexes
a = names[0]  # 'Ellen'
b = names[1]  # 'Meredith'
c = names[-1] # 'Grey' (negative numbers count from the back)

#check if contains sth
t = 'Taylor' in names     # True
f = 'Meredith' not in names  # False

#for
for name in names:
    print(name)

for i in [1, 2, 3]:
    print(i)

for i in range(3): #range(3) creates a list with int numbers < 3 == [0, 1, 2]
    print(i)

for x in range(-3, 3): # -3 < x < 3
    print(x)

for k in range(10,20,2): # Va contando de a 2
    print(k, end=' ')    # k = 10,12,...,18

#enumerate --> permite agregar un contador a la iteración
nombres = ['Juan', 'Elsa', 'Ingrid', 'Carlos', 'Federico']
for i, nombre in enumerate(nombres):
    print(i, nombre)
    # 0 Juan
    # 1 Elsa
    # etc.

#index of element (first aparition)
a = names.index('Meredith')
print(a) # 1

# remove using value
names.remove('Grey')

# remove using index
del names[0]

#concatenate lists
names2 = ['Chandler', 'Monica', 'Rachel', 'Joey', 'Phoebe', 'Ross']
new_list = names + names2
print(new_list) # ['Meredith', 'Taylor', 'Swift', 'Chandler', 'Monica', 'Rachel', 'Joey', 'Phoebe', 'Ross']

#string to list
line = 'Pera,100,490.10'
row = line.split(',')
print(row)      # ['Pera', '100', '490.10']

#replicate list
numeros = nums * 3
print(numeros)

#sort "in place" (without having to create a new list)
s = [10, 1, 7, 3]
s.sort()                 # [1, 3, 7, 10]
s.sort(reverse=True)     # [10, 7, 3, 1]
t = sorted(s)            # s queda igual, t guarda los valores ordenados

s = ['foo', 'bar', 'spam']
s.sort()     # ['bar', 'foo', 'spam']

#sorted (creating a new list)
t = sorted(s)
print(t) # [10, 7, 3, 1]


#slicing --> s[principio:fin], donde el índice final es excluyente
a = [0,1,2,3,4,5,6,7,8]
a[2:5]    # [2,3,4]
a[-5:]    # [4,5,6,7,8]
a[:3]     # [0,1,2]

# Reasignación --> no hace falta que tenga la misma longitud
a = [0,1,2,3,4,5,6,7,8]
a[2:4] = [10,11,12]       # [0,1,10,11,12,4,5,6,7,8]

# Borrado
a = [20,21,22,23,24,25,26,27,28]
del a[2:4]                # [20,21,24,25,26,27,28]