import numpy as np 

import sympy as sp

import matplotlib.pyplot as plt

def Newton_R(f, x0, tol=1e-10,ItMax = 100):
    
    x = sp.Symbol('x')
    
    df = sp.diff(f, x)
    
    for i in range(ItMax):
        
        fx = f.subs(x, x0).evalf()
        dfx = df.subs(x, x0).evalf()
        
        if dfx == 0:
            print("raiz")
            return None
        
        xi = x0 - fx/dfx
        
        if abs(xi - x0) < tol:
            
            return xi, i + 1
        x0 = xi 
        
    return x0 , ItMax


x = sp.Symbol('x')

f = x*sp.log(x) - 10 

R,It = Newton_R(f, 5)

fn = sp.lambdify(x, f, 'numpy')

xii = np.linspace(4.5, 6, 100)

fxi = fn(xii)

plt.plot(xii, fxi, label='f(x) = x ln(x) - 10')

plt.axhline(0, color='k')

plt.legend()

plt.xlabel('x')

plt.ylabel('f(x)')

plt.grid()

plt.title("Metodo de Newton-Raphson")


x = [R]
y = [0]

plt.scatter(x, y, color='r')


print("R =",R)


print("It =",It)
    
    
    
    