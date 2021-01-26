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


class Ventanappal(QMainWindow):
    def __init__(self, parent=None):
        super(Ventanappal,self).__init__(parent)
        loadUi('Ventanappal.ui',self)
        self.setup()

    def setup(self):

        self.edit_xi.setValidator(QIntValidator())
        self.edit_xf.setValidator(QIntValidator())
        self.edit_yi.setValidator(QIntValidator())
        self.edit_xf.setValidator(QIntValidator())

        self.boton_histograma.setEnabled(False)
        self.boton_contar.setEnabled(False)
        self.boton_cambios.setEnabled(False)

        self.boton_cargar.clicked.connect(self.cargar_img)
        self.cancelar.clicked.connect(self.cerrar)
        self.boton_histograma.clicked.connect(self.graficar_histograma)
        self.boton_contar.setEnabled(self.contar_celulas)
        self.boton_cambios.setEnabled(self.graficar_cambios)
        self.boton_equalizar.setEnabled(self.equalizar)

        # self.sc = Dibujo(self.campo1)
 
        # self.Layout1.addWidget(self.sc)

    # def mostrarimg(self):
    #     nimagen=self.nimagen.text()
    #     img=self.__coord.mostrarimg(nimagen)
    #     self.sc.graficarimg(img)
    def cargar_img(self):
        archivo_cargado, _ = QFileDialog.getOpenFileName(self, "Abrir imagen","","Archivos jpg (*.jpg)","","Archivos png (*.png)")
        if archivo_cargado !='':
            self.boton_histograma.setEnabled(True)
            self.boton_contar.setEnabled(True)
            self.boton_cambios.setEnabled(True)

        else:
            msj = QMessageBox(self)
            msj.setText('El archivo no se ha cargado\nVuelva a intentarlo')
            msj.show()

    def graficar_histograma(self):
        pass

    def graficar_cambios(self):
        xi=self.edit_xi.text()
        xf=self.edit_xf.text()
        yi=self.edit_yi.text()
        yf=self.edit_xf.text()

    def contar_celulas(self):
        pass

    def equalizar(self):
        pass

    def cerrar(self):
        self.close()
    def setcoord(self,coord):
        self.__coord=coord
        
