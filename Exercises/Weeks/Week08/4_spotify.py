# Vamos a trabajar con un nuevo dataset, el del archivo ["Spotify 2010 - 2019 Top 100.csv"], extraído de aquí, que contiene información de las canciones más escuchadas cada año en la plataforma de streaming Spotify.
# * Explorar el dataset (mirar cuántos líneas hay, qué campos tiene, de que tipo son, etc.)
# * Mostrar los 10 artistas con más canciones a lo largo de todos los años y los 10 géneros más frecuentes.
# * Buscar cuáles son las canciones con tempos (bpm, pulsaciones por minuto) más elevados. (Sugerencia: investigar en la documentación de pandas sobre el método sort_values())
# * Crear un nuevo DataFrame con los datos de ritmo (bpm) y duración (dur) promedio para cada año. (Sugerencia: es simple de hacerlo con el método groupby())
# * A partir del DataFrame del inciso anterior, haga gráficos de la evolución de la duración y el ritmo promedio a lo largo de los años.
# * (Opcional) Investigue cómo hacer gráficos de torta en pandas y haga uno que muestre la proporción de los distintos tipos de artista ('artist type') de todo el dataset.

import pandas as pd

spotify = pd.read_csv('../../../Data/Spotify 2010 - 2019 Top 100.csv')
print(spotify)
spotify.info()

artists = spotify.pivot_table(index = ['artist'], aggfunc ='size').sort_values().tail(10)
print('\n\n', artists)

genres = spotify.pivot_table(index = ['top genre'], aggfunc ='size').sort_values().tail(10)
print('\n\n', genres)

tempos = spotify