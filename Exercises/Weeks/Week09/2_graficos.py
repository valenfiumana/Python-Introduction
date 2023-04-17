# Modificá el siguiente código para reproducir el gráfico que se muestra. Prestá atención a cómo se numeran los subplots.

import matplotlib.pyplot as plt

fig = plt.figure()
plt.subplot(2, 1, 1) # define la figura de arriba
plt.plot([0,1,2],[0,1,0]) # dibuja la curva
plt.xticks([]), plt.yticks([]) # saca las marcas

plt.subplot(2, 3, 4) # 4 porque seria la cuarta en grilla de 3x3
plt.plot([0,1],[0,1])
plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 5) # 5 porque sería la quinta en grilla de 3x3
plt.plot([0,1],[0.5,0.5])
plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 6) # 6 porque sería la sexta en grilla de 3x3
plt.plot([0,1],[1,0])
plt.xticks([]), plt.yticks([])

plt.show()