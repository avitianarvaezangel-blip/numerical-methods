# Métodos pendientes

Inventario del código de la rama `main`, commit `7083e57c23aa3eb22d88f7242e293f685c840e21`, revisado el 18 de octubre de 2026. Se revisaron los 18 scripts disponibles. Esta reorganización no añade implementaciones de los métodos que aparecen como pendientes.

La referencia de cobertura es un curso de métodos numéricos para ingeniería, con extensiones a simulación, elementos finitos y señales. La lista es una ruta de desarrollo; no todos los métodos avanzados son necesarios en un curso introductorio.

## Qué existe y qué falta

| Área | Disponible | Pendiente | Prioridad |
| --- | --- | --- | --- |
| Errores y aritmética | Cálculos de error en algunos ejemplos; Taylor con SymPy | Ejemplos propios de redondeo, truncamiento, cifras significativas, cancelación, épsilon de máquina y propagación de errores | Alta |
| Raíces de una variable | Bisección, regla falsa, punto fijo, Newton–Raphson y secante | Brent para una alternativa robusta; Müller y Bairstow para ampliar a raíces polinómicas | Ampliación |
| Sistemas lineales directos | Gauss, Gauss–Jordan, inversa y LU | Pivoteo parcial sistemático y LU con permutaciones; Cholesky; QR; Thomas para sistemas tridiagonales | Alta |
| Sistemas lineales iterativos | Jacobi | Gauss–Seidel; posteriormente SOR y gradiente conjugado | Alta para Gauss–Seidel; ampliación para SOR y gradiente conjugado |
| Interpolación | Ejemplos lineal y cuadrático mediante SciPy | Implementaciones propias de Lagrange, Newton con diferencias divididas y splines cúbicos | Alta |
| Ajuste de datos | Sin ejemplos | Mínimos cuadrados lineales y polinómicos, preferentemente mediante QR | Media |
| Diferenciación | Primera derivada hacia adelante, atrás y centrada | Segunda derivada; fórmulas de cinco puntos; extrapolación de Richardson | Media |
| Integración | Trapecio compuesto y Simpson 3/8 compuesto | Simpson 1/3 compuesto; Romberg; cuadratura de Gauss–Legendre; integración adaptativa | Alta para Simpson 1/3; media para las demás |
| EDO | Sin integradores temporales | Euler; Heun; punto medio/RK2; RK4; sistemas de EDO; después Euler implícito y métodos multipaso | Alta |
| EDP | Sin discretizaciones | Calor 1D por diferencias finitas; Laplace/Poisson 2D; después esquemas implícitos y Crank–Nicolson | Extensión de ingeniería |
| Elementos finitos | Sin ensamblaje de elementos | Barra o conducción 1D; posteriormente triángulo CST y tetraedro | Extensión de ingeniería |
| Fourier y señales | Coeficientes simbólicos y suma parcial de una serie | DFT, FFT, espectro de señales muestreadas, convolución y comparación con bibliotecas | Extensión de ingeniería |
| Autovalores | Sin métodos dedicados | Método de la potencia e iteración inversa; aplicación a modos de vibración | Ampliación |
| Sistemas no lineales | Sin métodos multivariables | Newton para sistemas con Jacobiano y control del residuo | Ampliación |

### Distinciones para interpretar el inventario

- **LU ya está presente.** El script construye L con diagonal unitaria, como en Doolittle sin pivoteo. Lo pendiente es corregir y generalizar el manejo de permutaciones; no hace falta contar Doolittle como un método ausente.
- **Gauss–Seidel está ausente.** Su mención en el README anterior no correspondía a un archivo implementado.
- **Interpolación lineal y cuadrática sí tienen ejemplos.** Para practicar la construcción del algoritmo, faltan implementaciones propias de propósito general, además de Lagrange, Newton y splines.
- **La serie de Fourier sí está presente.** Calcula integrales simbólicas; no sustituye una DFT o una FFT sobre muestras.
- **El modelo masa–resorte es estático.** La matriz de rigidez se escribe directamente y se resuelve con SciPy. No implementa la dinámica, un integrador de EDO ni un procedimiento general de elementos finitos.
- **Cardano es una solución algebraica.** Puede añadirse como referencia para validar raíces cúbicas, pero no es un método numérico iterativo faltante.

## Orden sugerido de implementación

| Paso | Entregable | Forma de verificarlo |
| ---: | --- | --- |
| 1 | Análisis de errores y criterios de paro comunes | Comparar error absoluto, relativo y residuo; incluir referencia cero y cancelación numérica |
| 2 | Gauss–Seidel | Compararlo con Jacobi y `numpy.linalg.solve` en el sistema 4×4 del repositorio; medir también `norm(A @ x - b)` |
| 3 | Simpson 1/3 compuesto | Integrar polinomios de grado hasta tres y rechazar un número impar de subintervalos |
| 4 | Lagrange y Newton por diferencias divididas | Verificar que reproducen cada dato y un polinomio conocido; detectar nodos repetidos |
| 5 | Pivoteo parcial y LU con permutaciones | Resolver un sistema que exige intercambio de filas y comprobar `P @ A = L @ U` con la convención elegida |
| 6 | Cholesky y QR | Comprobar `A = L @ L.T`, o `A = Q @ R` y `Q.T @ Q = I`, y resolver un problema conocido |
| 7 | Euler, Heun y RK4 | Comparar con una EDO de solución analítica y observar el error al reducir el paso |
| 8 | Splines, mínimos cuadrados y cuadraturas adicionales | Usar datos con solución conocida y comparar con SciPy |
| 9 | Calor 1D y Laplace 2D | Verificar fronteras, residuo y convergencia de malla; comprobar la restricción de estabilidad del esquema explícito |
| 10 | Elementos finitos 1D y DFT/FFT | Comparar una barra con solución analítica y reconstruir una señal con frecuencias conocidas |

## Formato sugerido para cada implementación nueva

1. Explicar el problema, las hipótesis y los parámetros.
2. Escribir una función reutilizable y colocar la demostración bajo `if __name__ == "__main__":`.
3. Validar dimensiones, dominio, tolerancia y número máximo de iteraciones.
4. Devolver el resultado, un historial cuando corresponda y el estado de convergencia.
5. Comparar con una solución analítica o una biblioteca de referencia, sin exigir conocer la solución para que el algoritmo funcione.
6. Incluir una tabla o gráfica cuando ayude a interpretar el error y la convergencia.

Antes de añadir muchos métodos, conviene atender las [limitaciones comprobadas del código existente](revision_tecnica.md), especialmente LU con intercambio de filas y el tratamiento de pivotes.
