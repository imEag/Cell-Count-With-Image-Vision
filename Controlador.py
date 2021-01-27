from Modelo import sistema
from Vista import Ventanappal
from PyQt5.QtWidgets import QApplication
import sys



class Controlador():
    def __init__(self, vista, modelo):
        self.__vista= vista
        self.__modelo=modelo

    def cargar_img(self,imagen):
        return self.__modelo.cargar_img(imagen)

    def retornar_imagen(self):
        return self.__modelo.retornar_imagen()
    
    def retornar_info_img(self):
        return self.__modelo.retornar_info_img()

    def recortar_img(self,xi,xf,yi,yf):
        return self.__modelo.recortar_img(xi,xf,yi,yf)

    def retornar_espacio_color(self,espacio_color):
        return self.__modelo.retornar_espacio_color(espacio_color)

    def retornar_canal(self,canal):
        return self.__modelo.retornar_canal(canal)

    def retornar_operacion(self,operacion,escalar):
        return self.__modelo.retornar_operacion(operacion,escalar)
    
    def equalizar(self):
        return self.__modelo.equalizar()

    def contar_celulas(self):
        return self.__modelo.contar_celulas()

        
def main():
    app=QApplication(sys.argv)
    modelo=sistema()
    
    vista=Ventanappal()
    coord=Controlador(vista,modelo)
    vista.setcoord(coord)
    vista.show()
    sys.exit(app.exec_())

main()
