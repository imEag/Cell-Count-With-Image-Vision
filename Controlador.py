
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


        
def main():
    app=QApplication(sys.argv)
    modelo=sistema()
    
    vista=Ventanappal()
    coord=Controlador(vista,modelo)
    vista.setcoord(coord)
    vista.show()
    sys.exit(app.exec_())

main()


