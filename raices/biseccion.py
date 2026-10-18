import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from IPython.display import HTML

# Funcion f(x)

def f(x):
  return -0.5*x**2 + 2.5*x + 4.5

# Metodo de biseccion

def Biseccion(f, xl, xu, tol = 1e-10,ItMax = 100):
  #Historial de Intervalos
    His_Int = []
    if f(xl)*f(xu) > 0:
        print("la raiz no esta en el intervalo")
        return None, His_Int

    for i in range(ItMax):
        xr = (xl + xu)/2
        fxr = f(xr)
        His_Int.append((xl, xu, xr))

        if abs(fxr) < tol or abs(xu - xl)/2 < tol:
           return xr, i + 1, His_Int

        if f(xl) * fxr < 0:
            xu = xr
        else:

            xl = xr

    return xr, ItMax, His_Int

# Intervalo inicial
xl = 5
xu = 10

# Raíz, Iteraciones e historial de intervalos
R, It, Int = Biseccion(f, xl, xu)

# tabla de resultados

tabla = pd.DataFrame(
    [
        [i+1, xL, xU, xR, f(xR)]
        for i, (xL, xU, xR) in enumerate(Int)
    ],
    columns=["Iteración", "xl", "xu", "xr", "f(xr)"]
)

print(tabla)

# Gráfica

xi = np.linspace(xl - 0.2, xu + 0.2, 1000)
y = f(xi)

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(xi, y, linewidth=2, color='blue',
        label=r"$f(x)=-0.5x^2 + 2.5x + 4.5$")

ax.axhline(0, color='black',
           linestyle='-',lw=1.5)


ax.set_xlabel(r"$x$",fontsize=20)
ax.set_ylabel(r"$f(x)$",fontsize=20)
ax.set_title("Método de Bisección",fontsize=20)

ax.grid()

# Objetos animados

Punto, = ax.plot([], [], 'ro',label="$x_r$",
                    markersize=10)

shade = None

txt = ax.text(
    0.02,
    0.98,
    "",
    transform=ax.transAxes,
    verticalalignment='top',
    fontsize=11,
    bbox=dict(facecolor='white',
              alpha=0.5)
)

Linea_xl = ax.axvline(
    xl,
    color='green',
    linewidth=2,
    linestyle='--',
    label=r"$x_l$"
)

Linea_xu = ax.axvline(
    xu,
    color='green',
    linewidth=2,
    linestyle='--',
    label=r"$x_u$"
)

Linea_R = ax.axvline(
    xl,
    color='red',
    linewidth=2,
    linestyle='--',
    label=r"$x_r$"
)

# Inicialización

def init():
    Punto.set_data([], [])
    txt.set_text("")
    return Punto, txt, Linea_xl, Linea_xu, Linea_R

# Actualización de cada frame

def update(frame):

    global shade

    xL, xU, xR = Int[frame]

    if shade is not None:
        shade.remove()

    shade = ax.axvspan(
        xL,
        xU,
        color='green',
        alpha=0.6,
        label='Intervalo'
    )

    Linea_xl.set_xdata([xL, xL])
    Linea_xu.set_xdata([xU, xU])
    Linea_R.set_xdata([xR, xR])
    ax.legend()

    Punto.set_data([xR], [0])

    txt.set_text(
        f"Iteración = {frame+1}\n"
        f"$x_l$ = {xL:.10f}\n"
        f"$x_u$ = {xU:.10f}\n"
        f"$x_r$ = {xR:.10f}\n"
        f"$f(x_r)$ = {f(xR):.3e}"
    )

    return Punto, txt, Linea_xl, Linea_xu, Linea_R

# Animación

ani = anim.FuncAnimation(
    fig,
    update,
    frames=len(Int),
    init_func=init,
    interval=800,
    repeat=False,
    blit=True
)

plt.close()

HTML(ani.to_jshtml())
