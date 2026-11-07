import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


# Sistema y1' = y2, y2' = -y1; y(0) = [1,0].
def g(x):
    return np.stack((np.cos(x), -np.sin(x)), axis=-1)


def f(x, y):
    return np.array([y[1], -y[0]])


# solve_ivp usa paso adaptativo interno; t_eval fija solo donde mostrar la salida.
X = np.linspace(0, 2, 101)
resultado = solve_ivp(f, (X[0], X[-1]), [1, 0], method='RK45',
                      t_eval=X, rtol=1e-9, atol=1e-12)
if not resultado.success:
    raise RuntimeError(resultado.message)
Y = resultado.y.T
error = np.abs(g(X) - Y)
print("x =", X)
print("y =", Y)
print("Error absoluto maximo =", np.max(error))
print("Evaluaciones de f =", resultado.nfev)
xi = np.linspace(X[0], X[-1], 400)
plt.figure(figsize=(11, 7))
for j, color in enumerate(('b', 'g')):
    plt.plot(xi, g(xi)[:,j], color=color, label=f'S. Exacta: componente {j+1}')
    plt.plot(X, Y[:,j], '.', color=color, label=f'solve_ivp RK45: componente {j+1}')
plt.title('SciPy solve_ivp: sistema de EDO', fontsize=18)
plt.xlabel('x')
plt.ylabel('Solucion')
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()
