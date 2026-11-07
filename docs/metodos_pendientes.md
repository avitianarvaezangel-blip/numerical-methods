# Métodos pendientes

Inventario actualizado el 2 de noviembre de 2026 sobre la rama predeterminada `chore/organizacion-metodos-numericos` (base revisada para la última incorporación: `a6e82eff95cc1227a05d9f6b3cab23951703f23f`). El repositorio contiene 66 programas de Python, incluidos los originales sin extensión `fourier/Fourier_Par_Impar` y `aplicaciones/Fractal_Newton`. Se añadieron 19 programas de EDO para los métodos y temas del capítulo 10 del índice proporcionado; su [correspondencia por apartado](capitulo_10_edo.md) identifica las variantes implementadas. Los 47 programas anteriores conservan su contenido.

La referencia de cobertura es un curso de métodos numéricos para ingeniería, con extensiones a simulación, elementos finitos y señales. La lista es una ruta de desarrollo; no todos los métodos avanzados son necesarios en un curso introductorio.

## Qué existe y qué falta

| Área | Disponible | Pendiente | Prioridad |
| --- | --- | --- | --- |
| Errores y aritmética | Cálculos de error en algunos ejemplos; Taylor con SymPy | Ejemplos propios de redondeo, truncamiento, cifras significativas, cancelación, épsilon de máquina y propagación de errores | Alta |
| Raíces de una variable | Bisección, regla falsa, punto fijo, Newton–Raphson, Newton modificado para raíces múltiples y secante | Brent para una alternativa robusta; Müller y Bairstow para ampliar a raíces polinómicas | Ampliación |
| Sistemas lineales directos | Gauss, Gauss–Jordan, inversa, LU, Crout, QR de Householder para sistemas cuadrados, Cholesky y Cramer | Pivoteo parcial sistemático y LU/Crout con permutaciones; Thomas para sistemas tridiagonales; QR rectangular para mínimos cuadrados | Alta para pivoteo y permutaciones |
| Sistemas lineales iterativos | Jacobi; Gauss–Seidel general para `Ax = b` y en Laplace 2D; gradiente conjugado para matrices simétricas definidas positivas | SOR; precondicionamiento; soporte de matrices dispersas | Ampliación |
| Interpolación | Ejemplos lineal y cuadrático mediante SciPy | Implementaciones propias de Lagrange, Newton con diferencias divididas y splines cúbicos | Alta |
| Ajuste de datos | Sin ejemplos | Mínimos cuadrados lineales y polinómicos, preferentemente mediante QR | Media |
| Diferenciación | Primera y segunda derivadas, seis fórmulas de tercera derivada, seis de cuarta derivada y primeras derivadas parciales en x e y | Fórmulas de cinco puntos para primera y segunda derivadas; extrapolación de Richardson; derivadas mixtas y Hessiano | Media |
| Integración | Trapecio, Simpson 1/3, Simpson 3/8 y Boole compuestas; Monte Carlo; Simpson doble en rectángulos; integral impropia con cuadratura adaptativa de SciPy | Romberg; cuadratura de Gauss–Legendre; implementación propia de integración adaptativa local; integrales múltiples con límites variables o triples | Media |
| EDO | Euler explícito e implícito; Heun; punto medio y familia RK2; RK3 y RK4; AB4, AM4 y PECE; sistemas; orden superior; RK45 de SciPy; error local, paso adaptativo, estabilidad y rigidez con Radau | Problemas de frontera y disparo; métodos simplécticos; ejemplos de eventos y Jacobianos dispersos | Ampliación |
| EDP | Laplace 2D por diferencias finitas con Gauss–Seidel; calor 1D y Laplace 2D mediante series truncadas de Fourier | Calor 1D por diferencias finitas; Poisson 2D con término fuente; control de convergencia de Laplace; esquemas implícitos y Crank–Nicolson | Extensión de ingeniería |
| Elementos finitos | Conducción 1D con ensamblaje de cuatro elementos y convección en un extremo | Generalizar malla, propiedades y condiciones de frontera; después triángulo CST y tetraedro | Extensión de ingeniería |
| Fourier y señales | Series trigonométrica y compleja; simetrías par/impar, media onda y cuarto de onda par/impar; obtención de la serie por diferenciación; transformada continua por integral impropia; aplicaciones a calor 1D y Laplace 2D | DFT, FFT, espectro de señales muestreadas, convolución y comparación con bibliotecas | Extensión de ingeniería |
| Autovalores | Sin métodos dedicados | Método de la potencia e iteración inversa; aplicación a modos de vibración | Ampliación |
| Sistemas no lineales | Sin métodos multivariables | Newton para sistemas con Jacobiano y control del residuo | Ampliación |

### Distinciones para interpretar el inventario

