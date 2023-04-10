import pandas as pd
import numpy as np

alumnos = ['Carla', 'Daniel', 'Fernan', 'Ivan']
notas = [np.random.randint(10)+1 for i in range(4)]

df_alumnos = pd.DataFrame({'Alumno':alumnos, 'Calificacion': notas})

# Defino una función para cambiar los nombres a minúsculas
def minusculas(cadena):
  return cadena.lower()

# Aplico la función a la columna 'Alumno'
df_alumnos['Alumno'] = df_alumnos['Alumno'].map(minusculas)

df_alumnos = pd.DataFrame({'Alumno':alumnos, 'Calificacion': notas})

print(df_alumnos)
# Aplico la función a la columna 'Alumno'
df_alumnos['Alumno'] = df_alumnos['Alumno'].map(lambda x: x.lower())
df_alumnos
print(df_alumnos)

