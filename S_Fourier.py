import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.Symbol('x')
n = sp.Symbol('n', integer=True, positive=True)

f = -x/(2*sp.pi) + 1

# coeficientes
a0 = (1/sp.pi)*sp.integrate(f, (x,0,2*sp.pi))

an = (1/sp.pi)*sp.integrate(f*sp.cos(n*x), (x,0,2*sp.pi))

bn = (1/sp.pi)*sp.integrate(f*sp.sin(n*x), (x,0,2*sp.pi))

print("a0 =", sp.simplify(a0))
print("an =", sp.simplify(an))
print("bn =", sp.simplify(bn))

# aproximacion de Fourier
N = 20

S = a0/2

for k in range(1,N+1):
    ak = an.subs(n,k)
    bk = bn.subs(n,k)
    S = S + ak*sp.cos(k*x) + bk*sp.sin(k*x)

S = sp.simplify(S)

# funciones numericas
f_num = sp.lambdify(x,f,'numpy')
S_num = sp.lambdify(x,S,'numpy')

xx = np.linspace(0,2*np.pi,400)

plt.plot(xx,f_num(xx),label='f(x)')
plt.plot(xx,S_num(xx),'--',label='Serie Fourier N=20')

plt.legend()
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Serie de Fourier")

plt.show()
