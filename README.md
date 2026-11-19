# Métodos numéricos con Python

Ejemplos didácticos de métodos numéricos y matemáticas aplicadas a la ingeniería, con cálculos paso a paso, tablas, gráficas y animaciones.

**Autor:** Ángel A. Avitia N.

El repositorio contiene **66 programas de Python**, organizados en once áreas. Algunos desarrollan el algoritmo con ciclos y operaciones elementales; otros muestran aplicaciones de NumPy, SciPy o SymPy. El índice distingue ambos casos. Inventario actualizado el **2 de noviembre de 2026**.

## Instalación

```bash
git clone https://github.com/avitianarvaezangel-blip/numerical-methods.git
cd numerical-methods
python -m venv .venv
```

Activa el entorno:

```bash
# Linux / macOS
source .venv/bin/activate
```

```powershell
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Instala las dependencias:

```bash
python -m pip install -r requirements.txt
```

## Organización

| Carpeta | Tema | Scripts |
| --- | --- | ---: |
| [fundamentos](fundamentos/) | Aproximación mediante Taylor | 1 |
| [raices](raices/) | Ecuaciones no lineales de una variable | 6 |
| [sistemas_lineales](sistemas_lineales/) | Métodos directos e iterativos | 11 |
| [interpolacion](interpolacion/) | Interpolación con SciPy | 2 |
| [diferenciacion](diferenciacion/) | Derivadas de primer a cuarto orden y derivadas parciales | 5 |
| [integracion](integracion/) | Cuadraturas, Monte Carlo e integrales múltiples e impropias | 7 |
| [edo](edo/) | Problemas de valor inicial: métodos del capítulo 10 | 20 |
| [edp](edp/) | Calor y Laplace: diferencias finitas y series de Fourier | 3 |
| [elementos_finitos](elementos_finitos/) | Conducción térmica en una barra 1D | 1 |
| [fourier](fourier/) | Series, simetrías, diferenciación y transformada continua de Fourier | 8 |
| [aplicaciones](aplicaciones/) | Modelo estático de masa y resortes y fractal de Newton | 2 |
| [docs](docs/) | Pendientes, revisión técnica y cambios de rutas | — |

## Índice de métodos y ejemplos

“Algoritmo propio” indica que el script desarrolla el procedimiento. La presencia de una implementación no garantiza que maneje todos los datos de entrada; consulta la [revisión técnica](docs/revision_tecnica.md).

| Tema | Archivo | Contenido | Desarrollo |
| --- | --- | --- | --- |
| Fundamentos | [taylor_exponencial.py](fundamentos/taylor_exponencial.py) | Aproximación de `exp(-x**2)` e integración de un polinomio truncado | SymPy |
| Raíces | [biseccion.py](raices/biseccion.py) | Bisección, tabla de iteraciones y animación | Algoritmo propio |
| Raíces | [regla_falsa.py](raices/regla_falsa.py) | Regla falsa, tabla y animación de la secante | Algoritmo propio |
| Raíces | [newton_raphson.py](raices/newton_raphson.py) | Newton–Raphson con derivada simbólica | Algoritmo propio + SymPy |
| Raíces | [newton_raphson_modificado.py](raices/newton_raphson_modificado.py) | Newton modificado para raíces múltiples, con primera y segunda derivadas | Algoritmo propio + SymPy |
| Raíces | [secante.py](raices/secante.py) | Método de la secante | Algoritmo propio + SymPy |
| Raíces | [punto_fijo.py](raices/punto_fijo.py) | Iteración `g(x) = exp(-x)` | Algoritmo propio |
| Sistemas lineales | [eliminacion_gaussiana.py](sistemas_lineales/eliminacion_gaussiana.py) | Eliminación y sustitución hacia atrás | Algoritmo propio |
| Sistemas lineales | [gauss_jordan.py](sistemas_lineales/gauss_jordan.py) | Reducción de la matriz aumentada | Algoritmo propio |
| Sistemas lineales | [factorizacion_lu.py](sistemas_lineales/factorizacion_lu.py) | LU con diagonal unitaria de L y solución de `Ax = b` | Algoritmo propio |
| Sistemas lineales | [factorizacion_crout.py](sistemas_lineales/factorizacion_crout.py) | Crout sin pivoteo, diagonal unitaria de U, sustituciones y gráfica de planos | Algoritmo propio |
| Sistemas lineales | [factorizacion_qr.py](sistemas_lineales/factorizacion_qr.py) | QR mediante reflexiones de Householder, solución de un sistema cuadrado y gráfica de planos | Algoritmo propio |
| Sistemas lineales | [factorizacion_cholesky.py](sistemas_lineales/factorizacion_cholesky.py) | Factorización `A = L @ L.T` para una matriz real simétrica definida positiva, sustituciones y gráfica de planos | Algoritmo propio |
| Sistemas lineales | [matriz_inversa.py](sistemas_lineales/matriz_inversa.py) | Inversa mediante operaciones elementales | Algoritmo propio |
| Sistemas lineales | [jacobi.py](sistemas_lineales/jacobi.py) | Jacobi con tabla y errores porcentuales | Algoritmo propio |
| Sistemas lineales | [gauss_seidel.py](sistemas_lineales/gauss_seidel.py) | Solución de `Ax = b` con actualizaciones sucesivas, tabla, paro por residuo y gráfica de convergencia | Algoritmo propio |
| Sistemas lineales | [gradiente_conjugado.py](sistemas_lineales/gradiente_conjugado.py) | Gradiente conjugado para matrices reales simétricas definidas positivas, tabla y gráfica de convergencia | Algoritmo propio + validación con NumPy |
| Sistemas lineales | [cramer.py](sistemas_lineales/cramer.py) | Regla de Cramer mediante determinantes | Algoritmo propio + NumPy |
| Interpolación | [lineal.py](interpolacion/lineal.py) | Interpolación lineal de `ln(x)` | `scipy.interpolate.interp1d` |
| Interpolación | [cuadratica.py](interpolacion/cuadratica.py) | Interpolación cuadrática de `ln(x)` | `scipy.interpolate.interp1d` |
| Diferenciación | [diferencias_finitas.py](diferenciacion/diferencias_finitas.py) | Primera derivada de `exp(x)*sin(x)`: diferencias hacia adelante, atrás y centrada | Algoritmo propio + SymPy |
| Diferenciación | [segunda_derivada.py](diferenciacion/segunda_derivada.py) | Segunda derivada de `exp(x)*sin(x)`: tres fórmulas de diferencias finitas y comparación analítica | Algoritmo propio + SymPy |
| Diferenciación | [tercera_derivada.py](diferenciacion/tercera_derivada.py) | Tercera derivada: adelante y atrás con 4 y 5 puntos, centradas con 4 y 6 puntos, gráfica y errores máximos | Algoritmo propio + SymPy |
| Diferenciación | [cuarta_derivada.py](diferenciacion/cuarta_derivada.py) | Cuarta derivada: adelante y atrás con 5 y 6 puntos, centradas con 5 y 7 puntos, gráfica y errores máximos | Algoritmo propio + SymPy |
| Diferenciación | [derivadas_parciales.py](diferenciacion/derivadas_parciales.py) | Derivadas respecto a x e y de `sin(x) + sin(y)`, con fórmulas hacia adelante, atrás y centradas y ocho superficies | Algoritmo propio + SymPy |
| Integración | [trapecio.py](integracion/trapecio.py) | Trapecio compuesto con refinamiento uniforme, tabla y errores | Algoritmo propio |
| Integración | [simpson_1_3.py](integracion/simpson_1_3.py) | Simpson 1/3 compuesto con refinamiento uniforme, tabla y errores | Algoritmo propio |
| Integración | [simpson_3_8.py](integracion/simpson_3_8.py) | Simpson 3/8 compuesto con refinamiento uniforme, tabla y errores | Algoritmo propio |
| Integración | [boole.py](integracion/boole.py) | Boole compuesta con múltiplos de cuatro subintervalos, tabla y errores | Algoritmo propio |
| Integración | [monte_carlo.py](integracion/monte_carlo.py) | Muestreo uniforme reproducible, promedio de muestras, error estándar e intervalo aproximado del 95% | Algoritmo propio + NumPy |
| Integración | [integral_multiple.py](integracion/integral_multiple.py) | Integral doble en un rectángulo por Simpson 1/3 en ambas direcciones, tabla de refinamiento y superficie | Algoritmo propio + SymPy |
| Integración | [integral_impropia.py](integracion/integral_impropia.py) | Integral de `1/(1+x**2)` de cero a infinito; comparación con límites finitos y referencia simbólica | `scipy.integrate.quad` + SymPy |
| EDO | [euler.py](edo/euler.py) | Euler explícito para `y' = (x**2 - 1)/y**2`, con comparación analítica | Algoritmo propio |
| EDO | [euler_implicito.py](edo/euler_implicito.py) | Euler implícito con Newton en cada paso | Algoritmo propio |
| EDO | [euler_modificado.py](edo/euler_modificado.py) | Euler modificado de Heun | Algoritmo propio |
| EDO | [punto_medio.py](edo/punto_medio.py) | Método explícito del punto medio | Algoritmo propio |
| EDO | [runge_kutta_2.py](edo/runge_kutta_2.py) | Familia RK2; Ralston por defecto y parámetros para Heun o punto medio | Algoritmo propio |
| EDO | [runge_kutta_3.py](edo/runge_kutta_3.py) | RK3 clásico de Kutta | Algoritmo propio |
| EDO | [runge_kutta_4.py](edo/runge_kutta_4.py) | RK4 clásico de cuatro etapas | Algoritmo propio |
| EDO | [adams_bashforth.py](edo/adams_bashforth.py) | Adams–Bashforth AB4 y arranque con RK4 | Algoritmo propio |
| EDO | [adams_moulton.py](edo/adams_moulton.py) | Adams–Moulton de orden cuatro con Newton y arranque RK4 | Algoritmo propio |
| EDO | [predictor_corrector.py](edo/predictor_corrector.py) | AB4–AM4 con una corrección PECE | Algoritmo propio |
| EDO | [euler_sistemas.py](edo/euler_sistemas.py) | Euler explícito para sistemas | Algoritmo propio |
| EDO | [euler_modificado_sistemas.py](edo/euler_modificado_sistemas.py) | Heun para sistemas | Algoritmo propio |
| EDO | [runge_kutta_4_sistemas.py](edo/runge_kutta_4_sistemas.py) | RK4 para sistemas | Algoritmo propio |
| EDO | [edo_orden_superior.py](edo/edo_orden_superior.py) | Reducción de una EDO de segundo orden a un sistema, resuelto con RK4 | Algoritmo propio |
| EDO | [solve_ivp_escalar.py](edo/solve_ivp_escalar.py) | PVI escalar con RK45 adaptativo | SciPy |
| EDO | [solve_ivp_sistemas.py](edo/solve_ivp_sistemas.py) | Sistema de EDO con RK45 adaptativo | SciPy |
| EDO | [error_truncamiento.py](edo/error_truncamiento.py) | Error local de un paso en Euler y RK2 | Análisis numérico con NumPy |
| EDO | [paso_adaptativo.py](edo/paso_adaptativo.py) | RK4 con control local de error por duplicación de pasos | Algoritmo propio |
| EDO | [estabilidad.py](edo/estabilidad.py) | Factores de amplificación y prueba de estabilidad temporal | Algoritmo propio |
| EDO | [edo_rigida.py](edo/edo_rigida.py) | Comparación de Euler explícito, implícito y Radau en una EDO rígida | Algoritmos propios + SciPy |
| EDP | [calor_1d_fourier.py](edp/calor_1d_fourier.py) | Calor 1D transitorio, extremos a cero e inicio a 100: cinco modos de Fourier | Coeficientes simbólicos + evaluación numérica |
| EDP | [laplace_2d_diferencias_finitas.py](edp/laplace_2d_diferencias_finitas.py) | Laplace 2D: bordes superior e izquierdo a 100; esquema de cinco puntos con barridos Gauss–Seidel | Algoritmo propio |
| EDP | [laplace_2d_fourier.py](edp/laplace_2d_fourier.py) | Laplace en un cuadrado: borde superior a 100 y los otros tres a cero; diez modos de Fourier | Coeficientes simbólicos + evaluación numérica |
| Elementos finitos | [conduccion_barra_1d.py](elementos_finitos/conduccion_barra_1d.py) | Ensamblaje de cuatro elementos, temperatura prescrita y convección en el extremo | Ensamblaje propio + solución con NumPy |
| Fourier | [serie_fourier.py](fourier/serie_fourier.py) | Coeficientes y suma parcial de `exp(x)` en `[-pi, pi]` | Integración simbólica con SymPy |
| Fourier | [serie_compleja_fourier.py](fourier/serie_compleja_fourier.py) | Coeficientes complejos y suma de frecuencias de -20 a 20 de `exp(x)`, con gráfica comparativa | Integración simbólica con SymPy |
| Fourier | [Fourier_Par_Impar](fourier/Fourier_Par_Impar) | Programa original de referencia: detección par/impar y serie de `x**2`; conserva su nombre sin extensión | Integración simbólica con SymPy |
| Fourier | [serie_media_onda.py](fourier/serie_media_onda.py) | Extensión con simetría de media onda, integrales en medio periodo y armónicos impares de seno y coseno | SymPy + NumPy |
| Fourier | [serie_cuarto_onda_par.py](fourier/serie_cuarto_onda_par.py) | Extensión par con simetría de media onda; coeficientes de coseno desde el primer cuarto | SymPy + NumPy |
| Fourier | [serie_cuarto_onda_impar.py](fourier/serie_cuarto_onda_impar.py) | Onda triangular impar con simetría de media onda; coeficientes de seno desde el primer cuarto | SymPy + NumPy |
| Fourier | [serie_por_diferenciacion.py](fourier/serie_por_diferenciacion.py) | Recuperación de la serie de `x**2` desde la primera y segunda derivadas periódicas, incluyendo la delta y el valor medio | SymPy + NumPy |
| Fourier | [transformada_fourier_continua.py](fourier/transformada_fourier_continua.py) | Transformada de `exp(-a*abs(x))` por las integrales impropias sobre ambos semiejes, con a positivo | Integración simbólica con SymPy + NumPy |
| Aplicaciones | [masa_resorte_estatico.py](aplicaciones/masa_resorte_estatico.py) | Desplazamientos de equilibrio mediante `K x = W` | Inversa con SciPy |
| Aplicaciones | [Fractal_Newton](aplicaciones/Fractal_Newton) | Cuencas de atracción de Newton para `z**3-1` en el plano complejo; archivo original sin extensión | Algoritmo propio + NumPy |

