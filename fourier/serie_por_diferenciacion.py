import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


# Variables y funcion simbolicas, como en Fourier_Par_Impar
x = sp.Symbol('x', real=True)
n = sp.Symbol('n', integer=True, positive=True)
f = x**2

T = 2 * sp.pi
w0 = (2 * sp.pi) / T

# Se extiende f periodicamente desde [-T/2,T/2].
# Para recuperar sus coeficientes desde f', f debe ser continua en la union.
if sp.simplify(f.subs(x, -T / 2) - f.subs(x, T / 2)) != 0:
    raise ValueError("Este ejemplo requiere continuidad de f en la union del periodo.")

df = sp.diff(f, x)
d2f_regular = sp.diff(f, x, 2)

print("f(x) =", f)
print("f'(x) dentro del periodo =", df)

# Primero obtener la serie de f' mediante integracion simbolica.
an_df = sp.simplify((2 / T) * sp.integrate(df * sp.cos(n * w0 * x), (x, -T / 2, T / 2)))
bn_df = sp.simplify((2 / T) * sp.integrate(df * sp.sin(n * w0 * x), (x, -T / 2, T / 2)))

print("an de f' =", an_df)
print("bn de f' =", bn_df)

# Si f = a0/2 + sum(an*cos + bn*sin), entonces
# an de f' = n*w0*bn y bn de f' = -n*w0*an.
an = sp.simplify(-bn_df / (n * w0))
bn = sp.simplify(an_df / (n * w0))

# La diferenciacion no determina el valor medio: se calcula por separado.
a0 = sp.simplify((2 / T) * sp.integrate(f, (x, -T / 2, T / 2)))

# Segunda via: al derivar f' periodica aparece su salto en x = T/2.
# Se integra en (0,T) para que esa delta sea interior y se cuente una vez.
salto_df = sp.simplify(df.subs(x, -T / 2) - df.subs(x, T / 2))
d2f_en_periodo = sp.Piecewise(
    (d2f_regular, x < T / 2),
    (d2f_regular.subs(x, x - T), True)
)
d2f_periodica = d2f_en_periodo + salto_df * sp.DiracDelta(x - T / 2)

an_d2f = sp.simplify((2 / T) * sp.integrate(d2f_periodica * sp.cos(n * w0 * x), (x, 0, T)))
bn_d2f = sp.simplify((2 / T) * sp.integrate(d2f_periodica * sp.sin(n * w0 * x), (x, 0, T)))
an_desde_d2f = sp.simplify(-an_d2f / (n * w0)**2)
bn_desde_d2f = sp.simplify(-bn_d2f / (n * w0)**2)

print("f'' periodica en (0,T) =", d2f_periodica)
print("an recuperado desde f'' =", an_desde_d2f)
print("bn recuperado desde f'' =", bn_desde_d2f)
print("Diferencias entre ambas vias =",
      sp.simplify(an - an_desde_d2f), sp.simplify(bn - bn_desde_d2f))

print("a0 =", a0)
print("an =", an)
print("bn =", bn)

# Construir la serie de f con los coeficientes recuperados
N = 5
S = a0 / 2

for i in range(1, N + 1):
    ai = an.subs(n, i)
    bi = bn.subs(n, i)
    S = S + ai * sp.cos(i * w0 * x) + bi * sp.sin(i * w0 * x)

S = sp.simplify(S)
dS = sp.diff(S, x)
print("S =", S)

# Funciones numericas
fn = sp.lambdify(x, f, 'numpy')
dfn = sp.lambdify(x, df, 'numpy')
Sn = sp.lambdify(x, S, 'numpy')
dSn = sp.lambdify(x, dS, 'numpy')
xi = np.linspace(-float(T / 2), float(T / 2), 600)

fig, ax = plt.subplots(2, 1, figsize=(12, 9), sharex=True)
ax[0].plot(xi, fn(xi), label=rf'$f(x) = {sp.latex(f)}$', color='b')
ax[0].plot(xi, Sn(xi), label=rf'$S_{{{N}}}(x)$ recuperada por diferenciacion', color='r')
ax[0].set_title('Serie de Fourier obtenida por diferenciacion', fontsize=20)
ax[0].set_ylabel(r'$f(x),\ S_N(x)$')

ax[1].plot(xi, dfn(xi), label=rf"$f'(x) = {sp.latex(df)}$ en el interior", color='b')
ax[1].plot(xi, dSn(xi), label=rf"$S'_{{{N}}}(x)$", color='r')
ax[1].set_xlabel('x')
ax[1].set_ylabel(r"$f'(x),\ S'_N(x)$")

for eje in ax:
    eje.legend(fontsize=12)
    eje.grid()

# f' tiene un salto periodico: en los extremos su serie converge al promedio.
# f'' incluye una delta; no se representa como una funcion ordinaria con NumPy.
fig.tight_layout()
plt.show()
