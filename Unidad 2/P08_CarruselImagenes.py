import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P08_CarruselImagenes.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.selectorImagen.valueChanged.connect(self.cambiaValor)
        self.selectorImagen.setMinimum(0)
        self.selectorImagen.setMaximum(2)
        self.selectorImagen.setSingleStep(1)
        self.selectorImagen.setValue(0)

        self.datosImagenes = {
            0: [":/Programas/ImagenGatoEuropeo.png", "Imagen 1"],
            1: [":/Logos/FIT_logo_vertical.png", "Imagen 2"],
            2: [":/Logos/log_uat_nuevo.png", "Imagen 3"]
        }

        nombre = self.datosImagenes[0][1]
        self.txt_nombre_imagen.setText(nombre)

    # Área de los Slots
    def cambiaValor(self):
        try:
            valor = self.selectorImagen.value()
            imagen_ruta = self.datosImagenes[valor][0]
            self.imagen.setPixmap(QtGui.QPixmap(imagen_ruta))

            nombre = self.datosImagenes[valor][1]
            self.txt_nombre_imagen.setText(nombre)
            print(valor)
        except Exception as error:
            print(error)

#pyrcc5 nombre.qrc -o nombre_rc.py
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

