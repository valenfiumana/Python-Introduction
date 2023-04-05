# Functions

### Simple function
```python
def add(x, y):
    return x+y

print(add(2,3)) # 5
```

### *args
*args allows us to pass a variable number of non-keyword arguments to a Python function. 

In the function, we should use an asterisk (*) before the parameter name to pass a variable number of arguments.

! Note that the name of the argument need not necessarily be args – it can be anything. 
```python
def add(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add(2, 3)) #5
print(add(2, 3, 5)) #10
print(add(2, 3, 5, 7)) #17
```

### **kwargs
**kwargs allows us to pass a variable number of keyword arguments to a Python function.

```python
def indeterminados_nombre(**kwargs):
    print(kwargs)           # {'n': 5, 'c': 'Hola', 'l': [1, 2, 3, 4, 5]}
    print(type(kwargs))     # <class 'dict'>

indeterminados_nombre(n=5, c="Hola", l=[1,2,3,4,5])
```
```python
def func(**kwargs):
    for kwarg in kwargs:
        print(kwarg, "=>", kwargs[kwarg])
        # n => 4
        # c => Hola mundo
        # a => [2, 4, 6]

func(n=4, c='Hola mundo', a = [2,4,6])
```

### Return more than one value

```python
def CuadradoCubo(n):
  cuadrado = n ** 2
  cubo = n ** 3
  return cuadrado, cubo

a = CuadradoCubo(5)
print(a) # (25, 125) --> tuple

c2, c3 = CuadradoCubo(5)
print(c2) # 25
print(c3) # 125
```

### Errors and exceptions

#### try / except
```python
numero_valido=False
while not numero_valido:
    try:
        a = input('Ingresá un número entero: ')
        n = int(a)
        numero_valido = True
    except ValueError:
        print('No es válido. Intentá de nuevo.')
print(f'Ingresaste {n}.')
```
#### generate Exception

```python
raise RuntimeError('Something went bad! Poor you')
```

```python

```
