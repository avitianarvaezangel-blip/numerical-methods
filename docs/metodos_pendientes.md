# Métodos pendientes

Inventario del código de la rama `main`, commit `642750b599618097bdcc2d6b9c5ccbd106e3cff5`, revisado el 25 de octubre de 2026. Se revisaron los 26 scripts disponibles, incluidos Newton modificado, Cramer, conducción 1D por elementos finitos y tres ejemplos de EDP. La reorganización conserva su contenido y no añade implementaciones de los métodos que aparecen como pendientes.

La referencia de cobertura es un curso de métodos numéricos para ingeniería, con extensiones a simulación, elementos finitos y señales. La lista es una ruta de desarrollo; no todos los métodos avanzados son necesarios en un curso introductorio.

## Qué existe y qué falta

| Área | Disponible | Pendiente | Prioridad |
| --- | --- | --- | --- |
| Errores y aritmética | Cálculos de error en algunos ejemplos; Taylor con SymPy | Ejemplos propios de redondeo, truncamiento, cifras significativas, cancelación, épsilon de máquina y propagación de errores | Alta |
| Raíces de una variable | Bisección, regla falsa, punto fijo, Newton–Raphson, Newton modificado para raíces múltiples y secante | Brent para una alternativa robusta; Müller y Bairstow para ampliar a raíces polinómicas | Ampliación |
| Sistemas lineales directos | Gauss, Gauss–Jordan, inversa, LU y Cramer | Pivoteo parcial sistemático y LU con permutaciones; Cholesky; QR; Thomas para sistemas tridiagonales | Alta |
| Sistemas lineales iterativos | Jacobi; Gauss–Seidel en el barrido de Laplace 2D | Solucionador general de Gauss–Seidel para `Ax = b`; posteriormente SOR y gradiente conjugado | Alta para generalizar Gauss–Seidel; ampliación para SOR y gradiente conjugado |
| Interpolación | Ejemplos lineal y cuadrático mediante SciPy | Implementaciones propias de Lagrange, Newton con diferencias divididas y splines cúbicos | Alta |
| Ajuste de datos | Sin ejemplos | Mínimos cuadrados lineales y polinómicos, preferentemente mediante QR | Media |
| Diferenciación | Primera derivada hacia adelante, atrás y centrada | Segunda derivada; fórmulas de cinco puntos; extrapolación de Richardson | Media |
| Integración | Trapecio compuesto, Simpson 1/3 compuesto y Simpson 3/8 compuesto | Romberg; cuadratura de Gauss–Legendre; integración adaptativa | Media |
| EDO | Euler explícito para una EDO escalar | Heun; punto medio/RK2; RK4; sistemas de EDO; después Euler implícito y métodos multipaso | Alta |
| EDP | Laplace 2D por diferencias finitas con Gauss–Seidel; calor 1D y Laplace 2D mediante series truncadas de Fourier | Calor 1D por diferencias finitas; Poisson 2D con término fuente; control de convergencia de Laplace; esquemas implícitos y Crank–Nicolson | Extensión de ingeniería |
| Elementos finitos | Conducción 1D con ensamblaje de cuatro elementos y convección en un extremo | Generalizar malla, propiedades y condiciones de frontera; después triángulo CST y tetraedro | Extensión de ingeniería |
| Fourier y señales | Serie de Fourier de una función y aplicaciones a calor 1D y Laplace 2D | DFT, FFT, espectro de señales muestreadas, convolución y comparación con bibliotecas | Extensión de ingeniería |
| Autovalores | Sin métodos dedicados | Método de la potencia e iteración inversa; aplicación a modos de vibración | Ampliación |
| Sistemas no lineales | Sin métodos multivariables | Newton para sistemas con Jacobiano y control del residuo | Ampliación |

### Distinciones para interpretar el inventario

