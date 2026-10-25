# Cambios de nombres y rutas

Correspondencia actualizada al 25 de octubre de 2026: los 20 scripts de `main` se distribuyen por tema y se renombran en minúsculas, sin espacios ni acentos. Se añade `.py` a los tres archivos que carecen de extensión. El contenido de los scripts se conserva; las funciones internas mantienen sus nombres anteriores.

| Ruta anterior | Ruta nueva |
| --- | --- |
| `Taylor_Exp.py` | [fundamentos/taylor_exponencial.py](../fundamentos/taylor_exponencial.py) |
| `Bisection.py` | [raices/biseccion.py](../raices/biseccion.py) |
| `Regla_Falsa` | [raices/regla_falsa.py](../raices/regla_falsa.py) |
| `Newton_Raphson.py` | [raices/newton_raphson.py](../raices/newton_raphson.py) |
| `M_secante.py` | [raices/secante.py](../raices/secante.py) |
| `punto_fijo.py` | [raices/punto_fijo.py](../raices/punto_fijo.py) |
| `Eliminacion_Gaussiana.py` | [sistemas_lineales/eliminacion_gaussiana.py](../sistemas_lineales/eliminacion_gaussiana.py) |
| `Gauss_Jordan.py` | [sistemas_lineales/gauss_jordan.py](../sistemas_lineales/gauss_jordan.py) |
| `Factorizacion_LU` | [sistemas_lineales/factorizacion_lu.py](../sistemas_lineales/factorizacion_lu.py) |
| `Matriz_Inversa.py` | [sistemas_lineales/matriz_inversa.py](../sistemas_lineales/matriz_inversa.py) |
| `Metodo_de_Jacobi.py` | [sistemas_lineales/jacobi.py](../sistemas_lineales/jacobi.py) |
| `Int_Lineal.py` | [interpolacion/lineal.py](../interpolacion/lineal.py) |
| `Int_Cuadratica.py` | [interpolacion/cuadratica.py](../interpolacion/cuadratica.py) |
| `Diferenciación_numérica.py` | [diferenciacion/diferencias_finitas.py](../diferenciacion/diferencias_finitas.py) |
| `Regla_Trapecio.py` | [integracion/trapecio.py](../integracion/trapecio.py) |
| `Simpson3_8.py` | [integracion/simpson_3_8.py](../integracion/simpson_3_8.py) |
| `Simpson_1_3.py` | [integracion/simpson_1_3.py](../integracion/simpson_1_3.py) |
| `Metodo_de_Euler` | [edo/euler.py](../edo/euler.py) |
| `S_Fourier.py` | [fourier/serie_fourier.py](../fourier/serie_fourier.py) |
| `Sistema Masa-Resorte.py` | [aplicaciones/masa_resorte_estatico.py](../aplicaciones/masa_resorte_estatico.py) |

El nombre más antiguo `Diferenciación numérica.py` también corresponde a `diferenciacion/diferencias_finitas.py`. Se conserva en esa ruta la versión más reciente de `main`, que usa `exp(x)*sin(x)`.

Actualiza cualquier acceso directo, comando `%run`, enlace o material de clase que use las rutas anteriores. Las nuevas rutas son relativas a la raíz del repositorio.
