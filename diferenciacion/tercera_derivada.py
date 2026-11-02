import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Variable, función y 3ra derivada simbólicas
x = sp.Symbol('x')

f = sp.exp(x) * sp.sin(x)

df = sp.diff(f, x, 3)

# Función y 3ra derivada numéricas
fn = sp.lambdify(x, f, 'numpy')

dfn = sp.lambdify(x, df, 'numpy')

# Intervalo de valores
xn = np.linspace(0, 2, 100)

# Paso uniforme (h > 0)
# La función debe estar definida también en los puntos desplazados.
h = 0.1

# Diferencias finitas para la 3ra derivada


# Hacia adelante: 4 puntos, error de truncamiento O(h)
def DF_Adelante_3ra_4p(f, xn, h):
    return (
        -f(xn) + 3*f(xn + h)
        - 3*f(xn + 2*h) + f(xn + 3*h)
    ) / h**3


# Hacia adelante: 5 puntos, error de truncamiento O(h^2)
def DF_Adelante_3ra_5p(f, xn, h):
    return (
        -5*f(xn) + 18*f(xn + h)
        - 24*f(xn + 2*h) + 14*f(xn + 3*h)
        - 3*f(xn + 4*h)
    ) / (2*h**3)


# Hacia atrás: 4 puntos, error de truncamiento O(h)
def DF_Atras_3ra_4p(f, xn, h):
    return (
        -f(xn - 3*h) + 3*f(xn - 2*h)
        - 3*f(xn - h) + f(xn)
    ) / h**3


# Hacia atrás: 5 puntos, error de truncamiento O(h^2)
def DF_Atras_3ra_5p(f, xn, h):
    return (
        3*f(xn - 4*h) - 14*f(xn - 3*h)
        + 24*f(xn - 2*h) - 18*f(xn - h)
        + 5*f(xn)
    ) / (2*h**3)


# Centrada: 4 puntos, error de truncamiento O(h^2)
def DF_Centrada_3ra_4p(f, xn, h):
    return (
        -f(xn - 2*h) + 2*f(xn - h)
        - 2*f(xn + h) + f(xn + 2*h)
    ) / (2*h**3)


# Centrada: 6 puntos, error de truncamiento O(h^4)
def DF_Centrada_3ra_6p(f, xn, h):
    return (
        f(xn - 3*h) - 8*f(xn - 2*h)
        + 13*f(xn - h) - 13*f(xn + h)
        + 8*f(xn + 2*h) - f(xn + 3*h)
    ) / (8*h**3)


# Diferencias finitas evaluadas
DFAd4 = DF_Adelante_3ra_4p(fn, xn, h)
DFAd5 = DF_Adelante_3ra_5p(fn, xn, h)

DFAt4 = DF_Atras_3ra_4p(fn, xn, h)
DFAt5 = DF_Atras_3ra_5p(fn, xn, h)

DFC4 = DF_Centrada_3ra_4p(fn, xn, h)
DFC6 = DF_Centrada_3ra_6p(fn, xn, h)

# Derivada analítica evaluada
df_exacta = dfn(xn)

print("f(x) =", f)
print("f'''(x) =", df)
print("\nPaso h =", h)

# Error absoluto máximo en los puntos de la gráfica
aproximaciones = [
    ("Adelante, 4 puntos, O(h)", DFAd4),
    ("Adelante, 5 puntos, O(h^2)", DFAd5),
    ("Atrás, 4 puntos, O(h)", DFAt4),
    ("Atrás, 5 puntos, O(h^2)", DFAt5),
    ("Centrada, 4 puntos, O(h^2)", DFC4),
    ("Centrada, 6 puntos, O(h^4)", DFC6),
]

print(f"\n{'Método':<32}{'Error absoluto máximo':>24}")

for nombre, aproximacion in aproximaciones:
    error = np.max(np.abs(df_exacta - aproximacion))
    print(f"{nombre:<32}{error:>24.6e}")

# Gráficas
plt.figure(figsize=(16, 9))

plt.plot(xn, fn(xn), color='blue', lw=2,
         label=r'$f(x)=e^x\sin(x)$')

plt.plot(xn, df_exacta, color='black', lw=2.5,
         label=r"$f'''(x)=2e^x[\cos(x)-\sin(x)]$")

plt.plot(xn, DFAd4, '--', color='red',
         label=(r"Adelante, 4 puntos: $f'''(x_i)\approx"
                r"\frac{-f_i+3f_{i+1}-3f_{i+2}+f_{i+3}}{h^3}"
                r"\quad O(h)$"))

plt.plot(xn, DFAd5, '--', color='darkorange',
         label=(r"Adelante, 5 puntos: $f'''(x_i)\approx"
                r"\frac{-5f_i+18f_{i+1}-24f_{i+2}+14f_{i+3}-3f_{i+4}}{2h^3}"
                r"\quad O(h^2)$"))

plt.plot(xn, DFAt4, '--', color='green',
         label=(r"Atrás, 4 puntos: $f'''(x_i)\approx"
                r"\frac{-f_{i-3}+3f_{i-2}-3f_{i-1}+f_i}{h^3}"
                r"\quad O(h)$"))

plt.plot(xn, DFAt5, '--', color='teal',
         label=(r"Atrás, 5 puntos: $f'''(x_i)\approx"
                r"\frac{3f_{i-4}-14f_{i-3}+24f_{i-2}-18f_{i-1}+5f_i}{2h^3}"
                r"\quad O(h^2)$"))

plt.plot(xn, DFC4, '--', color='purple',
         label=(r"Centrada, 4 puntos: $f'''(x_i)\approx"
                r"\frac{-f_{i-2}+2f_{i-1}-2f_{i+1}+f_{i+2}}{2h^3}"
                r"\quad O(h^2)$"))

plt.plot(xn, DFC6, '-.', color='deeppink',
         label=(r"Centrada, 6 puntos: $f'''(x_i)\approx"
                r"\frac{f_{i-3}-8f_{i-2}+13f_{i-1}-13f_{i+1}+8f_{i+2}-f_{i+3}}{8h^3}"
                r"\quad O(h^4)$"))

# Etiquetas
plt.xlabel('x')
plt.ylabel(r"$f(x)$ y $f'''(x)$")
plt.title('Diferenciación numérica (3ra derivada)', fontsize=20)
plt.text(0.02, 0.05, f'h = {h:g}', transform=plt.gca().transAxes)

plt.legend(fontsize=9, ncol=2, loc='upper center',
           bbox_to_anchor=(0.5, -0.16))
plt.grid(alpha=0.3)

# Notación compacta para las seis fórmulas de la leyenda
plt.figtext(0.5, 0.025, r'$f_{i+k}=f(x_i+kh)$',
            ha='center', fontsize=11)
plt.subplots_adjust(bottom=0.36)

plt.show()
