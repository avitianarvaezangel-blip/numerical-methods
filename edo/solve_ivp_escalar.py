import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


# Mismo problema de euler.py: y' = (x**2-1)/y**2, y(0) = 2.
def g(x):
    return np.cbrt(x**3 - 3*x + 8)


def f(x, y):
    return (x**2 - 1) / y**2


# solve_ivp usa paso adaptativo interno; t_eval fija solo donde mostrar la salida.
X = np.linspace(0, 2, 101)
resultado = solve_ivp(f, (X[0], X[-1]), [2], method='RK45',
                      t_eval=X, rtol=1e-9, atol=1e-12)
if not resultado.success:
    raise RuntimeError(resultado.message)
Y = resultado.y[0]
error = np.abs(g(X) - Y)
print("x =", X)
print("y =", Y)
print("Error absoluto maximo =", np.max(error))
print("Evaluaciones de f =", resultado.nfev)
xi = np.linspace(X[0], X[-1], 400)
plt.figure(figsize=(11, 7))
plt.plot(xi, g(xi), color='b', label='S. Exacta')
plt.plot(X, Y, 'r.', label='solve_ivp RK45')
plt.title('SciPy solve_ivp: EDO escalar', fontsize=18)
plt.xlabel('x')
plt.ylabel('Solucion')
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()
