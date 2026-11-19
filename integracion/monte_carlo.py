import numpy as np
import sympy as sp
import pandas as pd
import matplotlib.pyplot as plt


# Variable y funcion simbolicas: mismo ejemplo de las reglas compuestas
x = sp.Symbol('x', real=True)
f = 2 * x * sp.exp(-x**2) + x**3
x0 = 0
xn = 5
N = 100_000
semilla = 2026

I_exacta = sp.integrate(f, (x, x0, xn))
I = float(I_exacta)
fn = sp.lambdify(x, f, 'numpy')


def Monte_Carlo(f, x0, xn, N, semilla=2026):

    if not np.isfinite(x0) or not np.isfinite(xn) or xn <= x0:
        raise ValueError("Se requieren limites finitos con x0 < xn.")
    if isinstance(N, (bool, np.bool_)) or not isinstance(N, (int, np.integer)) or N < 2:
        raise ValueError("N debe ser un entero de al menos dos muestras.")

    # Muestreo uniforme independiente; la semilla permite repetir el ejemplo.
    generador = np.random.default_rng(semilla)
    muestras = generador.uniform(x0, xn, N)
    valores = np.asarray(f(muestras))
    if np.iscomplexobj(valores):
        raise ValueError("La funcion debe tener valores reales.")
    valores = np.broadcast_to(np.asarray(valores, dtype=float), muestras.shape)
    if not np.all(np.isfinite(valores)):
        raise ValueError("La funcion produjo valores no finitos.")

    # Reutilizar prefijos de la misma muestra para construir el historial.
    tamanos = np.unique(np.append(np.geomspace(min(100, N), N, 8).astype(int), N))
    datos = []
    anterior = None

    for n in tamanos:
        media = np.mean(valores[:n])
        desviacion = np.std(valores[:n], ddof=1)
        estimacion = (xn - x0) * media
        error_estandar = (xn - x0) * desviacion / np.sqrt(n)

        # Intervalo normal aproximado, puntual, del 95%; no es una cota exacta.
        inferior = estimacion - 1.96 * error_estandar
        superior = estimacion + 1.96 * error_estandar
        ea = np.nan
        if anterior is not None and estimacion != 0:
            ea = abs((estimacion - anterior) / estimacion) * 100
        datos.append([n, estimacion, error_estandar, inferior, superior, ea])
        anterior = estimacion

    tabla = pd.DataFrame(datos, columns=[
        'n', 'I', 'error estandar', 'IC95 inferior', 'IC95 superior', 'ea(%)'
    ])
    return float(estimacion), tabla, muestras, valores


Im, tabla, muestras, valores = Monte_Carlo(fn, x0, xn, N, semilla)

# La referencia exacta solo se usa para comparar, no para estimar la integral.
tabla['error absoluto'] = np.abs(tabla['I'] - I)
tabla['et(%)'] = 100 * tabla['error absoluto'] / abs(I) if I != 0 else np.nan

print("Integral exacta =", I_exacta)
print("Valor numerico de referencia =", I)
print("Integral Monte Carlo =", Im)
print("Semilla =", semilla)
print("\nTabla de resultados:\n")
print(tabla.to_string(index=False, float_format=lambda valor: f"{valor:.6e}"))
print("El intervalo del 95% es aproximado; el error no disminuye en cada muestra.")

xi = np.linspace(x0, xn, 400)
fi = np.broadcast_to(fn(xi), xi.shape)
fig, ax = plt.subplots(2, 1, figsize=(12, 9))

ax[0].plot(xi, fi, color='black', label=rf'$f(x) = {sp.latex(f)}$')
ax[0].fill_between(xi, fi, color='green', alpha=0.2, label='Area de integracion')
ax[0].scatter(muestras[:200], valores[:200], s=12, color='b', alpha=0.5,
              label='Primeras 200 evaluaciones aleatorias')
ax[0].set_title('Integracion de Monte Carlo por promedio de muestras', fontsize=20)
ax[0].set_xlabel('x')
ax[0].set_ylabel('f(x)')

ax[1].plot(tabla['n'], tabla['I'], 'bo-', label='Estimacion Monte Carlo')
ax[1].fill_between(tabla['n'], tabla['IC95 inferior'], tabla['IC95 superior'],
                   color='b', alpha=0.15, label='Intervalo aproximado del 95%')
ax[1].axhline(I, color='r', linestyle='--', label='Integral exacta')
ax[1].set_xscale('log')
ax[1].set_xlabel('Numero de muestras')
ax[1].set_ylabel('Integral')

for eje in ax:
    eje.legend(fontsize=10)
    eje.grid()
fig.tight_layout()
plt.show()
