import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('../cell.jpeg')
print('img cargada')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)

row, col, chn=np.shape(img)
print('Filas    ', row)
print('Columnas ', col)
print('Canales  ', chn)
lista_info = [row, col, chn]

imaR=np.copy(img)
imaR[:,:,1]=0
imaR[:,:,2]=0
print(imaR)
print(np.max(imaR))
print(np.min(imaR))
"""
imaG=np.copy(img)
imaG[:,:,0]=0
imaG[:,:,2]=0
print(imaG)
print(np.max(imaG))

imaB=np.copy(img)
imaB[:,:,1]=0
imaB[:,:,0]=0

print(imaB)
print(np.max(imaB))
"""
plt.figure(figsize=(15,6))
# plt.subplot(1,3,1)
# plt.imshow(imaB)
# plt.subplot(1,3,2)
# plt.imshow(imaG)
plt.subplot(1,3,3)
plt.imshow(imaR)
"""max_eje1 = (np.argmax(img, axis=0))
#print(max_eje1)
max_eje = np.argmax(max_eje1, axis=1)
print(max_eje)"""

img2=cv2.imread('azul.png')
img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
imaR2=np.copy(img2)
imaR2[:,:,1]=0
imaR2[:,:,2]=0
print(imaR2)
print(np.max(imaR2))
print(np.min(imaR2))
plt.imshow(imaR2)

