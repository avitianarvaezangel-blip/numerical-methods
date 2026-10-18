import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

x = sp.Symbol('x')

f = sp.sin(x)

i = sp.integrate(f, (x, 0, 4)).evalf()

print("f(x) =", f)

print("Integral Exacta =", i)

fn = sp.lambdify(x, f, 'numpy')

xi = np.linspace(0, 4 , 100)

def Traprecio(f, x0, xn, n):
    h = (xn - x0)/n
    
    S = f(x0) + f(xn)
    
    for i in range(1, n):
        
        x = x0 + i*h
        
        S = S + 2*f(x)
        
    return (h/2)*S

n = 10

In_T = Traprecio(fn, 0, 4, n)

xin = np.linspace(0, 4, n + 1)

print("Para",n,"Trapecios")

print("Regla del Trapecio =", In_T)

fi = fn(xi)
fin = fn(xin)

plt.plot(xi, fi, label='f(x) = 1 - exp(2*x)', color='b')

plt.scatter(xin, fin, color='r', label="x_i")

plt.vlines(xin, 0, fin, color='b', label='Trapecios')

plt.axhline(0, color='k')

plt.fill_between(xi, fi, where=(xi >= 0) & (xi <= 4), alpha=0.6, color='g', label='Area')

plt.grid()

plt.title("Regla del Trapecio")

plt.xlabel("x")

plt.ylabel("f(x)")

plt.legend()
