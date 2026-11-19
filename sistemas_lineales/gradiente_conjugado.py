import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Matriz real, simetrica y definida positiva; mismo sistema de Jacobi
A = np.array([
    [10, -1,  2,  0],
    [-1, 11, -1,  3],
    [ 2, -1, 10, -1],
    [ 0,  3, -1,  8]
])

b = np.array([6, 25, -11, 15])

# Aproximacion inicial, tolerancia del residuo relativo e iteraciones maximas
x0 = np.zeros(b.shape[0])
tol = 1e-8
ItMax = 100


def gradiente_conjugado(A, b, x0, tol, ItMax):

    if np.iscomplexobj(A) or np.iscomplexobj(b) or np.iscomplexobj(x0):
        raise ValueError("A, b y x0 deben contener numeros reales.")

    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    x = np.array(x0, dtype=float)

    if A.ndim != 2 or A.shape[0] == 0 or A.shape[0] != A.shape[1]:
        raise ValueError("A debe ser una matriz cuadrada no vacia.")
    f = A.shape[0]
    if b.shape != (f,) or x.shape != (f,):
        raise ValueError("b y x0 deben ser vectores compatibles con A.")
    if not all(np.all(np.isfinite(v)) for v in (A, b, x)):
        raise ValueError("Los datos deben contener valores finitos.")
    if not np.isfinite(tol) or tol <= 0:
        raise ValueError("tol debe ser positiva y finita.")
    if isinstance(ItMax, (bool, np.bool_)) or not isinstance(ItMax, (int, np.integer)) or ItMax < 1:
        raise ValueError("ItMax debe ser un entero positivo.")

    escala = np.linalg.norm(A, ord=np.inf)
    if not np.allclose(A, A.T, rtol=1e-12, atol=1e-12 * escala):
        raise ValueError("Gradiente conjugado requiere una matriz simetrica.")

    # Validacion para este ejemplo denso; la solucion se calcula abajo
    # mediante gradiente conjugado, sin usar el factor de Cholesky.
    try:
        np.linalg.cholesky(A)
    except np.linalg.LinAlgError as error:
        raise ValueError("Gradiente conjugado requiere una matriz definida positiva.") from error

    # Residuo inicial y primera direccion de busqueda
    r = b - A @ x
    p = r.copy()
    rr = r @ r

    # Si b = 0, la tolerancia se aplica al residuo absoluto.
    norma_b = np.linalg.norm(b, ord=np.inf)
    escala_b = norma_b if norma_b > 0 else 1.0
    residuo = np.linalg.norm(r, ord=np.inf)
    residuo_relativo = residuo / escala_b
    convergio = residuo_relativo <= tol

    columnas = ["Iteracion"] + [f"x{i+1}" for i in range(f)]
    columnas = columnas + ["alpha", "beta", "ea(%)", "norma residuo", "residuo relativo"]
    datos = [[0, *x, np.nan, np.nan, np.nan, residuo, residuo_relativo]]

    for it in range(1, ItMax + 1):
        if convergio:
            break

        Ap = A @ p
        denominador = p @ Ap

        if not np.isfinite(denominador) or denominador <= 0:
            raise FloatingPointError("Se perdio la curvatura positiva en la direccion de busqueda.")

        # Longitud del paso: alpha = (r.T @ r) / (p.T @ A @ p)
        alpha = rr / denominador
        x_anterior = x.copy()
        x = x + alpha * p

        # Recalcular el residuo real evita usar solo el residuo recursivo
        # para decidir si se alcanzo la tolerancia.
        r_nuevo = b - A @ x
        if not np.all(np.isfinite(x)) or not np.all(np.isfinite(r_nuevo)):
            raise FloatingPointError("Las iteraciones produjeron valores no finitos.")

        rr_nuevo = r_nuevo @ r_nuevo
        beta = rr_nuevo / rr

        cambio = np.linalg.norm(x - x_anterior, ord=np.inf)
        norma_x = np.linalg.norm(x, ord=np.inf)
        ea = 100 * cambio / norma_x if norma_x > 0 else (0.0 if cambio == 0 else np.nan)

        residuo = np.linalg.norm(r_nuevo, ord=np.inf)
        residuo_relativo = residuo / escala_b
        datos.append([it, *x, alpha, beta, ea, residuo, residuo_relativo])
        convergio = residuo_relativo <= tol

        # Nueva direccion conjugada: p_(k+1) = r_(k+1) + beta*p_k
        p = r_nuevo + beta * p
        r = r_nuevo
        rr = rr_nuevo

    tabla = pd.DataFrame(datos, columns=columnas)
    return x, tabla, convergio


x, tabla, convergio = gradiente_conjugado(A, b, x0, tol, ItMax)

# Solucion de referencia; el algoritmo no necesita conocerla.
x2 = np.linalg.solve(A, b)

print("\nTabla de resultados (alpha, beta y ea no se definen en la iteracion inicial):\n")
print(tabla.to_string(index=False, float_format=lambda valor: f"{valor:.6e}"))
print("\nx =", x)
print("x con NumPy =", x2)
print("Error absoluto maximo =", np.linalg.norm(x - x2, ord=np.inf))
print("Norma del residuo =", np.linalg.norm(b - A @ x, ord=np.inf))

if convergio:
    print("Convergencia alcanzada en", int(tabla.iloc[-1]['Iteracion']), "iteraciones.")
else:
    print("Se alcanzo ItMax sin cumplir la tolerancia.")

# Grafica de convergencia
plt.figure(figsize=(10, 6))
plt.semilogy(tabla['Iteracion'], tabla['residuo relativo'], 'bo-', label='Residuo relativo')
plt.axhline(tol, color='r', linestyle='--', label=f'Tolerancia = {tol:.0e}')
plt.xlabel('Iteracion')
plt.xticks(tabla['Iteracion'])
plt.ylabel(r'$\|b-Ax\|_\infty/\|b\|_\infty$')
plt.title('Metodo de gradiente conjugado', fontsize=20)
plt.legend(fontsize=12)
plt.grid(True, which='both')
plt.tight_layout()
plt.show()
