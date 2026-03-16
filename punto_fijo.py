import numpy as np
import matplotlib.pyplot as plt

# Funciones
def fx(x):
    return np.exp(-x) - x

def gx(x):
    return np.exp(-x)

# Parámetros
x0 = 0          
tol = 0.001     
ItMax = 50      

# Iteraciones
i = 1
while i <= ItMax:
    
    x = gx(x0)
    
    if abs(x - x0) <= tol:
        print("La raíz aproximada es:", x)
        print("Número de iteraciones:", i)
        break
    
    x0 = x
    i = i + 1

if i > ItMax:
    print("El método no convergió")

# Intervalo de la gráfica
xi = np.linspace(0, 1, 101)
fi = fx(xi)
gi = gx(xi)
yi = xi

# Gráfica
plt.axhline(0, color='black')
plt.plot(xi, fi, label='f(x) = e^(-x) - x')
plt.plot(xi, gi, label='g(x) = e^(-x)')
plt.plot(xi, yi, label='y = x')

plt.axvline(x, color='red', label='raíz aproximada')

# Leyendas
plt.title('Método del Punto Fijo')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()

plt.show()
