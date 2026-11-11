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
print("*-*-*-* Cuadro en la imagen *-*-*-*")
img_ramon = cv2.imread('DonRamon.png')
plt.imshow(img_ramon)
x = [480, 740, 740, 480, 480]
y = [100, 100, 390, 390, 100]
plt.plot(x, y, c='Orange')
plt.show()
print("*-*-*- circulo verde en la imagen *-*-*-")
I = cv2.imread('DonRamon.png')
plt.imshow(I)
N = 30 # lados del poligono
x = np.zeros((N+1,))
y = np.zeros((N+1,))
(xc,yc) = (340, 320)
r = 150 # radio
for i in range(N+1):
    t    = 2*np.pi/N*i
    x[i] = xc + r*np.cos(t)
    y[i] = yc + r*np.sin(t)
plt.plot(x, y, c='green')
plt.show()