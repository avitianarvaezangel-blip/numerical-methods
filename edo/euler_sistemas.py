import numpy as np
import matplotlib.pyplot as plt


# Sistema y1' = y2, y2' = -y1; y(0) = [1,0].
def g(x):
    return np.stack((np.cos(x), -np.sin(x)), axis=-1)


def f(x, y):
    return np.array([y[1], -y[0]])


def Euler_Sistemas(f, x0, y0, h, n):
    if isinstance(n, (bool, np.bool_)) or not isinstance(n, (int, np.integer)) or n < 0:
        raise ValueError("n debe ser un entero no negativo.")
    y0 = np.array(y0, dtype=float)
    if y0.ndim != 1 or y0.size == 0 or not np.all(np.isfinite(y0)):
        raise ValueError("y0 debe ser un vector real finito no vacio.")
    if not np.isfinite(x0) or not np.isfinite(h) or h <= 0:
        raise ValueError("x0 debe ser finito y h positivo y finito.")
    x = x0 + h*np.arange(n + 1)
    y = np.zeros((n + 1, y0.size))
    y[0] = y0

    def pendiente(t, z):
        valor = np.asarray(f(t, z), dtype=float)
        if valor.shape != y0.shape or not np.all(np.isfinite(valor)):
            raise ValueError("f debe devolver un vector finito del mismo tamano que y0.")
        return valor
    for i in range(n):
        y[i + 1] = y[i] + h*pendiente(x[i], y[i])
    if not np.all(np.isfinite(y)):
        raise FloatingPointError("La integracion produjo valores no finitos.")
    return x, y


n = 50
h = 0.1
X, Y = Euler_Sistemas(f, 0, [1, 0], h, n)
exacta = g(X)
error = np.abs(exacta - Y)
et = np.full_like(Y, np.nan)
np.divide(100*error, np.abs(exacta), out=et, where=exacta != 0)
print("x =", X)
print("y =\n", Y)
print("et(%) =\n", et)
print("Error absoluto maximo por componente =", np.max(error, axis=0))

xi = np.linspace(X[0], X[-1], 400)
plt.figure(figsize=(11, 7))
for j, color in enumerate(('b', 'g')):
    plt.plot(xi, g(xi)[:,j], color=color, label=f'S. Exacta: componente {j+1}')
    plt.plot(X, Y[:,j], 'o--', color=color, markersize=3, label=f'Aproximacion: componente {j+1}')
plt.title('Euler explicito para sistemas', fontsize=18)
plt.xlabel('x')
plt.ylabel('Solucion')
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()
