import numpy as np
import matplotlib.pyplot as plt


# Mismo problema de euler.py: y' = (x**2-1)/y**2, y(0) = 2.
def g(x):
    return np.cbrt(x**3 - 3*x + 8)


def f(x, y):
    return (x**2 - 1) / y**2


def dfdy(x, y):
    return -2 * (x**2 - 1) / y**3


def Newton(residuo, derivada, z, tol, ItMax):
    if not np.isfinite(tol) or tol <= 0 or not isinstance(ItMax, (int, np.integer)) or ItMax < 1:
        raise ValueError("Newton requiere tolerancia positiva e iteraciones enteras positivas.")
    for _ in range(ItMax):
        r = residuo(z)
        if not np.isfinite(r):
            raise FloatingPointError("Residuo no finito en Newton.")
        if abs(r) <= tol * max(1.0, abs(z)):
            return z
        d = derivada(z)
        if not np.isfinite(d) or abs(d) <= np.finfo(float).eps:
            raise ValueError("Derivada nula o demasiado pequena en Newton.")
        z = z - r / d
    if np.isfinite(z) and abs(residuo(z)) <= tol * max(1.0, abs(z)):
        return z
    raise RuntimeError("Newton no convergio; reducir h o revisar la ecuacion.")


def Euler_Implicito(f, dfdy, x0, y0, h, n, tol=1e-12, ItMax=30):
    if isinstance(n, (bool, np.bool_)) or not isinstance(n, (int, np.integer)) or n < 0:
        raise ValueError("n debe ser un entero no negativo.")
    if not all(np.isfinite(v) for v in (x0, y0, h)) or h <= 0:
        raise ValueError("x0 e y0 deben ser finitos; h debe ser positivo y finito.")
    x = x0 + h * np.arange(n + 1)
    y = np.zeros(n + 1)
    y[0] = y0
    for i in range(n):
        # Resolver y_(i+1) - y_i - h*f(x_(i+1),y_(i+1)) = 0.
        predictor = y[i] + h * f(x[i], y[i])
        y[i + 1] = Newton(lambda z: z - y[i] - h*f(x[i + 1], z),
                          lambda z: 1 - h*dfdy(x[i + 1], z), predictor, tol, ItMax)
    if not np.all(np.isfinite(y)):
        raise FloatingPointError("La integracion produjo valores no finitos.")
    return x, y


n = 10
h = 0.2
X, Y = Euler_Implicito(f, dfdy, 0, 2, h, n)
exacta = g(X)
error = np.abs(exacta - Y)
et = np.full_like(Y, np.nan)
np.divide(100 * error, np.abs(exacta), out=et, where=exacta != 0)
print("x =", X)
print("y =", Y)
print("et(%) =", et)
print("Error absoluto maximo =", np.max(error))

xi = np.linspace(X[0], X[-1], 400)
plt.figure(figsize=(10, 6))
plt.plot(xi, g(xi), color='b', label='S. Exacta')
plt.plot(X, Y, 'ro-', label='Euler implicito')
plt.title('Euler implicito', fontsize=18)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()
