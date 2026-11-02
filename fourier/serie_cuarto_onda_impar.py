import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


# Variables simbolicas
x = sp.Symbol('x', real=True)
n = sp.Symbol('n', integer=True, positive=True)

# Periodo y frecuencia angular fundamental
T = 2 * sp.pi
w0 = (2 * sp.pi) / T

# Funcion en el primer cuarto de onda, 0 <= x <= T/4
g = x

# Reflejar el primer cuarto respecto de T/4 y extender como funcion impar.
# El resultado es una onda triangular en [-T/2,T/2].
f = sp.Piecewise(
    (sp.sign(x) * g.subs(x, sp.Abs(x)), sp.Abs(x) <= T / 4),
    (sp.sign(x) * g.subs(x, T / 2 - sp.Abs(x)), True)
)

print("g(x) en el primer cuarto =", g)
print("f(x) en un periodo =", f)
print("Cuarto de onda impar: f(-x) = -f(x), f(x+T/2) = -f(x).")
print("Solo aparecen senos de armonicos impares.")

a0 = sp.Integer(0)
an = sp.Integer(0)

# Para n impar: bn = (8/T) * integral en el primer cuarto.
bn_impar = (8 / T) * sp.integrate(g * sp.sin(n * w0 * x), (x, 0, T / 4))
bn_impar = sp.simplify(bn_impar)
bn = sp.Piecewise((bn_impar, sp.Eq(sp.Mod(n, 2), 1)), (0, True))

print("a0 =", a0)
print("an =", an)
print("bn =", bn)

# Armonico maximo: se suman solamente n = 1, 3, 5.
N = 5
S = a0 / 2

for i in range(1, N + 1, 2):
    bi = sp.simplify(bn.subs(n, i))
    S = S + bi * sp.sin(i * w0 * x)

S = sp.simplify(S)
print("S =", S)

# Funciones numericas
fn = sp.lambdify(x, f, 'numpy')
Sn = sp.lambdify(x, S, 'numpy')
xi = np.linspace(-float(T / 2), float(T / 2), 600)
fi = np.broadcast_to(fn(xi), xi.shape)
Si = np.broadcast_to(Sn(xi), xi.shape)

plt.figure(figsize=(12, 7))
plt.plot(xi, fi, label=r'$f(x)$: funcion original', color='b')
plt.plot(xi, Si, color='r',
         label=rf'$S_{{{N}}}(x)=\sum_{{n=1,3,\ldots}}^{{{N}}}b_n\sin(n\omega_0x)$')
plt.legend(fontsize=12)
plt.title('Serie de Fourier: cuarto de onda impar', fontsize=20)
plt.xlabel('x')
plt.ylabel(r'$f(x),\ S_N(x)$')
plt.grid()
plt.tight_layout()
plt.show()