- **LU ya está presente.** El script construye L con diagonal unitaria, como en Doolittle sin pivoteo. Lo pendiente es corregir y generalizar el manejo de permutaciones; no hace falta contar Doolittle como un método ausente.
- **Euler y Simpson 1/3 ya están presentes.** La lista anterior los señalaba como ausentes. Euler resuelve un problema escalar; los sistemas de EDO y métodos de orden superior siguen pendientes. Simpson 1/3 y trapecio refinan uniformemente el número de subintervalos; no implementan refinamiento adaptativo local.
- **Gauss–Seidel ya aparece en Laplace 2D.** La placa actualiza cada nodo en el mismo arreglo y usa los valores nuevos durante el barrido. Falta extraer una función general para `Ax = b` con residuo y criterio de paro; el ejemplo actual fija 500 barridos.
- **Elementos finitos 1D ya tiene un ejemplo.** La barra ensambla matrices de cuatro elementos térmicos. No se debe seguir señalando conducción 1D como completamente ausente; lo pendiente es su generalización y la extensión a otras dimensiones.
- **Newton modificado y Cramer ya están presentes.** Su generalización y limitaciones se describen en la revisión técnica.
- **Interpolación lineal y cuadrática sí tienen ejemplos.** Para practicar la construcción del algoritmo, faltan implementaciones propias de propósito general, además de Lagrange, Newton y splines.
- **Las aplicaciones de Fourier a EDP están presentes.** Calculan coeficientes simbólicos y evalúan sumas finitas; no sustituyen una DFT o una FFT sobre muestras ni una discretización temporal por diferencias finitas.
- **El modelo masa–resorte es estático.** La matriz de rigidez se escribe directamente y se resuelve con SciPy. No implementa la dinámica, un integrador de EDO ni un procedimiento general de elementos finitos.
- **Cardano es una solución algebraica.** Puede añadirse como referencia para validar raíces cúbicas, pero no es un método numérico iterativo faltante.

## Orden sugerido de implementación

| Paso | Entregable | Forma de verificarlo |
| ---: | --- | --- |
| 1 | Análisis de errores y criterios de paro comunes | Comparar error absoluto, relativo y residuo; incluir referencia cero y cancelación numérica |
| 2 | Gauss–Seidel general para `Ax = b` | Compararlo con Jacobi y `numpy.linalg.solve` en el sistema 4×4 del repositorio; medir también `norm(A @ x - b)` |
| 3 | Lagrange y Newton por diferencias divididas | Verificar que reproducen cada dato y un polinomio conocido; detectar nodos repetidos |
| 4 | Pivoteo parcial y LU con permutaciones | Resolver un sistema que exige intercambio de filas y comprobar `P @ A = L @ U` con la convención elegida |
| 5 | Cholesky y QR | Comprobar `A = L @ L.T`, o `A = Q @ R` y `Q.T @ Q = I`, y resolver un problema conocido |
| 6 | Heun, punto medio y RK4 | Comparar con Euler y una solución analítica; observar el error al reducir el paso |
| 7 | Splines, mínimos cuadrados y diferenciación de orden superior | Usar datos con solución conocida y comparar con SciPy o derivadas analíticas |
| 8 | Romberg y Gauss–Legendre | Comprobar convergencia y exactitud sobre polinomios conocidos |
| 9 | Calor 1D por diferencias finitas y Poisson 2D | Usar el ejemplo de Fourier como referencia para calor; verificar fronteras, residuo y convergencia de malla, y comprobar la estabilidad del esquema explícito |
| 10 | Generalización del MEF 1D, triángulo CST y DFT/FFT | Verificar el ensamblaje y las fronteras de la barra, ampliar a un elemento 2D y reconstruir una señal con frecuencias conocidas |

## Formato sugerido para cada implementación nueva

1. Explicar el problema, las hipótesis y los parámetros.
2. Escribir una función reutilizable y colocar la demostración bajo `if __name__ == "__main__":`.
3. Validar dimensiones, dominio, tolerancia y número máximo de iteraciones.
4. Devolver el resultado, un historial cuando corresponda y el estado de convergencia.
5. Comparar con una solución analítica o una biblioteca de referencia, sin exigir conocer la solución para que el algoritmo funcione.
6. Incluir una tabla o gráfica cuando ayude a interpretar el error y la convergencia.

Antes de añadir muchos métodos, conviene atender las [limitaciones comprobadas del código existente](revision_tecnica.md), especialmente LU con intercambio de filas y el tratamiento de pivotes.
