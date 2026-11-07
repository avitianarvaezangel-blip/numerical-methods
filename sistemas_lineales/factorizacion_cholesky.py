import numpy as np
import matplotlib.pyplot as plt


# Matriz real, simetrica y definida positiva
A = np.array([
    [4, 1, 1],
    [1, 3, 1],
    [1, 1, 2]
])

# Vector b; la solucion del ejemplo es [1, 2, 3]
b = np.array([9, 10, 9])


def Factorizacion_Cholesky(A, b):

    if np.iscomplexobj(A) or np.iscomplexobj(b):
        raise ValueError("A y b deben contener numeros reales.")

    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)

    if A.ndim != 2 or A.shape[0] == 0 or A.shape[0] != A.shape[1]:
        raise ValueError("A debe ser una matriz cuadrada no vacia.")
    if b.shape != (A.shape[0],):
        raise ValueError("b debe ser un vector compatible con A.")
    if not np.all(np.isfinite(A)) or not np.all(np.isfinite(b)):
        raise ValueError("A y b deben contener valores finitos.")

    escala = np.linalg.norm(A, ord=np.inf)
    if not np.allclose(A, A.T, rtol=1e-12, atol=1e-12 * escala):
        raise ValueError("Cholesky requiere una matriz simetrica.")

    # A = L @ L.T, con L triangular inferior y diagonal positiva
    f = A.shape[0]
    L = np.zeros((f, f))

    print("A =\n", A)

    for i in range(f):
        for j in range(i + 1):

            S = 0
            for k in range(j):
                S = S + L[i, k] * L[j, k]

            if i == j:
                valor = A[i, i] - S
                if valor <= 0:
                    raise ValueError("Cholesky requiere una matriz definida positiva.")
                L[i, j] = np.sqrt(valor)
            else:
                L[i, j] = (A[i, j] - S) / L[j, j]

        print("\nPaso", i + 1)
        print("L =\n", L)

    # Sustitucion hacia adelante: L @ y = b
    y = np.zeros(f)
    for i in range(f):
        S = 0
        for j in range(i):
            S = S + L[i, j] * y[j]
        y[i] = (b[i] - S) / L[i, i]

    # Sustitucion hacia atras: L.T @ x = y
    x = np.zeros(f)
    for i in range(f - 1, -1, -1):
        S = 0
        for j in range(i + 1, f):
            S = S + L[j, i] * x[j]
        x[i] = (y[i] - S) / L[i, i]

    return L, x


L, x = Factorizacion_Cholesky(A, b)

# Solucion de referencia con NumPy
x2 = np.linalg.solve(A, b)

print("\nL.T =\n", L.T)
print("L @ L.T =\n", L @ L.T)
print("x =", x)
print("x con NumPy =", x2)
print("Error de factorizacion =", np.linalg.norm(A - L @ L.T, ord=np.inf))
print("Norma del residuo =", np.linalg.norm(b - A @ x, ord=np.inf))

# Crear los valores de x e y
x3 = np.linspace(-1, 3, 50)
y = np.linspace(0, 4, 50)
X, Y = np.meshgrid(x3, y)

# Despejar z en cada ecuacion
Z1 = 9 - 4 * X - Y
Z2 = 10 - X - 3 * Y
Z3 = (9 - X - Y) / 2

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")

ax.plot_surface(X, Y, Z1, color="blue", alpha=0.4,
                label=r"$4x_1 + x_2 + x_3 = 9$")
ax.plot_surface(X, Y, Z2, color="red", alpha=0.4,
                label=r"$x_1 + 3x_2 + x_3 = 10$")
ax.plot_surface(X, Y, Z3, color="green", alpha=0.4,
                label=r"$x_1 + x_2 + 2x_3 = 9$")
ax.scatter(x[0], x[1], x[2], color="black", s=100,
           label=f"Solucion: {np.round(x, 4)}")

ax.set_xlabel(r"$x_1$")
ax.set_ylabel(r"$x_2$")
ax.set_zlabel(r"$x_3$")
ax.set_title("Factorizacion Cholesky", fontsize=20)
ax.legend(fontsize=11)
plt.tight_layout()
plt.show()
