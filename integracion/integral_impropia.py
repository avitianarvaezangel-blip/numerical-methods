import numpy as np
import sympy as sp
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import quad


# Integral impropia sobre un intervalo infinito
x = sp.Symbol('x', real=True)
f = 1 / (1 + x**2)
x0 = 0
xn = np.inf
tol = 1e-10

I_exacta = sp.integrate(f, (x, x0, sp.oo))
I = float(I_exacta)
fn = sp.lambdify(x, f, 'numpy')


def Integral_Impropia(f, x0, xn, tol=1e-10):

    if np.isnan(x0) or np.isnan(xn) or xn <= x0:
        raise ValueError("Los limites deben satisfacer x0 < xn; pueden ser infinitos.")
    if not np.isfinite(tol) or tol <= 0:
        raise ValueError("La tolerancia debe ser positiva y finita.")

    # quad admite limites infinitos y singularidades integrables en extremos.
    resultado = quad(f, x0, xn, epsabs=tol, epsrel=tol, limit=200, full_output=1)
    if len(resultado) > 3:
        raise ValueError("La cuadratura no convergio: " + resultado[3])
    valor, error_estimado = resultado[:2]
    if not np.isfinite(valor) or not np.isfinite(error_estimado):
        raise ValueError("La cuadratura produjo un resultado no finito.")
    return valor, error_estimado


Ii, error_estimado = Integral_Impropia(fn, x0, xn, tol)

# Comparar truncamientos finitos con el calculo que utiliza infinito.
datos = []
for R in (1, 2, 5, 10, 25, 50, 100):
    IR, error_R = Integral_Impropia(fn, x0, R, tol)
    datos.append([R, IR, error_R, abs(I - IR)])
datos.append([np.inf, Ii, error_estimado, abs(I - Ii)])
tabla = pd.DataFrame(datos, columns=['R', 'I de 0 a R', 'error estimado quad', 'error absoluto'])

print("Integral exacta =", I_exacta)
print("Valor numerico de referencia =", I)
print("Integral impropia con limite infinito =", Ii)
print("Error absoluto verdadero =", abs(I - Ii))
print("Error de cuadratura estimado por SciPy =", error_estimado)
print("\nComparacion con limites superiores finitos:\n")
print(tabla.to_string(index=False, float_format=lambda valor: f"{valor:.6e}"))
print("El error estimado por quad es una estimacion numerica, no una cota exacta.")

fig, ax = plt.subplots(2, 1, figsize=(12, 9))
xi = np.linspace(x0, 10, 500)
fi = np.broadcast_to(fn(xi), xi.shape)
ax[0].plot(xi, fi, color='black', label=rf'$f(x) = {sp.latex(f)}$')
ax[0].fill_between(xi, fi, color='green', alpha=0.3, label='Area visible: 0 a 10')
ax[0].set_title('Integral impropia de 0 a infinito', fontsize=20)
ax[0].set_xlabel('x (solo se muestra un intervalo finito)')
ax[0].set_ylabel('f(x)')

finitas = tabla[np.isfinite(tabla['R'])]
ax[1].plot(finitas['R'], finitas['I de 0 a R'], 'bo-', label='Integral truncada en R')
ax[1].axhline(I, color='r', linestyle='--', label=r'$\int_0^\infty f(x)\,dx = \pi/2$')
ax[1].set_xscale('log')
ax[1].set_xlabel('Limite superior finito R')
ax[1].set_ylabel('Integral')
for eje in ax:
    eje.legend(fontsize=11)
    eje.grid()
fig.tight_layout()
plt.show()
