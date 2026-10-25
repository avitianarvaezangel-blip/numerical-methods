import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Variables simbólicas
x = sp.Symbol('x')
y = sp.Symbol('y')
n = sp.Symbol('n') #, integer=True, positive=True)

# Datos
f = 100
a = 1
b = 1


An = sp.simplify((2/(a*sp.sinh((n*sp.pi)/a))) *sp.integrate(f*sp.sin((n*sp.pi*x)/a), (x,0,a)))

N = 10

S = 0

for k in range(1, N+1):
    Ak = An.subs(n, k)

    S = S + Ak * sp.sinh((k*sp.pi*y)/a) * sp.sin((k*sp.pi*x)/a)

S = sp.simplify(S)

print("S =",S)

Sf = sp.lambdify((x, y), S, 'numpy')


X = np.linspace(0, a, 100)

Y = np.linspace(0, b, 100)

X, Y = np.meshgrid(X, Y)

Sp = Sf(X, Y)

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

Sup = ax.plot_surface(X, Y, Sp, cmap='jet')

fig.colorbar(Sup, label ='T')


#ax.view_init(90, -90)

plt.show()