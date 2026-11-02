import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


# Variables reales y parametro positivo
x = sp.Symbol('x', real=True)
omega = sp.Symbol('omega', real=True)
a = sp.Symbol('a', positive=True)

# Funcion absolutamente integrable en toda la recta
f = sp.exp(-a * sp.Abs(x))

# Definicion con frecuencia angular, sin factor de normalizacion:
# F(omega) = integral de f(x)*exp(-i*omega*x) desde -infinito a infinito.
kernel = sp.exp(-sp.I * omega * x)
definicion = sp.Integral(f * kernel, (x, -sp.oo, sp.oo))
print("f(x) =", f)
print("Definicion de F(omega) =", definicion)

# Separar en x = 0 para eliminar el valor absoluto.
# Como a > 0 y omega es real, ambas integrales impropias convergen
# absolutamente. conds='none' usa estas hipotesis ya establecidas.
f_negativa = sp.refine(f, sp.Q.negative(x))
f_positiva = sp.refine(f, sp.Q.positive(x))
I_negativa = sp.integrate(f_negativa * kernel, (x, -sp.oo, 0), conds='none')
I_positiva = sp.integrate(f_positiva * kernel, (x, 0, sp.oo), conds='none')

I_negativa = sp.simplify(I_negativa)
I_positiva = sp.simplify(I_positiva)
F = sp.simplify(I_negativa + I_positiva)

print("Integral en (-infinito,0) =", I_negativa)
print("Integral en (0,infinito) =", I_positiva)
print("F(omega) =", F)
print("F(0), area bajo f =", sp.simplify(F.subs(omega, 0)))

# Valor numerico del parametro para la grafica
a_valor = 1
if not np.isfinite(a_valor) or a_valor <= 0:
    raise ValueError("a_valor debe ser positivo y finito.")

f_evaluada = f.subs(a, a_valor)
F_evaluada = F.subs(a, a_valor)
fn = sp.lambdify(x, f_evaluada, 'numpy')
Fn = sp.lambdify(omega, F_evaluada, 'numpy')

xi = np.linspace(-6 / a_valor, 6 / a_valor, 601)
wi = np.linspace(-10 * a_valor, 10 * a_valor, 601)
fi = np.broadcast_to(fn(xi), xi.shape)
Fi = np.broadcast_to(np.asarray(Fn(wi), dtype=complex), wi.shape)

fig, ax = plt.subplots(2, 1, figsize=(12, 9))

ax[0].plot(xi, fi, color='b', label=rf'$f(x) = {sp.latex(f_evaluada)}$')
ax[0].set_title('Transformada continua de Fourier por integral impropia', fontsize=20)
ax[0].set_xlabel('x')
ax[0].set_ylabel(r'$f(x)$')

ax[1].plot(wi, np.real(Fi), color='r',
           label=rf'$\mathrm{{Re}}(F(\omega)) = {sp.latex(F_evaluada)}$')
ax[1].plot(wi, np.imag(Fi), color='g', linestyle='--', label=r'$\mathrm{Im}(F(\omega)) = 0$')
ax[1].set_xlabel(r'$\omega$ (frecuencia angular)')
ax[1].set_ylabel(r'$F(\omega)$')
ax[1].set_title(r'$F(\omega)=\int_{-\infty}^{\infty} f(x)e^{-i\omega x}\,dx$', fontsize=16)

for eje in ax:
    eje.legend(fontsize=12)
    eje.grid()

fig.tight_layout()
plt.show()
