import numpy as np 
import matplotlib.pyplot as plt 
import scipy as sc

# Datos
x = np.array([7.6953, 7.9413])
y = np.array([100, 150])

# vector de datos 
xi2 = np.linspace(7.6953, 7.9413, 100)
# yi = y1 + ((y2 - y1)*(xi - x1))/(x2 -x1)  
yi = sc.interpolate.interp1d(x, y, kind="linear")
xi = 7.8
yi2 = yi(xi)  
print("yi = ", yi2)       

# grafica 
plt.plot(x, y,"o")
plt.plot(xi2, yi(xi2), "-")
plt.plot(xi, yi2, "sr")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["Puntos (x,y)","Funcion Lineal Aproximada", "Dato Interpolado"])
plt.title("Interpolacion Lineal")
plt.grid()