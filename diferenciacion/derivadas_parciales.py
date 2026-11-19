import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Variable, función y derivadas simbólicas
x, y = sp.symbols('x y')

f = sp.sin(x) + sp.sin(y)

pdx = sp.diff(f, x)
pdy = sp.diff(f, y)

print("∂f/∂x =", pdx)
print("∂f/∂y =", pdy)

# Función y derivadas numéricas: todas dependen de x e y
fn = sp.lambdify((x, y), f, 'numpy')
pfxn = sp.lambdify((x, y), pdx, 'numpy')
pfyn = sp.lambdify((x, y), pdy, 'numpy')

# Intervalos y malla numérica
xn = np.linspace(-5, 5, 100)
yn = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(xn, yn)

# Pasos de diferenciación
hx = 0.1
hy = 0.1


# Diferencias finitas respecto a x
def DF_Adelante_x(f, X, Y, hx):
    return (f(X + hx, Y) - f(X, Y)) / hx


def DF_Atras_x(f, X, Y, hx):
    return (f(X, Y) - f(X - hx, Y)) / hx


def DF_Centrada_x(f, X, Y, hx):
    return (f(X + hx, Y) - f(X - hx, Y)) / (2*hx)


# Diferencias finitas respecto a y
def DF_Adelante_y(f, X, Y, hy):
    return (f(X, Y + hy) - f(X, Y)) / hy


def DF_Atras_y(f, X, Y, hy):
    return (f(X, Y) - f(X, Y - hy)) / hy


def DF_Centrada_y(f, X, Y, hy):
    return (f(X, Y + hy) - f(X, Y - hy)) / (2*hy)


# Derivadas exactas evaluadas
Fx = pfxn(X, Y)
Fy = pfyn(X, Y)

# Aproximaciones evaluadas sobre toda la malla
DFAd_x = DF_Adelante_x(fn, X, Y, hx)
DFAt_x = DF_Atras_x(fn, X, Y, hx)
DFC_x = DF_Centrada_x(fn, X, Y, hx)

DFAd_y = DF_Adelante_y(fn, X, Y, hy)
DFAt_y = DF_Atras_y(fn, X, Y, hy)
DFC_y = DF_Centrada_y(fn, X, Y, hy)

# Gráficas: primera fila ∂f/∂x, segunda fila ∂f/∂y
superficies = [
    (Fx,    r'$\frac{\partial f}{\partial x}  = \cos{x}$'),
    (DFAd_x, r'$\frac{\partial f(x_i, y_i)}{\partial x} \approx \frac{f(x_i + h_x, y_i) - f(x_i, y_i)}{h_x}$'),
    (DFAt_x, r'$\frac{\partial f(x_i, y_i)}{\partial x} \approx \frac{f(x_i, y_i) - f(x_i - h, y_i)}{h_x}$'),
    (DFC_x,  r'$\frac{\partial f(x_i, y_i)}{\partial x} \approx \frac{f(x_i + h, y_i) - f(x_i - h, y_i)}{2 h_x}$'),
    (Fy,    r'$\frac{\partial f}{\partial y}  = \cos{y}$'),
    (DFAd_y, r'$\frac{\partial f(x_i, y_i)}{\partial y} \approx \frac{f(x_i, y_i + h_y) - f(x_i, y_i)}{h_y}$'),
    (DFAt_y, r'$\frac{\partial f(x_i, y_i)}{\partial y} \approx \frac{f(x_i, y_i) - f(x_i, y_i - h)}{h_y}$'),
    (DFC_y,  r'$\frac{\partial f(x_i, y_i)}{\partial y} \approx \frac{f(x_i, y_i + h) - f(x_i, y_i - h)}{2 h_y}$')
]

fig = plt.figure(figsize=(20, 10))

# Escala común por fila para comparar los métodos
limites = [
    (min(Z.min() for Z, _ in superficies[:4]),
     max(Z.max() for Z, _ in superficies[:4])),
    (min(Z.min() for Z, _ in superficies[4:]),
     max(Z.max() for Z, _ in superficies[4:]))
]

for i, (Z, titulo) in enumerate(superficies):
    ax = fig.add_subplot(2, 4, i + 1, projection='3d')
    zmin, zmax = limites[i // 4]

    ax.plot_surface(
        X, Y, Z,
        cmap='jet',
        vmin=zmin,
        vmax=zmax,
        linewidth=0,
        antialiased=True
    )

    ax.set_title(titulo)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('Derivada')
    ax.set_zlim(zmin, zmax)

plt.show()
