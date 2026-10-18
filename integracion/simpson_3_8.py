import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

x = sp.Symbol('x')

f = x * sp.exp(-2*x)

i = sp.integrate(f, (x, 0, 3)).evalf()

print("f(x) =", f)

print("Integral Exacta =", i)

fn = sp.lambdify(x, f, 'numpy')

def Simpson_3_8(f, x0, xn, n):

    h = (xn - x0)/n
    x = np.linspace(x0, xn, n + 1)
    
    S = f(x[0]) + f(x[n])
    
    for i in range(1, n):
        if i % 3 == 0:
            S = S + 2 * f(x[i])
        else:
            S = S + 3 * f(x[i])
    
    return (3*h/8) * S

n = 30

I = Simpson_3_8(fn, 0, 3, n)

print("Integral aproximada =", I)

et = abs((i - I)/i)*100

print("et =", et,"%")


# Gráfica
xi = np.linspace(0, 3, 100)

x2 = np.linspace(0, 3, n + 1)

f2 = fn(x2)

fi = fn(xi)

plt.plot(xi, fi, label='f(x) = x e^(-2x)', color='b')

plt.scatter(x2, f2, color='r', label="x_i")

plt.vlines(x2, 0, f2, color='b', label='Secciones')

plt.fill_between(xi, fi, where=(xi >= 0) & (xi<= 3), color='g', alpha=0.7, label='Area')

plt.axhline(0, color='k')

plt.title("Regla de Simpson 3/8")

plt.xlabel("x")

plt.ylabel("f(x)")


plt.grid()

plt.legend()

