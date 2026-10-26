import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Variable, función y 2da derivada simbólicas
x = sp.Symbol('x')

f = sp.exp(x) * sp.sin(x)

df = sp.diff(f, x, 2)


# Funcion y 2da derivada numérica
fn = sp.lambdify(x, f, 'numpy')

dfn = sp.lambdify(x, df, 'numpy')

# intervalo de valores
xn = np.linspace(0, 2, 100)

# Paso
h = 0.1

# Diferencias finitas para las 2das derivadas

def DF_Adelante_2da(f, xn, h):
    return (f(xn + 2*h) - 2*f(xn + h) + f(xn)) / h**2

def DF_Atras_2da(f, xn, h):
    return (f(xn) - 2*f(xn - h) + f(xn -2*h)) / h**2

def DF_Centrada_2da(f, xn, h):
    return (f(xn + h) - 2*f(xn) + f(xn - h)) / h**2

# Diferencias finitas evaluadas
DFAd = DF_Adelante_2da(fn, xn, h)

DFAt = DF_Atras_2da(fn, xn, h)

DFC = DF_Centrada_2da(fn, xn, h)

# graficas
plt.plot(xn, fn(xn), color='blue',
         label=r'$f(x)=e^x\sin(x)$')

plt.plot(xn, dfn(xn), color='black',
         label=r"$f''(x)=2 e^{x} \cos{\left(x \right)}$")

plt.plot(xn, DFAd, '--', color='red',
         label=r"$ f''(x_i) \approx \frac{f(x_i + 2 h) - 2 f(x_i + h) + f(x_i)}{h^2}$")

plt.plot(xn, DFC, '--', color='orange',
         label=r"$ f''(x_i) \approx \frac{f(x_i + h) - 2 f(x_i) + f(x_i - h)}{h^2}$")

plt.plot(xn, DFAt, '--', color='green',
         label=r"$ f''(x_i) \approx \frac{f(x_i) - 2 f(x_i - h) + f(x_i - 2 h)}{h^2}$")

# Etiquetas

plt.xlabel('x')

plt.ylabel('f(x)')

plt.title('Diferenciación numérica (2da Derivada)', fontsize=20)

plt.legend(fontsize=12)

plt.grid()

plt.show()
