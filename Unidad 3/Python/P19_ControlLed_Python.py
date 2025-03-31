
#pyserial ....
import serial as control

arduino = control.Serial("/dev/cu.usbmodem11301",   ## COM?
                         baudrate=9600,
                         timeout=1)

while True:
    v = input("valor de control para el led:")
    arduino.write(v.encode())

