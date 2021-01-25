
from Modelo import sistema
from Vista import Ventanappal
from PyQt5.QtWidgets import QApplication
import sys



class Controlador():
    def __init__(self, vista, modelo):
        self.__mivista= vista
        self.__mimodelo=modelo


    def mostrarimg(self,nimagen):
        return self.__mimodelo.mostrarimg(nimagen)

        
def main():
    app=QApplication(sys.argv)
    modelo=sistema()
    
    vista=Ventanappal()
    coord=Controlador(vista,modelo)
    vista.setcoord(coord)
    vista.show()
    sys.exit(app.exec_())

main()


