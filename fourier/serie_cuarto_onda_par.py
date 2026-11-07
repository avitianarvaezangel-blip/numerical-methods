import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


# Variables simbolicas
x = sp.Symbol('x', real=True)
n = sp.Symbol('n', integer=True, positive=True)

# Periodo y frecuencia angular fundamental
T = 2 * sp.pi
w0 = (2 * sp.pi) / T

# Funcion en el primer cuarto de onda, 0 <= x <= T/4.
# El valor en T/4 es cero para que la extension sea continua.
g = (T / 4)**2 - x**2

# Extension par y con simetria de media onda en [-T/2,T/2]:
# f(-x) = f(x), f(x+T/2) = -f(x).
f = sp.Piecewise(
    (g.subs(x, sp.Abs(x)), sp.Abs(x) <= T / 4),
    (-g.subs(x, T / 2 - sp.Abs(x)), True)
)

print("g(x) en el primer cuarto =", g)
print("f(x) en un periodo =", f)
print("Cuarto de onda par: funcion par y simetria de media onda.")
print("Solo aparecen cosenos de armonicos impares.")

a0 = sp.Integer(0)
bn = sp.Integer(0)

# Para n impar: an = (8/T) * integral en el primer cuarto.
# Ser par por si solo no bastaria para usar este factor.
an_impar = (8 / T) * sp.integrate(g * sp.cos(n * w0 * x), (x, 0, T / 4))
an_impar = sp.simplify(an_impar)
an = sp.Piecewise((an_impar, sp.Eq(sp.Mod(n, 2), 1)), (0, True))

print("a0 =", a0)
print("an =", an)
print("bn =", bn)

# Armonico maximo, como en Fourier_Par_Impar
N = 5
S = a0 / 2

for i in range(1, N + 1, 2):
    ai = sp.simplify(an.subs(n, i))
    S = S + ai * sp.cos(i * w0 * x)

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
         label=rf'$S_{{{N}}}(x)=\sum_{{n=1,3,\ldots}}^{{{N}}}a_n\cos(n\omega_0x)$')
plt.legend(fontsize=12)
plt.title('Serie de Fourier: cuarto de onda par', fontsize=20)
plt.xlabel('x')
plt.ylabel(r'$f(x),\ S_N(x)$')
plt.grid()
plt.tight_layout()
plt.show()
