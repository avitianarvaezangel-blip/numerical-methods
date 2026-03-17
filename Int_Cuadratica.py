import numpy as np 
import matplotlib.pyplot as plt 
import scipy as sc


def f(x):
    return np.log(x)

# Datos
x = np.array([1, 4, 6])
y = np.array([np.log(1),  np.log(4), np.log(6)])

# vector de datos 
xi = np.linspace(1, 6, 100)
# yi = y1 + ((y2 - y1)*(xi - x1))/(x2 -x1)  
fi = sc.interpolate.interp1d(x, y, kind="quadratic")
xi2 = 2
fi2 = fi(xi2)
p = fi(xi) 
fx = f(xi2) 
fxi = f(xi)

x2 = [2]
y2 = [np.log(2)]
y3 = [fi2]

et = abs((fx - fi2)/fx)*100
print("f(2) =", fx)
print("f(2),Aprox = ", fi2)    
print("et = ",et, "%")   

# grafica 
plt.plot(xi, fxi, color='b', label='f(x) = ln(x)')
plt.plot(xi, p, label='p(x)')
plt.plot(x, y, "o", color='r', label='P1(1, ln(1)) -- P2(4, ln(4))')
plt.plot(x2, y2, 'o', color='k', label='Valor Real')
plt.plot(x2, y3,'o', color='r', label='Valor Interpolado')
plt.legend()
plt.title("Interpolacion Lineal")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.show()