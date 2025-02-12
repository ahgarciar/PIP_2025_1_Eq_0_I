
from matplotlib import pyplot as plt
# tabular para x.....

lim_inferior = -10
lim_superior = 10

x = []
for i in range(lim_inferior, lim_superior+1, 1):
    x.append(i)
print("X:", x)

import math
y = []
for i in range(len(x)):
    funcion = "math.sin(x)"
    funcion = funcion.replace("x", str(i))
    resultado = eval(funcion)
    y.append(resultado)
print("Y: ", y)

plt.plot(x, y)
plt.show()