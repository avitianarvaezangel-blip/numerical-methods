import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


# Escalas rapida (1/lambda) y lenta (cos x): ejemplo rigido.
lam = 1000.0


def g(x):
    return np.cos(x) - np.exp(-lam*x)


def f(x, y):
    return -lam*(y - np.cos(x)) - np.sin(x)


def Euler_Rigido(x0, y0, h, n, implicito=False):
    x = x0 + h*np.arange(n+1)
    y = np.zeros(n+1)
    y[0] = y0
    for i in range(n):
        if implicito:
            # Ecuacion implicita lineal resuelta algebraicamente.
            y[i+1] = (y[i] + h*(lam*np.cos(x[i+1]) - np.sin(x[i+1])))/(1+lam*h)
        else:
            y[i+1] = y[i] + h*f(x[i], y[i])
    return x, y


h, n = 0.01, 100
X, Y_exp = Euler_Rigido(0, 0, h, n)
_, Y_imp = Euler_Rigido(0, 0, h, n, implicito=True)
resultado = solve_ivp(f, (X[0], X[-1]), [0], method='Radau',
                      t_eval=X, rtol=1e-9, atol=1e-12)
if not resultado.success:
    raise RuntimeError(resultado.message)
Y_radau = resultado.y[0]
exacta = g(X)

print('Euler explicito: |1-lambda*h| =', abs(1-lam*h), '(inestable si es mayor que 1)')
for nombre, Y in (('Euler explicito', Y_exp), ('Euler implicito', Y_imp), ('Radau', Y_radau)):
    print(nombre, ': error absoluto maximo =', np.max(np.abs(exacta-Y)))
print('Radau: evaluaciones de f =', resultado.nfev)
print('Un paso estable no garantiza resolver con precision la capa transitoria inicial.')

xi = np.unique(np.r_[np.linspace(0, 0.02, 500), np.linspace(0.02, 1, 500)])
fig, ax = plt.subplots(2, 1, figsize=(11, 9))
ax[0].plot(xi, g(xi), 'b', label='S. Exacta')
ax[0].plot(X, Y_imp, 'g.--', label='Euler implicito')
ax[0].plot(X, Y_radau, 'r.', label='Radau adaptativo')
ax[0].set_ylabel('y(x)')
ax[0].set_title('EDO rigida: estabilidad y precision', fontsize=18)
for nombre, Y in (('Euler explicito', Y_exp), ('Euler implicito', Y_imp), ('Radau', Y_radau)):
    ax[1].semilogy(X[1:], np.abs(exacta-Y)[1:], label=nombre)
ax[1].set_xlabel('x')
ax[1].set_ylabel('Error absoluto')
for eje in ax:
    eje.grid()
    eje.legend()
fig.tight_layout()
plt.show()
