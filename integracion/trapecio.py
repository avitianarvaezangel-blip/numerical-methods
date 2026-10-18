import numpy as np
import sympy as sp
import matplotlib.pyplot as plt 


x = sp.symbols('x')

f = 2 * x * sp.exp(-x**2) + x**3

print(sp.latex(f))

x0 = 0 

xn = 5

n = 3

I = sp.integrate(f , (x, x0, xn)).evalf()

fn = sp.lambdify(x, f, 'numpy')

def R_Trapecio(f, x0, xn, n):
    
    h = (xn - x0)/n
    
    S = f(x0) + f(xn)
    
    for i in range(1, n):
        
        xi = x0 + i*h
        
        S = S + 2*f(xi)
        
    return(h/2)*S

It = R_Trapecio(fn, x0, xn, n)

xi = np.linspace(x0, xn, 100)

xin = np.linspace(x0, xn, n + 1)

print(I)

print(It)

plt.plot(xi, fn(xi), label=r'$f(x) = x^{3} + 2 x e^{- x^{2}}$', color='black', lw=3)

plt.axhline(0, color='gray')

plt.fill_between(xi, fn(xi), where=(xi >= x0) & (xi <= xn), color='red', alpha=0.5, label=r'$\int_{x_0}^{x_n} f(x) dx$')

plt.fill_between(xin, fn(xin), where=(xin >= x0) & (xin <= xn), color='green', alpha=0.5, label=r'$\frac{h}{2} \left[ f(x_0) + 2 \sum_{i = 0}^{n - 1} f(x_i)  + f(x_n)\right]$')

plt.vlines(xin,0,  fn(xin), color='blue', lw=1.5)

plt.scatter(xin, fn(xin), color='blue', label=r'$f(x_i)$')

plt.plot(xin, fn(xin), color='blue', lw=1.5)

plt.title("Regla del Trapecio", fontsize=20)

plt.xlabel("x", fontsize=12)

plt.ylabel("f(x)", fontsize=12)

plt.legend(fontsize=12)

plt.grid()
