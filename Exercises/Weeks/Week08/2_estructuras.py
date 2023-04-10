# * Crear una serie pandas para cada una de ellas, llamadas serLis, serArr y serDic.
# * Convertir la serie 'serDic' en un dataframe con su índice como otra columna en el dataframe.
# * Combine 'serLis' y 'serArr' para formar un dataframe.
# * Exporte el dataframe creado en el punto anterior a un archivo "serDic.csv"

import pandas as pd
import numpy as np

mi_lista = list('abcdefghijklmnopqrstuvwxyz')

mi_array = np.arange(26)

mi_diccionario = dict(zip(mi_lista,mi_array))

serList = pd.Series(mi_lista)
serArr = pd.Series(mi_array)
serDic = pd.Series(mi_diccionario)

dfDic = pd.DataFrame(serDic)

df = pd.DataFrame({'array': serArr, 'list': serList})

df.to_csv('serDic.csv')