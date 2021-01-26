import matplotlib as plt
import cv2
import numpy as np
import matplotlib.pyplot as plt

class sistema:
    def __init__(self):
        pass

    def cargar_img(self,imagen):
        #img=cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
        self.imagen = imagen

    
    def retornar_info_img(self):
        row, col, chn=np.shape(self.imagen)
        # print('Filas    ', row)
        # print('Columnas ', col)
        # print('Canales  ', chn)
        
        imaR=np.copy(self.imagen)
        imaR[:,:,1]=0
        imaR[:,:,2]=0
        
        max_imaR=np.max(imaR)
        min_imaR=np.min(imaR)
        
        imaG=np.copy(self.imagen)
        imaG[:,:,0]=0
        imaG[:,:,2]=0
        max_imaG=np.max(imaG)
        min_imaG=np.min(imaG)

        imaB=np.copy(self.imagen)
        imaB[:,:,1]=0
        imaB[:,:,0]=0
        
        max_imaB=np.max(imaB)
        min_imaB=np.min(imaB)
             
        lista_info = [row, col, chn, max_imaR, min_imaR, max_imaG, min_imaG, max_imaB, min_imaB]
        return lista_info
    
    def graficar_canal(self, canal):
        if canal == 'Rojo':
            imgR=np.copy(self.imagen)
            imgR[:,:,1]=0
            imgR[:,:,2]=0
            return imgR
        elif canal == 'Verde':
            imgG=np.copy(self.imagen)
            imgG[:,:,0]=0
            imgG[:,:,2]=0
            return imgG
        elif canal == 'Azul':
            imgB=np.copy(self.imagen)
            imgB[:,:,1]=0
            imgB[:,:,0]=0
            return imgB
    
    def retornar_imagen(self):
        return self.imagen
    
    def recortar_img(self, xi, xf, yi, yf):
        img_recortada = np.copy(self.imagen)
        print(xi, xf, yi, yf)
        return img_recortada[yi:yf+1, xi:xf+1, :]