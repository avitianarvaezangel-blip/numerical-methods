import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


# Variables simbolicas
x = sp.Symbol('x', real=True)
n = sp.Symbol('n', integer=True, positive=True)

# Periodo y frecuencia angular fundamental
T = 2 * sp.pi
w0 = (2 * sp.pi) / T

# Funcion en la primera media onda, 0 <= x <= T/2
g = x**2 * (T / 2 - x)

# Construir un periodo en [-T/2,T/2] usando f(x+T/2) = -f(x).
# Fuera de este intervalo se entiende su extension periodica.
f = sp.Piecewise(
    (-g.subs(x, x + T / 2), x < 0),
    (g, True)
)

print("f(x) en un periodo =", f)
print("Simetria de media onda: f(x + T/2) = -f(x)")
print("Solo aparecen armonicos impares; pueden existir senos y cosenos.")

# La media es cero y todos los coeficientes de indice par son cero.
a0 = sp.Integer(0)

# Para n impar, las integrales se reducen a media onda.
an_impar = (4 / T) * sp.integrate(g * sp.cos(n * w0 * x), (x, 0, T / 2))
bn_impar = (4 / T) * sp.integrate(g * sp.sin(n * w0 * x), (x, 0, T / 2))
an_impar = sp.refine(sp.simplify(an_impar), sp.Q.odd(n))
bn_impar = sp.refine(sp.simplify(bn_impar), sp.Q.odd(n))

an = sp.Piecewise((an_impar, sp.Eq(sp.Mod(n, 2), 1)), (0, True))
bn = sp.Piecewise((bn_impar, sp.Eq(sp.Mod(n, 2), 1)), (0, True))

print("a0 =", a0)
print("an =", an)
print("bn =", bn)

# Armonico maximo: N = 5 incluye n = 1, 3 y 5.
N = 5
S = a0 / 2

for i in range(1, N + 1, 2):
    ai = an.subs(n, i)
    bi = bn.subs(n, i)
    S = S + ai * sp.cos(i * w0 * x) + bi * sp.sin(i * w0 * x)

S = sp.simplify(S)
print("S =", S)

# Funciones numericas y puntos de evaluacion
fn = sp.lambdify(x, f, 'numpy')
Sn = sp.lambdify(x, S, 'numpy')
xi = np.linspace(-float(T / 2), float(T / 2), 600)
fi = np.broadcast_to(fn(xi), xi.shape)
Si = np.broadcast_to(Sn(xi), xi.shape)

plt.figure(figsize=(12, 7))
plt.plot(xi, fi, label=r'$f(x)$: funcion original', color='b')
plt.plot(xi, Si, color='r',
         label=rf'$S_{{{N}}}(x)=\sum_{{n=1,3,\ldots}}^{{{N}}}'
               r'[a_n\cos(n\omega_0x)+b_n\sin(n\omega_0x)]$')
plt.legend(fontsize=12)
plt.title('Serie de Fourier: simetria de media onda', fontsize=20)
plt.xlabel('x')
plt.ylabel(r'$f(x),\ S_N(x)$')
plt.grid()
plt.tight_layout()
plt.show()
