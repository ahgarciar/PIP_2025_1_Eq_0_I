import sys
from PyQt5 import uic, QtWidgets, QtCore

import serial as placa

qtCreatorFile = "P41_ArduinoPythonGUI_ReadWrite_VariosActuadores.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.txt_com.setText("/dev/cu.usbmodem11301")

        self.arduino = None
        self.btn_accion.clicked.connect(self.accion)

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.lecturas)

        self.btn_led0.clicked.connect(self.control)
        self.btn_led1.clicked.connect(self.control)
        self.btn_led2.clicked.connect(self.control)

    # Área de los Slots
    def control(self):
        objeto = self.sender()
        if self.arduino.isOpen(): # 00 01   10  11   20  21
            led = objeto.objectName()[-1]
            texto = objeto.text()
            if texto == "PRENDER":
                objeto.setText("APAGAR")
                c = led + "1"
                self.arduino.write(c.encode())
            else:
                objeto.setText("PRENDER")
                c = led + "0"
                self.arduino.write(c.encode())

    def lecturas(self):
        if self.arduino.isOpen(): #la comunicacion esta abierta...
            if self.arduino.inWaiting(): #hay informacion que leer...
                lectura = self.arduino.readline().decode().strip()
                if lectura !="":
                    print(lectura)
                    #####
                    #PROCESAMIENTO DE LOS DATOS...
                    lectura = lectura.split("@")
                    lectura = lectura[:-1]

                    lectura = [int(i) for i in lectura]

                    ####
                    self.lista_datos.addItem(str(lectura))
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

