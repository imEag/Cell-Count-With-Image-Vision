import matplotlib as plt
import cv2
import numpy as np
import matplotlib.pyplot as plt

class sistema:
    def __init__(self):
        pass

    def cargar_img(self,imagen):
        #el self.imagen almacenará la imagen que fue cargada originalmente, el self.imagen_cambios almacena la imagen con todos los cambios que se le
        #hacen excepto recortes, en self.imagen_recortada se guarda la imagen recortada
        self.imagen = imagen
        self.imagen_cambios = np.copy(imagen)
        self.imagen_recortada = np.copy(imagen)
        
        
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
    
    def retornar_canal(self, canal):
        #esta fx retorna la imagen en un solo canal. La imagen la edita a partir de la imagen recortada (self.imagen_recortada) y la guarda en imagen_cambios
        if canal == 'Rojo':
            imgR=np.copy(self.imagen_recortada)
            imgR[:,:,1]=0
            imgR[:,:,2]=0
            self.imagen_cambios = imgR 
            return imgR
        elif canal == 'Verde':
            imgG=np.copy(self.imagen_recortada)
            imgG[:,:,0]=0
            imgG[:,:,2]=0
            self.imagen_cambios = imgG 
            return imgG
        elif canal == 'Azul':
            imgB=np.copy(self.imagen_recortada)
            imgB[:,:,1]=0
            imgB[:,:,0]=0
            self.imagen_cambios = imgB
            return imgB
        elif canal == 'TODOS LOS CANALES':
            self.imagen_cambios = np.copy(self.imagen)
            return self.imagen
        
    
    def retornar_imagen(self):
        return self.imagen
    
    def recortar_img(self, xi, xf, yi, yf):
        img = np.copy(self.imagen)
        img_recortada=img[yi:yf+1, xi:xf+1, :]
        self.imagen_recortada = img_recortada
        return img_recortada