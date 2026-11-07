import numpy as np
import sympy as sp
import matplotlib.pyplot as plt 


x = sp.Symbol('x')

t = sp.Symbol('t')

n = sp.Symbol('n', integer=True, positive=True)

f = 100

L = sp.pi

k = 1 

An = sp.simplify((2/L)* sp.integrate(f*sp.sin(n*sp.pi*x/L),(x,0,L)))

print("An =", An)

N = 5

S = 0 

for i in range(1 , N + 1 ):
    
    Ai = An.subs(n,i)
    
    S = S + Ai * sp.exp(-1*((i*sp.pi/L)**2)*k*t) * sp.sin(i*sp.pi*x/L)
    
S = sp.simplify(S)
    
print("\n")
    
print("S =", S)


Sn = sp.lambdify((x,t), S, 'numpy')

X = np.linspace(0, np.pi, 100)

T = np.linspace(0, 1.5, 100)

X,T = np.meshgrid(X,T)

Sp = Sn(X,T)

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

Sup = ax.plot_surface(X, T, Sp, cmap='jet')

plt.xlabel("Posicion")

plt.ylabel("Tiempo")

ax.view_init(90,-90)

plt.colorbar(Sup, label='Temperatura')

