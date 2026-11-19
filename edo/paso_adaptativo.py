import numpy as np
import matplotlib.pyplot as plt


def g(x):
    return np.cbrt(x**3 - 3*x + 8)


def f(x, y):
    return (x**2 - 1) / y**2


def Paso_RK4(f, x, y, h):
    k1 = f(x, y)
    k2 = f(x + h/2, y + h*k1/2)
    k3 = f(x + h/2, y + h*k2/2)
    k4 = f(x + h, y + h*k3)
    return y + h*(k1 + 2*k2 + 2*k3 + k4)/6


def RK4_Adaptativo(f, x0, y0, xn, h0, rtol=1e-6, atol=1e-9, ItMax=100000):
    if not all(np.isfinite(v) for v in (x0, y0, xn, h0, rtol, atol)):
        raise ValueError('Los datos y tolerancias deben ser finitos.')
    if xn <= x0 or h0 <= 0 or rtol < 0 or atol <= 0:
        raise ValueError('Se requiere xn>x0, h0>0, rtol>=0 y atol>0.')
    if not isinstance(ItMax, (int, np.integer)) or ItMax < 1:
        raise ValueError('ItMax debe ser un entero positivo.')

    x, y, h = float(x0), float(y0), float(h0)
    X, Y, historial = [x], [y], []
    rechazados = 0
    for _ in range(ItMax):
        if x == xn:
            return np.array(X), np.array(Y), np.array(historial), rechazados
        h = min(h, xn - x)
        if x + h == x:
            raise FloatingPointError('El paso es demasiado pequeno para avanzar.')

        y_un_paso = Paso_RK4(f, x, y, h)
        y_medio = Paso_RK4(f, x, y, h/2)
        y_dos_pasos = Paso_RK4(f, x+h/2, y_medio, h/2)

        # Error estimado de los dos medios pasos para un metodo de orden 4.
        error = abs(y_dos_pasos - y_un_paso)/15
        escala = atol + rtol*max(abs(y), abs(y_dos_pasos))
        razon = error/escala
        if not np.isfinite(razon) or not np.isfinite(y_dos_pasos):
            raise FloatingPointError('La integracion produjo valores no finitos.')

        if razon <= 1:
            # Conservar la solucion RK4 de dos medios pasos (sin extrapolar).
            x = xn if h == xn - x else x + h
            y = y_dos_pasos
            X.append(x)
            Y.append(y)
            historial.append([x, h, error, escala])
        else:
            rechazados += 1

        factor = 5.0 if razon == 0 else np.clip(0.9*razon**(-1/5), 0.2, 5.0)
        h = h*factor

    if X[-1] == xn:
        return np.array(X), np.array(Y), np.array(historial), rechazados
    raise RuntimeError('Se alcanzo ItMax antes del extremo final.')


X, Y, historial, rechazados = RK4_Adaptativo(f, 0, 2, 2, 0.4)
error = np.abs(g(X) - Y)
print('x =', X)
print('y =', Y)
print('Error absoluto maximo =', np.max(error))
print('Pasos aceptados =', len(X)-1, '; rechazados =', rechazados)
print('Columnas del historial: x aceptado, h, error local estimado, tolerancia local')
print(historial)
print('La tolerancia controla una estimacion local; no es una cota del error global.')

xi = np.linspace(X[0], X[-1], 400)
fig, ax = plt.subplots(2, 1, figsize=(11, 8))
ax[0].plot(xi, g(xi), 'b', label='S. Exacta')
ax[0].plot(X, Y, 'ro', label='Valores aceptados de RK4 adaptativo')
ax[0].set_ylabel('y(x)')
ax[0].set_title('Paso segun la precision deseada', fontsize=18)
ax[0].legend()
ax[1].stairs(historial[:,1], X)
ax[1].set_xlabel('x')
ax[1].set_ylabel('Paso aceptado h')
for eje in ax:
    eje.grid()
fig.tight_layout()
plt.show()
