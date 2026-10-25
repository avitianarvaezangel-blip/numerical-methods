# Métodos numéricos con Python

Ejemplos didácticos de métodos numéricos y matemáticas aplicadas a la ingeniería, con cálculos paso a paso, tablas, gráficas y animaciones.

**Autor:** Ángel A. Avitia N.

El repositorio contiene **20 scripts**, organizados en nueve áreas. Algunos desarrollan el algoritmo con ciclos y operaciones elementales; otros muestran aplicaciones de NumPy, SciPy o SymPy. El índice distingue ambos casos. Inventario actualizado el **25 de octubre de 2026**.

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
| [raices](raices/) | Ecuaciones no lineales de una variable | 5 |
| [sistemas_lineales](sistemas_lineales/) | Métodos directos e iterativos | 5 |
| [interpolacion](interpolacion/) | Interpolación con SciPy | 2 |
| [diferenciacion](diferenciacion/) | Diferencias finitas | 1 |
| [integracion](integracion/) | Cuadratura numérica | 3 |
| [edo](edo/) | Ecuaciones diferenciales ordinarias | 1 |
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
| Raíces | [secante.py](raices/secante.py) | Método de la secante | Algoritmo propio + SymPy |
| Raíces | [punto_fijo.py](raices/punto_fijo.py) | Iteración `g(x) = exp(-x)` | Algoritmo propio |
| Sistemas lineales | [eliminacion_gaussiana.py](sistemas_lineales/eliminacion_gaussiana.py) | Eliminación y sustitución hacia atrás | Algoritmo propio |
| Sistemas lineales | [gauss_jordan.py](sistemas_lineales/gauss_jordan.py) | Reducción de la matriz aumentada | Algoritmo propio |
| Sistemas lineales | [factorizacion_lu.py](sistemas_lineales/factorizacion_lu.py) | LU con diagonal unitaria de L y solución de `Ax = b` | Algoritmo propio |
| Sistemas lineales | [matriz_inversa.py](sistemas_lineales/matriz_inversa.py) | Inversa mediante operaciones elementales | Algoritmo propio |
| Sistemas lineales | [jacobi.py](sistemas_lineales/jacobi.py) | Jacobi con tabla y errores porcentuales | Algoritmo propio |
| Interpolación | [lineal.py](interpolacion/lineal.py) | Interpolación lineal de `ln(x)` | `scipy.interpolate.interp1d` |
| Interpolación | [cuadratica.py](interpolacion/cuadratica.py) | Interpolación cuadrática de `ln(x)` | `scipy.interpolate.interp1d` |
| Diferenciación | [diferencias_finitas.py](diferenciacion/diferencias_finitas.py) | Primera derivada de `exp(x)*sin(x)`: diferencias hacia adelante, atrás y centrada | Algoritmo propio + SymPy |
| Integración | [trapecio.py](integracion/trapecio.py) | Trapecio compuesto con refinamiento uniforme, tabla y errores | Algoritmo propio |
| Integración | [simpson_1_3.py](integracion/simpson_1_3.py) | Simpson 1/3 compuesto con refinamiento uniforme, tabla y errores | Algoritmo propio |
| Integración | [simpson_3_8.py](integracion/simpson_3_8.py) | Regla compuesta de Simpson 3/8 | Algoritmo propio |
| EDO | [euler.py](edo/euler.py) | Euler explícito para `y' = (x**2 - 1)/y**2`, con comparación analítica | Algoritmo propio |
| Fourier | [serie_fourier.py](fourier/serie_fourier.py) | Coeficientes y suma parcial de `exp(x)` en `[-pi, pi]` | Integración simbólica con SymPy |
| Aplicaciones | [masa_resorte_estatico.py](aplicaciones/masa_resorte_estatico.py) | Desplazamientos de equilibrio mediante `K x = W` | Inversa con SciPy |

## Cómo ejecutar los ejemplos

Desde la raíz del repositorio:

```bash
python sistemas_lineales/jacobi.py
python interpolacion/lineal.py
python edo/euler.py
python integracion/simpson_1_3.py
```

Los datos del problema se editan dentro de cada archivo. Los scripts conservan su desarrollo didáctico original y ejecutan sus ejemplos al cargarse; todavía no constituyen una biblioteca con una interfaz común.

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

Las prioridades para ampliar el curso son **análisis de errores, Gauss–Seidel, interpolación de Lagrange y Newton, Cholesky, QR, Heun y Runge–Kutta de cuarto orden**. **Euler y Simpson 1/3 ya están implementados.** Consulta la [lista completa de métodos pendientes](docs/metodos_pendientes.md), que también incluye extensiones a EDP, elementos finitos y análisis de señales.

Gauss–Seidel aparecía en el README anterior, pero no se encontró su implementación. El ejemplo masa–resorte resuelve equilibrio estático; no implementa integración temporal de la dinámica.

## Documentación

- [Métodos pendientes y orden sugerido](docs/metodos_pendientes.md).
- [Limitaciones y verificación del código actual](docs/revision_tecnica.md).
- [Correspondencia entre nombres anteriores y rutas nuevas](docs/migracion.md).

La reorganización conserva el contenido de los 20 scripts de `main` revisados el 25 de octubre. Los nombres de archivo se unificaron en minúsculas, sin espacios ni acentos, y todos terminan en `.py`.
