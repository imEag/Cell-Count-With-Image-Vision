#%%
import cv2
import numpy as np
import matplotlib.pyplot as plt
imgB = cv2.imread('cell.jpeg')
imgB[:,:,1]=0
imgB[:,:,2]=0
plt.imshow(imgB)
imgB = cv2.cvtColor(imgB, cv2.COLOR_BGR2GRAY)
print('img cargada')
#imgB=np.copy(img)


kernel = np.ones((3,3),np.uint8)
imgB = cv2.dilate(imgB,kernel,iterations = 2)
imgB = cv2.erode(imgB,kernel,iterations = 2)
blur = cv2.GaussianBlur(imgB,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
elem,mask=cv2.connectedComponents(th3)
print(elem)

plt.figure()
plt.plot()
#img2 en BGR
plt.imshow(mask,'gray')

# imgRGB=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
# imgBGR=cv2.cvtColor(img2,cv2.COLOR_RGB2BGR)
# imgHSV=cv2.cvtColor(img2,cv2.COLOR_BGR2HSV)
# imgHLS=cv2.cvtColor(img2,cv2.COLOR_BGR2HLS)
# imgLAB=cv2.cvtColor(img2,cv2.COLOR_BGR2LAB)
# imgGRAY=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
# imgYCRCB=cv2.cvtColor(img2,cv2.COLOR_BGR2YCrCb)



# plt.imshow(img2)
# plt.subplot(3,3,2)
# plt.imshow(imgRGB)
# plt.subplot(2,3,3)
# plt.imshow(imgHSV)
# plt.subplot(3,3,4)
# plt.imshow(imgHLS)
# plt.subplot(3,3,5)
# plt.imshow(imgLAB)
# plt.subplot(3,3,6)
# plt.imshow(imgGRAY)
# plt.subplot(3,3,7)
# plt.imshow(imgYCRCB)
# plt.subplot(3,3,8)
# plt.imshow(img2)
# plt.subplot(3,3,9)
# plt.imshow(img2)









# """
# row, col, chn=np.shape(img)
# print('Filas    ', row)
# print('Columnas ', col)
# print('Canales  ', chn)
# lista_info = [row, col, chn]

# imaR=np.copy(img)
# imaR[:,:,1]=0
# imaR[:,:,2]=0
# print(imaR)
# print(np.max(imaR))
# print(np.min(imaR))

# imaG=np.copy(img)
# imaG[:,:,0]=0
# imaG[:,:,2]=0
# print(imaG)
# print(np.max(imaG))

# imaB=np.copy(img)
# imaB[:,:,1]=0
# imaB[:,:,0]=0

# print(imaB)
# print(np.max(imaB))

# plt.figure(figsize=(15,6))
# # plt.subplot(1,3,1)
# # plt.imshow(imaB)
# # plt.subplot(1,3,2)
# # plt.imshow(imaG)
# plt.subplot(1,3,3)
# plt.imshow(imaR)
# max_eje1 = (np.argmax(img, axis=0))
# #print(max_eje1)
# max_eje = np.argmax(max_eje1, axis=1)
# print(max_eje)

# img2=cv2.imread('azul.png')
# img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
# imaR2=np.copy(img2)
# imaR2[:,:,1]=0
# imaR2[:,:,2]=0
# print(imaR2)
# print(np.max(imaR2))
# print(np.min(imaR2))
# plt.imshow(imaR2)
# """