## Cómo ejecutar los ejemplos

Desde la raíz del repositorio:

```bash
python sistemas_lineales/jacobi.py
python sistemas_lineales/factorizacion_crout.py
python sistemas_lineales/factorizacion_qr.py
python sistemas_lineales/factorizacion_cholesky.py
python sistemas_lineales/gauss_seidel.py
python sistemas_lineales/gradiente_conjugado.py
python interpolacion/lineal.py
python edo/euler.py
python edo/euler_modificado.py
python edo/runge_kutta_4.py
python edo/adams_bashforth.py
python edo/runge_kutta_4_sistemas.py
python edo/paso_adaptativo.py
python integracion/simpson_1_3.py
python integracion/boole.py
python integracion/monte_carlo.py
python integracion/integral_multiple.py
python integracion/integral_impropia.py
python sistemas_lineales/cramer.py
python edp/laplace_2d_diferencias_finitas.py
python diferenciacion/segunda_derivada.py
python diferenciacion/tercera_derivada.py
python diferenciacion/cuarta_derivada.py
python diferenciacion/derivadas_parciales.py
python fourier/serie_compleja_fourier.py
python fourier/Fourier_Par_Impar
python fourier/serie_media_onda.py
python fourier/serie_cuarto_onda_par.py
python fourier/serie_cuarto_onda_impar.py
python fourier/serie_por_diferenciacion.py
python fourier/transformada_fourier_continua.py
```

