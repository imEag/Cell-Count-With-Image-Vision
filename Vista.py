from PyQt5.QtWidgets import QMainWindow, QFileDialog, QDialog
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QApplication, QMessageBox, QVBoxLayout
from PyQt5.uic import loadUi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import cv2

from matplotlib.figure import Figure


class Dibujo(FigureCanvas):
    def __init__(self, parent = None, widht = 5, higth = 4, dpi = 40):
    
        self.figura = Figure(figsize=(widht, higth), dpi=dpi)
        self.axes = self.figura.add_subplot(111)
        FigureCanvas.__init__(self,self.figura)

    def graficar_imagen(self,img):
        self.axes.clear()
        self.axes.imshow(img)
        self.axes.figure.canvas.draw()

    def graficar_histograma(self,img):
        img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        R = cv2.calcHist([img],[0],None,[256],[0,256])
        G = cv2.calcHist([img],[1],None,[256],[0,256])
        B = cv2.calcHist([img],[2],None,[256],[0,256])
        self.axes.plot(B, 'r')
        self.axes.plot(G, 'g')
        self.axes.plot(R, 'b')
        self.axes.set_title('Histograma')
        self.axes.set_xlabel('Niveles')
        self.axes.set_ylabel('Densidad')
        self.axes.grid()
        self.axes.set_xlim((0, 255))
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
        self.boton_contar.setEnabled(False)
        self.boton_recorte.setEnabled(False)
        self.boton_equalizar.setEnabled(False)

        self.ok_canales.setEnabled(False)
        self.ok_espacio_color.setEnabled(False)
        self.ok_operaciones.setEnabled(False)


        self.boton_contar.clicked.connect(self.contar_celulas)
        self.boton_recorte.clicked.connect(self.graficar_recorte)
        self.boton_equalizar.clicked.connect(self.equalizar)
        self.boton_cargar.clicked.connect(self.cargar_img)
        self.boton_cerrar.clicked.connect(self.cerrar)
        self.boton_histograma.clicked.connect(self.graficar_histograma)

        self.ok_canales.clicked.connect(self.graficar_canal)
        self.ok_espacio_color.clicked.connect(self.graficar_espacio_color)
        self.ok_operaciones.clicked.connect(self.graficar_operaciones)

        self.canvas_histograma = Dibujo(self.campo_histograma)
 
        self.layout_histograma.addWidget(self.canvas_histograma)

        self.canvas_imagen = Dibujo(self.campo_img)
 
        self.layout_img.addWidget(self.canvas_imagen)

    def graficar_canal(self):
        canal=self.box_cambiar_canal.currentText()
        img_canal=self.__coord.retornar_canal(canal)
        self.canvas_imagen.graficar_imagen(img_canal)

    def graficar_espacio_color(self):
        espacio_color=self.box_espacio_color.currentText()
        img_espacio_color=self.__coord.retornar_espacio_color(espacio_color)
        self.canvas_imagen.graficar_imagen(img_espacio_color)

    def graficar_operaciones(self):
        operacion=self.box_operaciones.currentText()
        escalar=self.edit_operacion.text()
        img_canal=self.__coord.retornar_operacion(operacion,escalar)
        self.canvas_imagen.graficar_imagen(img_canal)

    def cargar_img(self):
        archivo_cargado, _ = QFileDialog.getOpenFileName(self, "Abrir imagen","","Archivos png, jpeg, jpg (*.png *.jpg *.jpeg)")
        if archivo_cargado !='':
            self.boton_histograma.setEnabled(True)
            self.boton_contar.setEnabled(True)
            self.boton_recorte.setEnabled(True)

            self.ok_canales.setEnabled(True)
            self.ok_espacio_color.setEnabled(True)
            self.ok_operaciones.setEnabled(True)

            img=cv2.imread(archivo_cargado)
            img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            self.__coord.cargar_img(img)
            imagen_retornada=self.__coord.retornar_imagen()
            self.canvas_imagen.graficar_imagen(imagen_retornada)
            msj = QMessageBox(self)
            msj.setText("Imagen cargada")
            msj.show() 

        else:
            msj = QMessageBox(self)
            msj.setText('El archivo no se ha cargado\nVuelva a intentarlo')
            msj.show()

    def graficar_histograma(self):
        img=self.__coord.retornar_imagen()
        self.canvas_histograma.graficar_histograma(img)

    def graficar_recorte(self):
        xi=self.edit_xi.text()
        xf=self.edit_xf.text()
        yi=self.edit_yi.text()
        yf=self.edit_xf.text()


        if xi!='' and xf!='' and yi!='' and yf!='':
            if xi<self.edit_filas and xf<=self.edit_filas and yi<self.edit_columnas and yf<=self.edit_columnas:
                img_recorte=self.__coord.recortar_img(int(xi),int(xf),int(yi),int(yf))
                self.canvas_imagen.graficar_imagen(img_recorte)

        else:
            msj = QMessageBox(self)
            msj.setText('Ingrese un valor válido')
            msj.show()
    def contar_celulas(self):
        pass

    def equalizar(self):
        pass

    def cerrar(self):
        self.close()
    def setcoord(self,coord):
        self.__coord=coord
        
