import matplotlib as plt
import cv2
import numpy as np
import matplotlib.pyplot as plt

class sistema:
    def __init__(self):
        self.__grafica=None

    def cargar_img(self,nimagen):
        img=cv2.imread('./Imagenes/'+ nimagen)
        img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return img