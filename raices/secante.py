import numpy as np 
import sympy as sp
import matplotlib.pyplot as plt

def Secante(f, x0, x1, tol=1e-10, ItMax=100):
    
    x = sp.Symbol('x')
    
    for i in range(ItMax):
        
        fx0 = f.subs(x, x0).evalf()
        fx1 = f.subs(x, x1).evalf()
        
        if fx1 - fx0 == 0:
            print("division entre cero")
            return None
        
        xi = x1 - fx1*(x1 - x0)/(fx1 - fx0)
        
        if abs(xi - x1) < tol:
            return xi, i + 1
        
        x0 = x1
        x1 = xi
        
    return x1, ItMax


x = sp.Symbol('x')

f = sp.exp(-x**2) - x 

R, It = Secante(f, 0, 1)

fn = sp.lambdify(x, f, 'numpy')

xii = np.linspace(-0.5, 2.5, 100)

fxi = fn(xii)

plt.plot(xii, fxi, label='f(x) = e**(-x**2) - x')

plt.axhline(0, color='k')

plt.legend()

plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()

plt.title("Metodo de la Secante")

xg = [R]
yg = [0]

plt.scatter(xg, yg, color='r')

print("R =", R)
print("It =", It)
