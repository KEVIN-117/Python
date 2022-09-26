from matplotlib import markers
import matplotlib.pyplot as plt
import numpy as np

x = list([75 ,
          150 ,
          300 ,
          600 ,
          900 ,
          1200 ,
          1800 ,
          3600])
y = list([1.513 ,
          3.056 ,
          6.06 ,
          17.08 ,
          12.13 ,
          24.14 ,
          35.90 ,
          72.10])


plt.figure(figsize=(10, 5))
plt.title("Grafica")
plt.xlabel("Eje x")
plt.ylabel("eje y")
plt.axis((75 ,150 ,300 ,600 ,900 ,1200 ,1800 ,3600))

plt.plot(x,y ,
         marker='o',
         linewidth=6,  # Aumentar el tamaño de la línea
         color='r',
         alpha=0.8,  # Tonalidad de la línea
         markersize=15,
         linestyle='--',
         label='f(x)')
plt.legend()
plt.show()