
#pyserial ....
import serial as control


arduino = control.Serial("COM7", baudrate=9600, timeout=1)

while True:
    mensaje = arduino.readline().decode().strip()
    print(mensaje)

