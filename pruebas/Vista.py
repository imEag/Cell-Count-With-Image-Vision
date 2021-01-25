from PyQt5.QtWidgets import QMainWindow, QFileDialog, QDialog
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QApplication, QMessageBox, QVBoxLayout
from PyQt5.uic import loadUi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import numpy as np
from matplotlib.figure import Figure


class Dibujo(FigureCanvas):
    def __init__(self, parent = None, widht = 5, higth = 4, dpi = 40):
    
        self.figura = Figure(figsize=(widht, higth), dpi=dpi)
        self.axes = self.figura.add_subplot(111)
        FigureCanvas.__init__(self,self.figura)

    def graficarimg(self,img):
        self.axes.imshow(img)
        self.axes.figure.canvas.draw()


class Ventanappal(QDialog):
    def __init__(self, parent=None):
        super(Ventanappal,self).__init__(parent)
        loadUi('ventanappal.ui',self)
        self.setup()

    def setup(self):
        self.mostrar.clicked.connect(self.mostrarimg)
        self.cancelar.clicked.connect(self.cancelarimg)

        self.sc = Dibujo(self.campo1)
 
        self.Layout1.addWidget(self.sc)

    def mostrarimg(self):
        nimagen=self.nimagen.text()
        img=self.__coord.mostrarimg(nimagen)
        self.sc.graficarimg(img)


    def cancelarimg(self):
        self.close()
    def setcoord(self,coord):
        self.__coord=coord
        
