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


def Factorizacion_QR(A, b):

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

    # Reflexiones de Householder: A = Q @ R y Q.T @ Q = I
    f = A.shape[0]
    Q = np.eye(f)
    R = A.copy()
    tol_pivote = np.finfo(float).eps * f * np.linalg.norm(A, ord=np.inf)

    print("A =\n", A)

    for k in range(f):

        # Vector de Householder para anular las entradas bajo R[k,k]
        v = R[k:, k].copy()
        norma = np.linalg.norm(v)

        if norma <= tol_pivote:
            raise ValueError("A es singular o numericamente de rango deficiente.")

        # Elegir el signo evita restar dos numeros casi iguales.
        v[0] = v[0] + np.copysign(norma, v[0])
        v = v / np.linalg.norm(v)

        # H = I - 2*v*v.T, aplicada sin construir la matriz completa
        R[k:, k:] = R[k:, k:] - 2 * np.outer(v, v @ R[k:, k:])
        Q[:, k:] = Q[:, k:] - 2 * np.outer(Q[:, k:] @ v, v)
        R[k + 1:, k] = 0.0

        print("\nPaso", k + 1)
        print("Q =\n", Q)
        print("R =\n", R)

    # Q @ R @ x = b; como Q es ortogonal, R @ x = Q.T @ b
    y = Q.T @ b

    # Sustitucion hacia atras
    x = np.zeros(f)
    for i in range(f - 1, -1, -1):
        S = 0
        for j in range(i + 1, f):
            S = S + R[i, j] * x[j]
        x[i] = (y[i] - S) / R[i, i]

    return Q, R, x


Q, R, x = Factorizacion_QR(A, b)

# Solucion de referencia con NumPy
x2 = np.linalg.solve(A, b)

print("\nQ @ R =\n", Q @ R)
print("Q.T @ Q =\n", Q.T @ Q)
print("x =", x)
print("x con NumPy =", x2)
print("Error de factorizacion =", np.linalg.norm(A - Q @ R, ord=np.inf))
print("Error de ortogonalidad =", np.linalg.norm(Q.T @ Q - np.eye(len(b)), ord=np.inf))
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
ax.set_title("Factorizacion QR", fontsize=20)
ax.legend(fontsize=11)
plt.tight_layout()
plt.show()
