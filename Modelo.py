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
    
    def retornar_espacio_color(self, espacio):
        imgRGB = np.copy(self.imagen_recortada)
        #imgRGB llega en RGB
        #luego convertir a BGR para trabajar con esta variable.
        imgBGR = cv2.cvtColor(imgRGB, cv2.COLOR_RGB2BGR)
        
        if espacio == 'ESPACIO COLOR RGB':
            return imgRGB
        elif espacio == 'BGR':
            return imgBGR
        elif espacio == 'HSV':
            imgHSV = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2HSV)
            return imgHSV
        elif espacio == 'HLS':
            imgHLS = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2HLS)
            return imgHLS
        elif espacio == 'Lab':
            imgLab = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2Lab)
            return imgLab
        elif espacio == 'GRAY':
            imgGRAY = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2GRAY)
            return imgGRAY 
        elif espacio == 'YCRCB':
            imgYCRCB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2YCrCb)
            return imgYCRCB
        elif espacio == 'Luv':
            imgLuv = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2Luv)
            return imgLuv
        elif espacio == 'YUV':
            imgYUV = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2YUV)
            return imgYUV
        
    def equalizar(self):
        img_original = np.copy(self.imagen)
        imgG=cv2.cvtColor(img_original, cv2.COLOR_RGB2GRAY)
        img=np.array(imgG, np.dtype('float32'))
        img2=img-np.min(img)
        img2=img2*255/np.max(img2)
        return img2
    

    def contar_celulas(self):
        imgB=np.copy(self.imagen)
        imgB=cv2.cvtColor(imgB,cv2.COLOR_RGB2BGR)
        imgB[:,:,1]=0
        imgB[:,:,2]=0
        
        imgB = cv2.cvtColor(imgB, cv2.COLOR_BGR2GRAY)


        kernel = np.ones((3,3),np.uint8)
        imgB = cv2.dilate(imgB,kernel,iterations = 2)
        imgB = cv2.erode(imgB,kernel,iterations = 2)
        blur = cv2.GaussianBlur(imgB,(5,5),0)
        _,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        elem,mask=cv2.connectedComponents(th3)
        print(elem)

        return elem,mask

    def retornar_operacion(self, op, escalar):
        img = np.copy(self.imagen_recortada)
        escalar = int(escalar)
        if op == 'SUMAR':
            img2 = img + escalar
            return img2
        elif op == 'RESTAR':
            img2 = img - escalar
            return img2
        elif op == 'MULTIPLICAR':
            img2 = img * escalar
            return img2
        elif op == 'DIVIDIR':
            img2 = img / escalar
            return img2
    

    
    
    
    
    
    
    