import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


# Variable x simbolica y real
x = sp.Symbol('x', real=True)

# Variable n simbolica y entera: incluye frecuencias negativas y positivas
n = sp.Symbol('n', integer=True)

# Funcion simbolica
f = sp.exp(x)

# Periodo e intervalo de integracion
T = 2 * sp.pi
a = -T / 2
b = T / 2

# Omega 0
w0 = (2 * sp.pi) / T

# Coeficientes de Fourier complejos
# c_n = (1/T) * integral de f(x) * exp(-i*n*w0*x) en un periodo
c0 = (1 / T) * sp.integrate(f, (x, a, b))
cn = (1 / T) * sp.integrate(f * sp.exp(-sp.I * n * w0 * x), (x, a, b))

# Coeficientes simplificados, separando las partes real e imaginaria
c0 = sp.simplify(c0)
cn = sp.simplify(sp.re(cn)) + sp.I * sp.simplify(sp.im(cn))

# Mostrar coeficientes
print("c0 =", c0)
print("cn =", cn)

# Serie compleja de Fourier
# N armonicos a cada lado de cero: 2*N + 1 terminos
N = 20

S = 0

for i in range(-N, N + 1):
    # El termino cero se calcula por separado para evitar singularidades
    # removibles en la expresion general de cn al cambiar la funcion.
    ci = c0 if i == 0 else sp.simplify(cn.subs(n, i))
    S = S + ci * sp.exp(sp.I * i * w0 * x)

print("S =", S)

# Funciones numericas
fn = sp.lambdify(x, f, 'numpy')
Sn = sp.lambdify(x, S, 'numpy')

xi = np.linspace(float(a), float(b), 100)
fi = np.broadcast_to(fn(xi), xi.shape)
Si = np.broadcast_to(Sn(xi), xi.shape)

# Para esta funcion real, c_{-n} = conjugado(c_n) y la suma es real.
# La parte imaginaria numerica debe ser cercana a cero por redondeo.
print("Residuo imaginario maximo =", np.max(np.abs(np.imag(Si))))

plt.figure(figsize=(12, 7))

plt.plot(xi, fi, label=rf'$f(x) = {sp.latex(f)}$', color='b')

plt.plot(xi, np.real(Si),
         label=rf'$\mathrm{{Re}}(S_{{{N}}}(x)),\quad '
               r'S_N(x)=\sum_{n=-N}^{N} c_n e^{i n \omega_0 x}$',
         color='r')

plt.legend(fontsize=12)
plt.title("Serie compleja de Fourier", fontsize=20)
plt.xlabel('x')
plt.ylabel(r'$f(x),\ \mathrm{Re}(S_N(x))$')
plt.grid()
plt.tight_layout()

# La extension periodica de exp(x) tiene un salto en los extremos.
# Alli la serie converge al promedio (exp(-pi) + exp(pi))/2, no a exp(x).
plt.show()
