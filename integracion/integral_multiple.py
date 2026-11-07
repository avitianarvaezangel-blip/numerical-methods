import numpy as np
import sympy as sp
import pandas as pd
import matplotlib.pyplot as plt


# Integral doble sobre un rectangulo: integrar primero respecto de y.
x, y = sp.symbols('x y', real=True)
f = x**2 + y**2 + sp.exp(x + y)
x0, xn = 0, 2
y0, yn = 0, 1
ItMax = 7
tol = 1e-7

I_exacta = sp.simplify(sp.integrate(f, (y, y0, yn), (x, x0, xn)))
I = float(I_exacta)
fn = sp.lambdify((x, y), f, 'numpy')


def Simpson_Doble(f, x0, xn, y0, yn, nx, ny):

    if not all(np.isfinite(v) for v in (x0, xn, y0, yn)) or xn <= x0 or yn <= y0:
        raise ValueError("Los limites deben ser finitos y definir un rectangulo de area positiva.")
    for n in (nx, ny):
        if isinstance(n, (bool, np.bool_)) or not isinstance(n, (int, np.integer)) or n < 2 or n % 2:
            raise ValueError("nx y ny deben ser enteros pares de al menos dos subintervalos.")

    hx = (xn - x0) / nx
    hy = (yn - y0) / ny
    xi = np.linspace(x0, xn, nx + 1)
    yi = np.linspace(y0, yn, ny + 1)
    X, Y = np.meshgrid(xi, yi)

    # Pesos 1,4,2,...,4,1 en cada direccion.
    wx = np.ones(nx + 1)
    wy = np.ones(ny + 1)
    wx[1:-1:2], wx[2:-1:2] = 4, 2
    wy[1:-1:2], wy[2:-1:2] = 4, 2

    Z = np.asarray(f(X, Y))
    if np.iscomplexobj(Z):
        raise ValueError("La funcion debe tener valores reales.")
    Z = np.broadcast_to(np.asarray(Z, dtype=float), X.shape)
    if not np.all(np.isfinite(Z)):
        raise ValueError("La funcion produjo valores no finitos en la malla.")

    # Producto de las dos reglas de Simpson: (hx/3)*(hy/3).
    return float((hx * hy / 9) * np.sum(wy[:, None] * wx[None, :] * Z))


datos = []
anterior = None
convergio = False

for j in range(ItMax):
    n = 2**(j + 1)
    Id = Simpson_Doble(fn, x0, xn, y0, yn, n, n)
    error = abs(I - Id)
    et = 100 * error / abs(I) if I != 0 else np.nan
    ea = 100 * abs((Id - anterior) / Id) if anterior is not None and Id != 0 else np.nan
    datos.append([n, n, Id, error, et, ea])

    # Criterio de refinamiento, independiente de la integral exacta.
    if anterior is not None and abs(Id - anterior) <= tol * max(1.0, abs(Id)):
        convergio = True
        break
    anterior = Id

tabla = pd.DataFrame(datos, columns=['nx', 'ny', 'I', 'error absoluto', 'et(%)', 'ea(%)'])
print("Integral exacta =", I_exacta)
print("Valor numerico de referencia =", I)
print("Integral doble por Simpson =", Id)
print("\nTabla de refinamiento:\n")
print(tabla.to_string(index=False, float_format=lambda valor: f"{valor:.6e}"))
print("Criterio de refinamiento alcanzado =", convergio)

# Superficie sobre el dominio y error de refinamiento
xi = np.linspace(x0, xn, 60)
yi = np.linspace(y0, yn, 60)
X, Y = np.meshgrid(xi, yi)
Z = np.broadcast_to(fn(X, Y), X.shape)
fig = plt.figure(figsize=(13, 6))
ax = fig.add_subplot(121, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.85)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x,y)')
ax.set_title('Integral doble: dominio rectangular')

ax2 = fig.add_subplot(122)
ax2.loglog(tabla['nx'], tabla['error absoluto'], 'bo-')
ax2.set_xlabel('Subintervalos en cada direccion')
ax2.set_ylabel('Error absoluto verdadero')
ax2.set_title('Refinamiento de Simpson 1/3 doble')
ax2.grid(True, which='both')
fig.tight_layout()
plt.show()
