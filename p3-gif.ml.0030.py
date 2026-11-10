import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

# Cepeda Darrell NC 0030
print("Cepeda Darrell NC 0030")
print("UIII Act3 colocar puntos a una imagen en blanco y negro")
mi_imagen = cv2.imread("DonRamon.png")
plt.imshow(mi_imagen)
plt.title('Don Ramon y Cepeda Darrell 0030')
plt.show()
print("*-*-*-* Puntos en la imagen *-*-*-*")
plt.imshow(mi_imagen)
x = [100,100,300,450]
y = [100,400,500,230]
plt.scatter(x, y, s=20,c='red')
plt.show()