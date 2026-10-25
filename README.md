# Métodos numéricos con Python

Ejemplos didácticos de métodos numéricos y matemáticas aplicadas a la ingeniería, con cálculos paso a paso, tablas, gráficas y animaciones.

**Autor:** Ángel A. Avitia N.

El repositorio contiene **26 scripts**, organizados en once áreas. Algunos desarrollan el algoritmo con ciclos y operaciones elementales; otros muestran aplicaciones de NumPy, SciPy o SymPy. El índice distingue ambos casos. Inventario actualizado el **25 de octubre de 2026**.

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
| [sistemas_lineales](sistemas_lineales/) | Métodos directos e iterativos | 6 |
| [interpolacion](interpolacion/) | Interpolación con SciPy | 2 |
| [diferenciacion](diferenciacion/) | Diferencias finitas | 1 |
| [integracion](integracion/) | Cuadratura numérica | 3 |
| [edo](edo/) | Ecuaciones diferenciales ordinarias | 1 |
| [edp](edp/) | Calor y Laplace: diferencias finitas y series de Fourier | 3 |
| [elementos_finitos](elementos_finitos/) | Conducción térmica en una barra 1D | 1 |
| [fourier](fourier/) | Coeficientes y sumas parciales de Fourier | 1 |
| [aplicaciones](aplicaciones/) | Modelo estático de masa y resortes | 1 |
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
| Sistemas lineales | [matriz_inversa.py](sistemas_lineales/matriz_inversa.py) | Inversa mediante operaciones elementales | Algoritmo propio |
| Sistemas lineales | [jacobi.py](sistemas_lineales/jacobi.py) | Jacobi con tabla y errores porcentuales | Algoritmo propio |
| Sistemas lineales | [cramer.py](sistemas_lineales/cramer.py) | Regla de Cramer mediante determinantes | Algoritmo propio + NumPy |
| Interpolación | [lineal.py](interpolacion/lineal.py) | Interpolación lineal de `ln(x)` | `scipy.interpolate.interp1d` |
| Interpolación | [cuadratica.py](interpolacion/cuadratica.py) | Interpolación cuadrática de `ln(x)` | `scipy.interpolate.interp1d` |
| Diferenciación | [diferencias_finitas.py](diferenciacion/diferencias_finitas.py) | Primera derivada de `exp(x)*sin(x)`: diferencias hacia adelante, atrás y centrada | Algoritmo propio + SymPy |
| Integración | [trapecio.py](integracion/trapecio.py) | Trapecio compuesto con refinamiento uniforme, tabla y errores | Algoritmo propio |
| Integración | [simpson_1_3.py](integracion/simpson_1_3.py) | Simpson 1/3 compuesto con refinamiento uniforme, tabla y errores | Algoritmo propio |
| Integración | [simpson_3_8.py](integracion/simpson_3_8.py) | Regla compuesta de Simpson 3/8 | Algoritmo propio |
| EDO | [euler.py](edo/euler.py) | Euler explícito para `y' = (x**2 - 1)/y**2`, con comparación analítica | Algoritmo propio |
| EDP | [calor_1d_fourier.py](edp/calor_1d_fourier.py) | Calor 1D transitorio, extremos a cero e inicio a 100: cinco modos de Fourier | Coeficientes simbólicos + evaluación numérica |
| EDP | [laplace_2d_diferencias_finitas.py](edp/laplace_2d_diferencias_finitas.py) | Laplace 2D: bordes superior e izquierdo a 100; esquema de cinco puntos con barridos Gauss–Seidel | Algoritmo propio |
| EDP | [laplace_2d_fourier.py](edp/laplace_2d_fourier.py) | Laplace en un cuadrado: borde superior a 100 y los otros tres a cero; diez modos de Fourier | Coeficientes simbólicos + evaluación numérica |
| Elementos finitos | [conduccion_barra_1d.py](elementos_finitos/conduccion_barra_1d.py) | Ensamblaje de cuatro elementos, temperatura prescrita y convección en el extremo | Ensamblaje propio + solución con NumPy |
| Fourier | [serie_fourier.py](fourier/serie_fourier.py) | Coeficientes y suma parcial de `exp(x)` en `[-pi, pi]` | Integración simbólica con SymPy |
| Aplicaciones | [masa_resorte_estatico.py](aplicaciones/masa_resorte_estatico.py) | Desplazamientos de equilibrio mediante `K x = W` | Inversa con SciPy |

## Cómo ejecutar los ejemplos

Desde la raíz del repositorio:

```bash
python sistemas_lineales/jacobi.py
python interpolacion/lineal.py
python edo/euler.py
python integracion/simpson_1_3.py
python sistemas_lineales/cramer.py
python edp/laplace_2d_diferencias_finitas.py
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

Las prioridades para ampliar el curso son **análisis de errores, un solucionador general de Gauss–Seidel para `Ax = b`, interpolación de Lagrange y Newton, Cholesky, QR, Heun y Runge–Kutta de cuarto orden**. Consulta la [lista completa de métodos pendientes](docs/metodos_pendientes.md), que también incluye extensiones a EDP, elementos finitos y análisis de señales.

Ya hay ejemplos de Euler, Simpson 1/3, Newton modificado, Cramer, conducción 1D por elementos finitos y soluciones de EDP. Gauss–Seidel está implementado dentro del barrido de la placa por diferencias finitas; todavía falta una función general para sistemas lineales. El ejemplo masa–resorte resuelve equilibrio estático; no implementa integración temporal de la dinámica.

## Documentación

- [Métodos pendientes y orden sugerido](docs/metodos_pendientes.md).
- [Limitaciones y verificación del código actual](docs/revision_tecnica.md).
- [Correspondencia entre nombres anteriores y rutas nuevas](docs/migracion.md).

La reorganización conserva el contenido de los 26 scripts de `main` revisados el 25 de octubre. Los nombres de archivo se unificaron en minúsculas, sin espacios ni acentos, y todos terminan en `.py`.
