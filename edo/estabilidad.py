import numpy as np
import matplotlib.pyplot as plt


# Ecuacion prueba y' = -lambda*y, y(0)=1.
lam = 10.0


def g(x):
    return np.exp(-lam*x)


def Euler_Lineal(lam, x0, y0, h, n, implicito=False):
    if not np.isfinite(lam) or lam <= 0 or not np.isfinite(h) or h <= 0:
        raise ValueError('lambda y h deben ser positivos y finitos.')
    if not isinstance(n, (int, np.integer)) or n < 0:
        raise ValueError('n debe ser un entero no negativo.')
    x = x0 + h*np.arange(n+1)
    y = np.zeros(n+1)
    y[0] = y0
    for i in range(n):
        y[i+1] = y[i]/(1+lam*h) if implicito else y[i]*(1-lam*h)
    return x, y


# R(z) es el factor de amplificacion, z = -lambda*h.
# Para reproducir amortiguacion se necesita |R(z)| < 1.
z = np.linspace(-4, 0, 500)
R_euler = 1 + z
R_heun = 1 + z + z**2/2
R_rk4 = 1 + z + z**2/2 + z**3/6 + z**4/24
R_implicito = 1/(1-z)

fig, ax = plt.subplots(2, 1, figsize=(11, 9))
for R, nombre in ((R_euler, 'Euler explicito'), (R_heun, 'Heun / punto medio'),
                   (R_rk4, 'RK4'), (R_implicito, 'Euler implicito')):
    ax[0].plot(z, np.abs(R), label=nombre)
ax[0].axhline(1, color='black', linestyle='--', label='Frontera |R| = 1')
ax[0].set_ylim(0, 3)
ax[0].set_xlabel(r'$z=-\lambda h$')
ax[0].set_ylabel('|R(z)|')
ax[0].set_title('Estabilidad sobre el eje real negativo', fontsize=18)

xi = np.linspace(0, 2, 400)
ax[1].plot(xi, g(xi), 'b', label='S. Exacta')
for h in (0.05, 0.25):
    X, Y = Euler_Lineal(lam, 0, 1, h, int(round(2/h)))
    print('Euler explicito: h =', h, ', |R| =', abs(1-lam*h),
          ', amortiguacion =', abs(1-lam*h) < 1)
    ax[1].plot(X, Y, 'o--', markersize=3, label=f'Euler explicito h={h}')
X, Y = Euler_Lineal(lam, 0, 1, 0.25, 8, implicito=True)
ax[1].plot(X, Y, 'go-', markersize=3, label='Euler implicito h=0.25')
ax[1].set_xlabel('x')
ax[1].set_ylabel('y(x)')
for eje in ax:
    eje.grid()
    eje.legend(fontsize=10)
fig.tight_layout()
plt.show()
