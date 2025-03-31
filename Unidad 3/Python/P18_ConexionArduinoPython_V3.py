
#pyserial ....
import serial as control

arduino = control.Serial("COM7", baudrate=9600, timeout=1)

tot_lecturas = 20
lectura = 0

datos = []

while lectura < tot_lecturas:
    mensaje = arduino.readline().decode().strip()
    if mensaje != "":
        print(mensaje)
        datos.append(mensaje)
        lectura += 1

#convierte los datos leidos en numeros
datos = [int(i) for i in datos]
print(datos)

from matplotlib import pyplot as plt
x = [i for i in range(len(datos))]

plt.plot(x, datos)
plt.show()







