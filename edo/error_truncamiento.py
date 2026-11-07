import numpy as np
import matplotlib.pyplot as plt


def g(x):
    return np.cbrt(x**3 - 3*x + 8)


def f(x, y):
    return (x**2 - 1) / y**2


def Paso_Euler(f, x, y, h):
    return y + h*f(x, y)


def Paso_Heun(f, x, y, h):
    k1 = f(x, y)
    k2 = f(x + h, y + h*k1)
    return y + h*(k1 + k2)/2


# Error local de UN paso, empezando desde la condicion exacta.
# Se usa la diferencia de valores, sin dividir entre h:
# Euler: O(h**2); RK2 de Heun: O(h**3). No son los ordenes globales.
x0, y0 = 0, 2
pasos = np.array([0.4, 0.2, 0.1, 0.05, 0.025, 0.0125])
error_euler = np.array([abs(g(x0+h) - Paso_Euler(f, x0, y0, h)) for h in pasos])
error_heun = np.array([abs(g(x0+h) - Paso_Heun(f, x0, y0, h)) for h in pasos])
orden_euler = np.r_[np.nan, np.log2(error_euler[:-1]/error_euler[1:])]
orden_heun = np.r_[np.nan, np.log2(error_heun[:-1]/error_heun[1:])]

print('Columnas: h, error local Euler, orden observado, error local Heun, orden observado')
print(np.column_stack((pasos, error_euler, orden_euler, error_heun, orden_heun)))

plt.figure(figsize=(10, 6))
plt.loglog(pasos, error_euler, 'bo-', label='Error local de un paso: Euler')
plt.loglog(pasos, error_heun, 'ro-', label='Error local de un paso: Heun (RK2)')
plt.loglog(pasos, error_euler[-1]*(pasos/pasos[-1])**2, 'b--', label=r'Referencia $h^2$')
plt.loglog(pasos, error_heun[-1]*(pasos/pasos[-1])**3, 'r--', label=r'Referencia $h^3$')
plt.title('Error local de truncamiento: Euler y RK2', fontsize=18)
plt.xlabel('Paso h')
plt.ylabel('Error absoluto local sin dividir entre h')
plt.grid(True, which='both')
plt.legend()
plt.tight_layout()
plt.show()