Los datos del problema se editan dentro de cada archivo. Los scripts conservan su desarrollo didáctico original y ejecutan sus ejemplos al cargarse; todavía no constituyen una biblioteca con una interfaz común.

Los dos ejemplos de placa usan condiciones de frontera distintas; sus resultados no se comparan directamente sin igualar esas condiciones. La temperatura ambiente del ejemplo de elementos finitos pertenece a la condición convectiva; no es un nodo adicional de la barra. Consulta la revisión técnica para interpretar las gráficas.

### Gráficas en Spyder, IPython o Jupyter

Algunos ejemplos construyen la figura sin llamar a `plt.show()`. En una consola de IPython/Spyder o en una celda de Jupyter puedes ejecutarlos así:

```python
%run integracion/trapecio.py
import matplotlib.pyplot as plt
plt.show()
```

### Animaciones de bisección y regla falsa

Estos scripts generan una animación HTML. Para verla, ejecuta en una celda de Jupyter/IPython, con el directorio de trabajo en la raíz del repositorio:

```python
%run raices/biseccion.py
from IPython.display import HTML, display
display(HTML(ani.to_jshtml()))
```

Para regla falsa, cambia la ruta por `raices/regla_falsa.py`. Ejecutar esos archivos desde una terminal calcula la tabla y el HTML, pero no abre automáticamente la animación.

