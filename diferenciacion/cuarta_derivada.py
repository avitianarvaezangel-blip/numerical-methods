import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Variable, función y 4ta derivada simbólicas
x = sp.Symbol('x')

f = sp.exp(x) * sp.sin(x)

df = sp.diff(f, x, 4)

# Función y 4ta derivada numéricas
fn = sp.lambdify(x, f, 'numpy')

dfn = sp.lambdify(x, df, 'numpy')

# Intervalo de valores
xn = np.linspace(0, 2, 100)

# Paso uniforme (h > 0)
# La función debe estar definida también en los puntos desplazados.
h = 0.1

# Diferencias finitas para la 4ta derivada


# Hacia adelante: 5 puntos, error de truncamiento O(h)
def DF_Adelante_4ta_5p(f, xn, h):
    return (
        f(xn) - 4*f(xn + h) + 6*f(xn + 2*h)
        - 4*f(xn + 3*h) + f(xn + 4*h)
    ) / h**4


# Hacia adelante: 6 puntos, error de truncamiento O(h^2)
def DF_Adelante_4ta_6p(f, xn, h):
    return (
        3*f(xn) - 14*f(xn + h) + 26*f(xn + 2*h)
        - 24*f(xn + 3*h) + 11*f(xn + 4*h)
        - 2*f(xn + 5*h)
    ) / h**4


# Hacia atrás: 5 puntos, error de truncamiento O(h)
def DF_Atras_4ta_5p(f, xn, h):
    return (
        f(xn - 4*h) - 4*f(xn - 3*h)
        + 6*f(xn - 2*h) - 4*f(xn - h) + f(xn)
    ) / h**4


# Hacia atrás: 6 puntos, error de truncamiento O(h^2)
def DF_Atras_4ta_6p(f, xn, h):
    return (
        -2*f(xn - 5*h) + 11*f(xn - 4*h)
        - 24*f(xn - 3*h) + 26*f(xn - 2*h)
        - 14*f(xn - h) + 3*f(xn)
    ) / h**4


# Centrada: 5 puntos, error de truncamiento O(h^2)
def DF_Centrada_4ta_5p(f, xn, h):
    return (
        f(xn - 2*h) - 4*f(xn - h) + 6*f(xn)
        - 4*f(xn + h) + f(xn + 2*h)
    ) / h**4


# Centrada: 7 puntos, error de truncamiento O(h^4)
# Corrección de la tabla: el coeficiente de f(x_i + h) es -39,
# igual que el de f(x_i - h); con +39 no se anula una constante.
def DF_Centrada_4ta_7p(f, xn, h):
    return (
        -f(xn - 3*h) + 12*f(xn - 2*h)
        - 39*f(xn - h) + 56*f(xn)
        - 39*f(xn + h) + 12*f(xn + 2*h)
        - f(xn + 3*h)
    ) / (6*h**4)


# Diferencias finitas evaluadas
DFAd5 = DF_Adelante_4ta_5p(fn, xn, h)
DFAd6 = DF_Adelante_4ta_6p(fn, xn, h)

DFAt5 = DF_Atras_4ta_5p(fn, xn, h)
DFAt6 = DF_Atras_4ta_6p(fn, xn, h)

DFC5 = DF_Centrada_4ta_5p(fn, xn, h)
DFC7 = DF_Centrada_4ta_7p(fn, xn, h)

# Derivada analítica evaluada
df_exacta = dfn(xn)

print("f(x) =", f)
print("f''''(x) =", df)
print("\nPaso h =", h)

# Error absoluto máximo en los puntos de la gráfica
aproximaciones = [
    ("Adelante, 5 puntos, O(h)", DFAd5),
    ("Adelante, 6 puntos, O(h^2)", DFAd6),
    ("Atrás, 5 puntos, O(h)", DFAt5),
    ("Atrás, 6 puntos, O(h^2)", DFAt6),
    ("Centrada, 5 puntos, O(h^2)", DFC5),
    ("Centrada, 7 puntos, O(h^4)", DFC7),
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
         label=r"$f^{(4)}(x)=-4e^x\sin(x)$")

plt.plot(xn, DFAd5, '--', color='red',
         label=(r"Adelante, 5 puntos: $f^{(4)}(x_i)\approx"
                r"\frac{f_i-4f_{i+1}+6f_{i+2}-4f_{i+3}+f_{i+4}}{h^4}"
                r"\quad O(h)$"))

plt.plot(xn, DFAd6, '--', color='darkorange',
         label=(r"Adelante, 6 puntos: $f^{(4)}(x_i)\approx"
                r"\frac{3f_i-14f_{i+1}+26f_{i+2}-24f_{i+3}+11f_{i+4}-2f_{i+5}}{h^4}"
                r"\quad O(h^2)$"))

plt.plot(xn, DFAt5, '--', color='green',
         label=(r"Atrás, 5 puntos: $f^{(4)}(x_i)\approx"
                r"\frac{f_{i-4}-4f_{i-3}+6f_{i-2}-4f_{i-1}+f_i}{h^4}"
                r"\quad O(h)$"))

plt.plot(xn, DFAt6, '--', color='teal',
         label=(r"Atrás, 6 puntos: $f^{(4)}(x_i)\approx"
                r"\frac{-2f_{i-5}+11f_{i-4}-24f_{i-3}+26f_{i-2}-14f_{i-1}+3f_i}{h^4}"
                r"\quad O(h^2)$"))

plt.plot(xn, DFC5, '--', color='purple',
         label=(r"Centrada, 5 puntos: $f^{(4)}(x_i)\approx"
                r"\frac{f_{i-2}-4f_{i-1}+6f_i-4f_{i+1}+f_{i+2}}{h^4}"
                r"\quad O(h^2)$"))

plt.plot(xn, DFC7, '-.', color='deeppink',
         label=(r"Centrada, 7 puntos: $f^{(4)}(x_i)\approx"
                r"\frac{-f_{i-3}+12f_{i-2}-39f_{i-1}+56f_i-39f_{i+1}+12f_{i+2}-f_{i+3}}{6h^4}"
                r"\quad O(h^4)$"))

# Etiquetas
plt.xlabel('x')
plt.ylabel(r"$f(x)$ y $f^{(4)}(x)$")
plt.title('Diferenciación numérica (4ta derivada)', fontsize=20)
plt.text(0.02, 0.05, f'h = {h:g}', transform=plt.gca().transAxes)

plt.legend(fontsize=9, ncol=2, loc='upper center',
           bbox_to_anchor=(0.5, -0.16))
plt.grid(alpha=0.3)

# Notación compacta para las seis fórmulas de la leyenda
plt.figtext(0.5, 0.025, r'$f_{i+k}=f(x_i+kh)$',
            ha='center', fontsize=11)
plt.subplots_adjust(bottom=0.36)

plt.show()
