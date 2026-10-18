import numpy as np
import pandas as pd


A = np.array([
    [10, -1,  2,  0],
    [-1, 11, -1,  3],
    [ 2, -1, 10, -1],
    [ 0,  3, -1,  8]
])

b = np.array([6, 25, -11, 15])

x0 = np.zeros(b.shape[0])

tol = 0.01

ItMax = 100


# Solución exacta

x_exacta = np.linalg.solve(A, b)


def jacobi(A, b, x0, tol, ItMax, x_exacta):

    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    x0 = np.array(x0, dtype=float)

    # Número de filas
    f = A.shape[0]

    # Contador de filas 
    k = 0

    # Criterio de diagonal dominante

    for i in range(f):

        D = abs(A[i, i])

        S = 0

        for j in range(f):

            if j != i:
                S = S + abs(A[i, j])

        print("R_",i+1)
        print("  |a",i+1,i+1,"| = ",D)
        print("Suma de términos restantes = ",S)

        if D > S:
            k = k + 1

    #  Verificar convergencia

    if k == f:

        print("\nLa matriz es estrictamente diagonal dominante.")
        print("El método de Jacobi converge.")

    else:

        print("\nLa matriz NO es estrictamente diagonal dominante.")
        print("No se garantiza la convergencia del método de Jacobi.")

        return None


    #  DataFrame con pandas


    datos = []

    # Iteraciones de Jacobi


    for it in range(1, ItMax + 1):

        x = np.zeros(f)

        # Calcular nueva iteración


        for i in range(f):

            S = 0

            for j in range(f):

                if j != i:

                    S = S + A[i, j] * x0[j]

            x[i] = (b[i] - S) / A[i, i]

        # Errores aproximados

        ea = np.zeros(f)

        for i in range(f):

            if x[i] != 0:

                ea[i] = abs(
                    (x[i] - x0[i]) / x[i]
                ) * 100

            else:

                ea[i] = 0


        # Errores verdaderos

        et = np.zeros(f)

        for i in range(f):

            et[i] = abs(
                (x_exacta[i] - x[i]) /
                x_exacta[i]
            ) * 100

        # Guardar datos

        fila = [it]

        # Valores de x
        for i in range(f):
            fila.append(x[i])

        # Errores aproximados
        for i in range(f):
            fila.append(ea[i])

        # Errores verdaderos
        for i in range(f):
            fila.append(et[i])

        datos.append(fila)


        # Error máximo aproximado

        e_max = max(ea)

        # Criterio de paro

        if e_max < tol:

            break

        # Nueva iteración
        x0 = x


    # Crear DataFrame


    columnas = ["Iteración"]

    # Variables
    for i in range(f):
        columnas.append(f"x{i+1}")

    # Errores aproximados
    for i in range(f):
        columnas.append(f"ea_x{i+1}(%)")

    # Errores verdaderos
    for i in range(f):
        columnas.append(f"et_x{i+1}(%)")

    tabla = pd.DataFrame(
        datos,
        columns=columnas
    )

    return x, tabla

# solucion con jacobi

solucion, tabla = jacobi(
    A,
    b,
    x0,
    tol,
    ItMax,
    x_exacta
)

#  tabla de resultados


print("\nTabla de resultados:\n")

print(
    tabla.to_string(
        index=False,
        float_format=lambda x: f"{x:.6f}"
    ))