- **LU, Crout, QR y Cholesky ya están presentes.** LU usa diagonal unitaria de L, como en Doolittle; Crout usa diagonal unitaria de U y no realiza pivoteo. QR desarrolla reflexiones de Householder para sistemas cuadrados, y Cholesky construye L para matrices reales simétricas definidas positivas. Siguen pendientes el manejo consistente de permutaciones y la extensión de QR a mínimos cuadrados rectangulares.
- **Los métodos del capítulo 10 de PVI ya tienen ejemplos.** Se conservó Euler y se añadieron los métodos escalares, sistemas, reducción de orden superior y ejemplos de control de error, estabilidad y rigidez. Los métodos multipaso arrancan con RK4; AM4 resuelve su ecuación implícita y PECE aplica una corrección. Las variantes y los equivalentes de las secciones de MATLAB se detallan en la guía del capítulo.
- **Las cuatro reglas compuestas ya están presentes.** Trapecio, Simpson 1/3, Simpson 3/8 y Boole refinan uniformemente el número de subintervalos; no implementan refinamiento adaptativo local.
- **Monte Carlo y las integrales múltiples e impropias ya tienen ejemplos.** Monte Carlo usa el promedio de muestras uniformes y muestra su incertidumbre estadística. La integral múltiple es doble y aplica Simpson 1/3 sobre un dominio rectangular. La impropia usa `scipy.integrate.quad` con un extremo infinito; la rutina adaptativa pertenece a SciPy. Las extensiones indicadas en la tabla siguen pendientes.
- **La segunda derivada y las primeras derivadas parciales ya están presentes.** El ejemplo de segunda derivada usa `exp(x)*sin(x)`; el de parciales compara las aproximaciones de x e y para `sin(x) + sin(y)`. Las derivadas mixtas, segundas parciales y un Hessiano general siguen pendientes.
- **La tercera derivada ya tiene seis fórmulas.** El nuevo programa usa diferencias hacia adelante y atrás de 4 puntos con error O(h), de 5 puntos con error O(h²), una centrada de 4 puntos con error O(h²) y una centrada de 6 puntos con error O(h⁴). Compara las seis con la derivada simbólica de `exp(x)*sin(x)`.
- **La cuarta derivada también tiene seis fórmulas.** Incluye diferencias hacia adelante y atrás de 5 puntos con error O(h), de 6 puntos con error O(h²), una centrada de 5 puntos con error O(h²) y una centrada de 7 puntos con error O(h⁴). La centrada de 7 puntos corrige la errata de signo de la tabla de referencia: ambos términos vecinos llevan coeficiente -39.
- **Gauss–Seidel y gradiente conjugado ya tienen programas propios.** Ambos devuelven solución, tabla y estado de convergencia, con paro por el residuo real `b - A @ x`. Gauss–Seidel admite matrices sin dominancia diagonal estricta, aunque su convergencia depende del sistema; gradiente conjugado requiere simetría y definición positiva. La aplicación de Gauss–Seidel a Laplace 2D continúa usando 500 barridos y aún necesita su propio criterio de paro.
- **Elementos finitos 1D ya tiene un ejemplo.** La barra ensambla matrices de cuatro elementos térmicos. No se debe seguir señalando conducción 1D como completamente ausente; lo pendiente es su generalización y la extensión a otras dimensiones.
- **Newton modificado y Cramer ya están presentes.** Su generalización y limitaciones se describen en la revisión técnica.
- **Interpolación lineal y cuadrática sí tienen ejemplos.** Para practicar la construcción del algoritmo, faltan implementaciones propias de propósito general, además de Lagrange, Newton y splines.
- **Las series y sus simetrías ya tienen ejemplos.** Además de las versiones trigonométrica y compleja de `exp(x)`, están el archivo original `Fourier_Par_Impar` y los tres programas de media onda y cuarto de onda. Los nuevos ejemplos construyen las extensiones correspondientes y usan solo armónicos impares. Cuarto de onda exige, además de paridad, simetría de media onda.
- **La obtención por diferenciación está implementada.** Recupera los coeficientes de `x**2` desde los de sus derivadas y calcula el valor medio por separado. La segunda derivada periódica incorpora la delta del salto de la primera derivada.
- **La transformada continua por integral impropia está presente.** El ejemplo usa `exp(-a*abs(x))`, con a positivo, y la convención `F(omega) = integral(f(x)*exp(-i*omega*x), -infinito, infinito)`. La DFT, la FFT y el procesamiento de señales muestreadas siguen pendientes. Las aplicaciones a EDP continúan siendo sumas de modos de Fourier; el calor por diferencias finitas temporales también sigue pendiente.
- **El modelo masa–resorte es estático.** La matriz de rigidez se escribe directamente y se resuelve con SciPy. No implementa la dinámica, un integrador de EDO ni un procedimiento general de elementos finitos.
- **Cardano es una solución algebraica.** Puede añadirse como referencia para validar raíces cúbicas, pero no es un método numérico iterativo faltante.

## Orden sugerido de implementación

| Paso | Entregable | Forma de verificarlo |
| ---: | --- | --- |
| 1 | Análisis de errores y criterios de paro comunes | Comparar error absoluto, relativo y residuo; incluir referencia cero y cancelación numérica |
| 2 | Pivoteo parcial y LU/Crout con permutaciones | Resolver un sistema que exige intercambio de filas y comprobar `P @ A = L @ U` con la convención elegida |
| 3 | Lagrange y Newton por diferencias divididas | Verificar que reproducen cada dato y un polinomio conocido; detectar nodos repetidos |
| 4 | SOR y gradiente conjugado precondicionado | Comparar iteraciones y residuo con Gauss–Seidel y gradiente conjugado en sistemas adecuados; comprobar que el precondicionador sea compatible |
| 5 | QR rectangular y mínimos cuadrados | Resolver un sistema sobredeterminado de rango completo y comprobar la ortogonalidad del residuo respecto de las columnas de A |
| 6 | Problemas de frontera para EDO y eventos | Implementar disparo con residuo de frontera y un ejemplo de detección de eventos; contrastar con SciPy |
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
