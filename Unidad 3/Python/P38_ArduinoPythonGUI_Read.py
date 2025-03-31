import sys
from PyQt5 import uic, QtWidgets, QtCore

import serial as placa

qtCreatorFile = "P38_ArduinoPythonGUI_Read.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.txt_com.setText("/dev/cu.usbmodem1401")

        self.arduino = None
        self.btn_accion.clicked.connect(self.accion)

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.lecturas)



    # Área de los Slots
    def lecturas(self):
        if self.arduino.isOpen(): #la comunicacion esta abierta...
            if self.arduino.inWaiting(): #hay informacion que leer...
                lectura = self.arduino.readline().decode().strip()
                if lectura !="":
                    print(lectura)
                    self.lista_datos.addItem(lectura)
                    self.lista_datos.setCurrentRow(self.lista_datos.count()-1)


    def accion(self):
        texto = self.btn_accion.text()
        if texto == "CONECTAR": #iniciar la comunicacion y la apertura
            com = self.txt_com.text()  # COM5
            self.btn_accion.setText("DESCONECTAR")
            self.txt_estado.setText("CONECTADO")
            self.arduino = placa.Serial(com, baudrate=9600, timeout=1)
            self.segundoPlano.start(100)
        elif texto == "DESCONECTAR": #cierra la comunicacion
            self.btn_accion.setText("RECONECTAR")
            self.txt_estado.setText("DESCONECTADO")
            self.segundoPlano.stop()
            self.arduino.close()
        else: #reapertura la comunicacion
            self.btn_accion.setText("DESCONECTAR")
            self.txt_estado.setText("RECONECTADO")
            self.arduino.open()
            self.segundoPlano.start(100)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