## Métodos que faltan

Las prioridades para ampliar el curso son **análisis de errores, pivoteo y factorizaciones con permutaciones, interpolación de Lagrange y Newton, mínimos cuadrados, Romberg y Gauss–Legendre**. Consulta la [lista completa de métodos pendientes](docs/metodos_pendientes.md), que también incluye extensiones a EDP, elementos finitos y análisis de señales.

Ya están implementados Gauss–Seidel general, gradiente conjugado, Crout, Cholesky y QR, además de las reglas de integración, diferenciación, Fourier, EDP y conducción 1D por elementos finitos. La carpeta `edo` cubre los métodos del capítulo 10 según la [correspondencia por apartado](docs/capitulo_10_edo.md). El archivo de masa–resorte conserva su modelo de equilibrio estático.

## Documentación

- [Métodos pendientes y orden sugerido](docs/metodos_pendientes.md).
- [Limitaciones y verificación del código actual](docs/revision_tecnica.md).
- [Correspondencia entre nombres anteriores y rutas nuevas](docs/migracion.md).
- [Capítulo 10: métodos de EDO y correspondencia por apartado](docs/capitulo_10_edo.md).

Los 29 scripts recibidos en `main` y revisados el 25 de octubre conservan su contenido. Las incorporaciones posteriores están registradas en la revisión técnica. Los programas nuevos usan nombres en minúsculas, sin espacios ni acentos y con extensión `.py`; `Fourier_Par_Impar` y `Fractal_Newton` conservan los nombres originales sin extensión.

Para mantener esta estructura, añade los nuevos ejemplos a su carpeta temática en la rama predeterminada y actualiza el índice y la lista de pendientes.
