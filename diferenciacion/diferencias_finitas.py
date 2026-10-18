import numpy as np
import matplotlib.pyplot as plt

# Funcion
def f(x):
    return x**3

# Derivada 
def df(x):
    return 3*x**2

# [xi-1,xi,xi+1]

x = np.array([2.75,3,3.25])

h = x[2] - x[1]


def df_Adelante(f, x, h):
    return (f(x[2]) - f(x[1]))/h

def df_Atras(f, x, h):
    return (f(x[1]) - f(x[0]))/h

def df_Centro(f, x, h):
    return (f(x[2]) - f(x[0]))/(2*h)


xi = np.linspace(1, 5,100)

def df_n(f, x, h):
    return (f(x + h) - f(x - h))/(2*h)

fi = f(xi)


dfi = df(xi)

df_a = df_Adelante(f, x, h)

df_at = df_Atras(f, x, h)

df_c = df_Centro(f, x, h)

dfn = df_n(f, xi, h)

print("Diferencia hacia delante =",df_a)

print("Diferencia hacia atras =",df_at)

print("Diferencia centrada =",df_c)


df_n = np.array([df_a, df_at, df_c])

plt.plot(xi, fi, label='f(x) = x^3')

plt.plot(xi, dfi,  label='df(x) = 3 x^2')

plt.scatter(x, df_n, color='r', label='Diferencias finitas')

plt.plot(xi, dfn,'--', label='Diferenciacion Centrada')

plt.title("Diferenciación Numérica")

plt.xlabel("x")

plt.ylabel("f(x)")

plt.legend()

plt.grid()

plt.show()