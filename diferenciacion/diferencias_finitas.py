import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Variable, función y derivada simbólicas
x = sp.Symbol('x')

f = sp.exp(x) * sp.sin(x)

df = sp.diff(f, x)

# Funcion y derivada numérica
fn = sp.lambdify(x, f, 'numpy')

dfn = sp.lambdify(x, df, 'numpy')

# intervalo de valores
xn = np.linspace(0, 2, 100)

# Paso
h = 0.1

# Diferencias finitas

def DF_Adelante(f, xn, h):
    return (f(xn + h) - f(xn)) / h

def DF_Atras(f, xn, h):
    return (f(xn) - f(xn - h)) / h

def DF_Centrada(f, xn, h):
    return (f(xn + h) - f(xn - h)) / (2*h)

# Diferencias finitas evaluadas
DFAd = DF_Adelante(fn, xn, h)

DFAt = DF_Atras(fn, xn, h)

DFC = DF_Centrada(fn, xn, h)

# graficas
plt.plot(xn, fn(xn), color='blue',
         label=r'$f(x)=e^x\sin(x)$')

plt.plot(xn, dfn(xn), color='black',
         label=r"$f'(x)=e^x[\sin(x)+\cos(x)]$")

plt.plot(xn, DFAd, '--', color='red',
         label=r"$ f'(x_i) \approx \frac{f(x_i + h) - f(x_i)}{h}$")

plt.plot(xn, DFC, '--', color='orange',
         label=r"$ f'(x_i) \approx \frac{f(x_i) - f(x_i - h)}{h}$")

plt.plot(xn, DFAt, '--', color='green',
         label=r"$ f'(x_i) \approx \frac{f(x_i + h) - f(x_i - h)}{2h}$")

# Etiquetas

plt.xlabel('x')

plt.ylabel('f(x)')

plt.title('Diferenciación numérica', fontsize=20)

plt.legend(fontsize=12)

plt.grid()

plt.show()
