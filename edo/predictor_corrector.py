import numpy as np
import matplotlib.pyplot as plt


# Mismo problema de euler.py: y' = (x**2-1)/y**2, y(0) = 2.
def g(x):
    return np.cbrt(x**3 - 3*x + 8)


def f(x, y):
    return (x**2 - 1) / y**2


def Paso_RK4(f, x, y, h):
    k1 = f(x, y)
    k2 = f(x + h/2, y + h*k1/2)
    k3 = f(x + h/2, y + h*k2/2)
    k4 = f(x + h, y + h*k3)
    return y + h * (k1 + 2*k2 + 2*k3 + k4) / 6


def Predictor_Corrector(f, x0, y0, h, n):
    if isinstance(n, (bool, np.bool_)) or not isinstance(n, (int, np.integer)) or n < 0:
        raise ValueError("n debe ser un entero no negativo.")
    if not all(np.isfinite(v) for v in (x0, y0, h)) or h <= 0:
        raise ValueError("x0 e y0 deben ser finitos; h debe ser positivo y finito.")
    x = x0 + h * np.arange(n + 1)
    y = np.zeros(n + 1)
    y[0] = y0
    # Arrancar los primeros tres pasos con RK4; no con la solucion exacta.
    F = np.zeros(n + 1)
    F[0] = f(x[0], y[0])
    for i in range(min(3, n)):
        y[i + 1] = Paso_RK4(f, x[i], y[i], h)
        F[i + 1] = f(x[i + 1], y[i + 1])

    for i in range(3, n):
        predictor = y[i] + h*(55*F[i] - 59*F[i-1] + 37*F[i-2] - 9*F[i-3])/24
        pendiente_predicha = f(x[i + 1], predictor)
        # Una sola correccion AM4, seguida de una nueva evaluacion (PECE).
        y[i + 1] = y[i] + h*(9*pendiente_predicha + 19*F[i] - 5*F[i-1] + F[i-2])/24
        F[i + 1] = f(x[i + 1], y[i + 1])
    if not np.all(np.isfinite(y)):
        raise FloatingPointError("La integracion produjo valores no finitos.")
    return x, y


n = 10
h = 0.2
X, Y = Predictor_Corrector(f, 0, 2, h, n)
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
plt.plot(X, Y, 'ro-', label='Predictor-corrector AB4-AM4 (PECE)')
plt.title('Predictor-corrector AB4-AM4 (PECE)', fontsize=18)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()
