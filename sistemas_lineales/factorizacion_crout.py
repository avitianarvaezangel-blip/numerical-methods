import numpy as np
import matplotlib.pyplot as plt


# Matriz de coeficientes
A = np.array([
    [ 2,  1, -1],
    [-1,  3,  2],
    [ 3, -1,  1]
])

# Vector b
b = np.array([1, 12, 4])


def Factorizacion_Crout(A, b):

    # Esta implementacion usa matrices reales y no realiza pivoteo.
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

    # En Crout, la diagonal de U es unitaria: A = L @ U.
    f = A.shape[0]
    L = np.zeros((f, f))
    U = np.eye(f)
    tol_pivote = np.finfo(float).eps * f * np.linalg.norm(A, ord=np.inf)

    print("A =\n", A)

    for j in range(f):

        # Calcular la columna j de L
        for i in range(j, f):
            S = 0
            for k in range(j):
                S = S + L[i, k] * U[k, j]
            L[i, j] = A[i, j] - S

        if abs(L[j, j]) <= tol_pivote:
            raise ValueError(
                "Pivote nulo o demasiado pequeno. "
                "Crout sin pivoteo no puede continuar; puede requerirse "
                "una permutacion de filas."
            )

        # Calcular la fila j de U
        for i in range(j + 1, f):
            S = 0
            for k in range(j):
                S = S + L[j, k] * U[k, i]
            U[j, i] = (A[j, i] - S) / L[j, j]

        print("\nPaso", j + 1)
        print("L =\n", L)
        print("U =\n", U)

    # Sustitucion hacia adelante: L @ y = b
    y = np.zeros(f)
    for i in range(f):
        S = 0
        for j in range(i):
            S = S + L[i, j] * y[j]
        y[i] = (b[i] - S) / L[i, i]

    # Sustitucion hacia atras: U @ x = y, con U[i,i] = 1
    x = np.zeros(f)
    for i in range(f - 1, -1, -1):
        S = 0
        for j in range(i + 1, f):
            S = S + U[i, j] * x[j]
        x[i] = y[i] - S

    return L, U, x


L, U, x = Factorizacion_Crout(A, b)

# Solucion de referencia con NumPy
x2 = np.linalg.solve(A, b)

print("\nL @ U =\n", L @ U)
print("x =", x)
print("x con NumPy =", x2)
print("Error de factorizacion =", np.linalg.norm(A - L @ U, ord=np.inf))
print("Norma del residuo =", np.linalg.norm(b - A @ x, ord=np.inf))

# Crear los valores de x e y
x3 = np.linspace(-2, 5, 50)
y = np.linspace(-2, 6, 50)
X, Y = np.meshgrid(x3, y)

# Despejar z en cada ecuacion
Z1 = 2 * X + Y - 1
Z2 = (12 + X - 3 * Y) / 2
Z3 = 4 - 3 * X + Y

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")

ax.plot_surface(X, Y, Z1, color="blue", alpha=0.4,
                label=r"$2x_1 + x_2 - x_3 = 1$")
ax.plot_surface(X, Y, Z2, color="red", alpha=0.4,
                label=r"$-x_1 + 3x_2 + 2x_3 = 12$")
ax.plot_surface(X, Y, Z3, color="green", alpha=0.4,
                label=r"$3x_1 - x_2 + x_3 = 4$")
ax.scatter(x[0], x[1], x[2], color="black", s=100,
           label=f"Solucion: {np.round(x, 4)}")

ax.set_xlabel(r"$x_1$")
ax.set_ylabel(r"$x_2$")
ax.set_zlabel(r"$x_3$")
ax.set_title("Factorizacion Crout", fontsize=20)
ax.legend(fontsize=11)
plt.tight_layout()
plt.show()
