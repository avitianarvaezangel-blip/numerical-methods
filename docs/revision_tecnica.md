# Revisión técnica del código existente

## Cuarta derivada: incorporación del 2 de noviembre de 2026

Se añadió [cuarta_derivada.py](../diferenciacion/cuarta_derivada.py) con el mismo formato del programa de tercera derivada: `exp(x)*sin(x)`, derivada analítica con SymPy, seis funciones explícitas, 100 puntos en `[0,2]`, h = 0.1, tabla de errores absolutos máximos y gráfica con las fórmulas en la leyenda. La referencia analítica es `-4*exp(x)*sin(x)`.

| Fórmula | Orden de truncamiento |
| --- | --- |
| Adelante, 5 puntos | O(h) |
| Adelante, 6 puntos | O(h²) |
| Atrás, 5 puntos | O(h) |
| Atrás, 6 puntos | O(h²) |
| Centrada, 5 puntos | O(h²) |
| Centrada, 7 puntos | O(h⁴) |

**Errata de la imagen de referencia:** en la centrada de siete puntos aparece `+39*f(x_i+h)`; debe ser `-39*f(x_i+h)`. Con el signo positivo, la suma de coeficientes es 78, de modo que la fórmula devolvería `13/h**4` para la función constante 1, cuya cuarta derivada es cero. La fórmula implementada usa los coeficientes `[-1,12,-39,56,-39,12,-1]/6` sobre los desplazamientos `[-3,-2,-1,0,1,2,3]`, divididos entre h⁴. La corrección también está señalada junto a la función.

Las seis fórmulas pasaron la verificación simbólica sobre monomios hasta el grado correspondiente a su orden y reprodujeron la cuarta derivada de una cuártica. Al reducir h de 0.1 a 0.05 con `exp(x)`, los órdenes observados fueron aproximadamente 1.081, 2.130, 0.924, 1.876, 2.001 y 4.004, en el orden de la tabla. Los coeficientes de la centrada de siete puntos se contrastaron además con los pesos de diferencias finitas generados por SymPy.

Se verificaron la derivada analítica, la evaluación vectorizada y la generación de la gráfica; se inspeccionó la imagen para comprobar que las seis fórmulas sean visibles. Las expresiones suponen paso uniforme no nulo y una función suficientemente suave, definida en los puntos desplazados. La división entre h⁴ amplifica el efecto del redondeo cuando h es demasiado pequeño. Los 30 programas anteriores permanecen sin cambios.

## Tercera derivada: incorporación del 2 de noviembre de 2026

Se añadió [tercera_derivada.py](../diferenciacion/tercera_derivada.py) junto a los otros programas de diferenciación. Mantiene la estructura de los ejemplos: función simbólica, derivada analítica con SymPy, funciones numéricas, fórmulas explícitas, evaluaciones y gráfica comparativa. Usa `exp(x)*sin(x)`, una malla de 100 puntos en `[0,2]` y h = 0.1. Imprime el error absoluto máximo de cada aproximación.

| Fórmula | Orden de truncamiento |
| --- | --- |
| Adelante, 4 puntos | O(h) |
| Adelante, 5 puntos | O(h²) |
| Atrás, 4 puntos | O(h) |
| Atrás, 5 puntos | O(h²) |
| Centrada, 4 puntos | O(h²) |
| Centrada, 6 puntos | O(h⁴) |

Se verificó simbólicamente la exactitud de cada fórmula sobre todos los monomios hasta el grado correspondiente a su orden. Se comprobó el signo con la tercera derivada de una cúbica y el orden de convergencia al reducir h de 0.1 a 0.05 usando `exp(x)`: los órdenes observados fueron aproximadamente 1.062, 2.105, 0.942, 1.899, 2.001 y 4.002, en el orden de la tabla. También se comprobó la derivada analítica, la evaluación vectorizada y la generación de la gráfica; se inspeccionó la imagen para verificar que las seis fórmulas de la leyenda sean visibles.

Las fórmulas suponen un paso uniforme no nulo y una función suficientemente suave, definida en todos los puntos desplazados. Los órdenes de truncamiento describen el comportamiento al reducir h antes de que predomine el redondeo; en las fórmulas de tercera derivada se divide entre h³. Los 29 programas anteriores permanecen sin cambios y conservan las verificaciones registradas a continuación.

## Revisión de los 29 programas anteriores

Revisión actualizada el 25 de octubre de 2026, sobre los 29 scripts recibidos en `main`, commit `a71389fd173e620d8799a4cb98ff50ddb60f342e`. Incluye los nuevos ejemplos de segunda derivada y derivadas parciales, junto con los métodos, EDP y elementos finitos ya organizados.

## Alcance de la reorganización

Se conservó el contenido de los scripts y se cambiaron sus rutas. Se añadieron un índice, instrucciones de ejecución, dependencias y un plan de métodos pendientes. Las limitaciones descritas aquí pertenecen al código original y siguen pendientes de corrección.

## Verificación realizada

- Se conservan los resultados de los **27 ejemplos sin cambios** respecto de la actualización anterior, ejecutados el 25 de octubre con Matplotlib/Agg. Entre ellos se comprobaron raíces, sistemas lineales, interpolación, diferenciación, cuadraturas, Euler, Taylor, Fourier, EDP y la barra por elementos finitos.
- Se ejecutaron los **dos ejemplos nuevos de diferenciación**, también con Matplotlib/Agg: **2/2 completados sin excepciones**. Se verificaron sus fórmulas, la comparación con derivadas analíticas y la reducción del error al disminuir el paso. Se dibujaron también la figura de segunda derivada y las ocho superficies de derivadas parciales con el backend Agg.
- En la revisión de integración se comprobó exactitud para todos los monomios hasta grado uno en trapecio, tres en Simpson 1/3 y 3/8, y cinco en Boole, con error numérico máximo menor que `1e-12`. Sus archivos permanecen sin cambios en esta actualización.
- El residuo del sistema reducido de la barra fue aproximadamente `4.44e-15`; las series de calor y Laplace satisfacen sus respectivas EDP de forma simbólica. Para la placa por diferencias finitas se midió el residuo del esquema, que se detalla más adelante; completar 500 barridos no implica alcanzar cualquier tolerancia.
- En las cuatro cuadraturas se verificó también que, al detenerse por tolerancia en los ejemplos actuales, `n` coincide con la última fila del historial y la gráfica usa `n + 1` nodos. Se comprobó por separado la salida cuando `ItMax = 1`; ese caso mantiene una inconsistencia que se describe más adelante.
- Para Euler, comprobación de la malla y de resultados finitos del ejemplo; también se verificó la reducción de error de primer orden al reducir el paso en `y' = y`, `y(0) = 1`.
- Para diferenciación, exactitud de la fórmula centrada sobre una cuadrática y menor error máximo que la fórmula hacia adelante en el ejemplo actual.
- Para segunda derivada, las tres fórmulas reproducen la derivada de una cuadrática. En `exp(x)*sin(x)`, al reducir h de 0.1 a 0.05, el error máximo de la centrada se redujo por un factor aproximado de 3.9991; los factores de las fórmulas hacia adelante y atrás fueron aproximadamente 2.0794 y 1.9198.
- Para derivadas parciales, las seis funciones reproducen las derivadas de una función lineal y las centradas reproducen las de una cuadrática con término cruzado. En `sin(x) + sin(y)`, el error máximo de las centradas con h = 0.1 fue aproximadamente `0.00166449` en ambas direcciones y disminuyó por un factor de 3.9985 al usar h = 0.05.
- Conservación de los casos límite de raíces y sistemas lineales comprobados en las revisiones anteriores y detallados en la tabla siguiente. La observación sobre pasar un `n` inválido al antiguo Simpson 3/8 ya no aplica: su interfaz actual genera internamente múltiplos de tres.
- Comparación de los 29 scripts con sus archivos de origen en `main`: contenido idéntico byte por byte. Se verificaron también la sintaxis y los 77 enlaces locales de la documentación.

Estas comprobaciones respaldan la ejecución de los ejemplos concretos. No constituyen una validación general para cualquier problema ni una revisión visual de todas las gráficas o animaciones.

Resultados de los ejemplos actuales de integración de `2*x*exp(-x**2) + x**3` en `[0,5]`:

| Regla | Último n usado | Aproximación | Error relativo verdadero (%) |
| --- | ---: | ---: | ---: |
| Trapecio | 7 | 160.3487501663 | 1.97058834 |
| Simpson 1/3 | 14 | 157.2512907371 | 0.00082082 |
| Simpson 3/8 | 21 | 157.2505628299 | 0.00035792 |
| Boole | 16 | 157.2494110341 | 0.00037454 |

Los criterios de paro no son iguales: trapecio usa un error aproximado porcentual menor que 1 y las otras tres reglas menor que 0.001. Esta tabla describe los datos configurados; para comparar eficiencia deben igualarse las tolerancias. El error aproximado entre refinamientos no equivale al error verdadero.

Entorno usado:

| Componente | Versión |
| --- | --- |
| Python | 3.12.14 |
| NumPy | 2.3.5 |
| SciPy | 1.17.0 |
| SymPy | 1.14.0 |
| Matplotlib | 3.10.8 |
| pandas | 2.2.3 |
| IPython | 9.17.1 |

## Casos comprobados que requieren corrección

| Archivo o método | Entrada | Comportamiento observado | Corrección pendiente |
| --- | --- | --- | --- |
| Gauss, Gauss–Jordan e inversa | `A = [[0,1,0],[0,0,1],[1,0,0]]`; para el sistema, `b = [1,2,3]` | Declaran que no hay solución única, aunque `det(A) = 1` | Buscar en todas las filas candidatas antes de declarar singularidad; incorporar pivoteo parcial |
| LU | `A = [[0,1],[1,1]]`, `b = [1,2]` | El intercambio de filas produce una L incorrecta y una solución no finita; la solución correcta es `[1,1]` | Implementar una permutación consistente de A y b, y permutar solamente las columnas ya calculadas de L |
| Bisección | `f(x) = x`, intervalo `[0,1]` | Devuelve aproximadamente `0.99999999994`, aunque la raíz es el extremo izquierdo `0` | Comprobar raíces en ambos extremos antes de iterar |
| Bisección y regla falsa | `f(x) = x**2 + 1`, intervalo `[-1,1]` | Devuelven dos elementos en lugar de los tres que espera el ejemplo | Uniformar la salida de error o lanzar una excepción descriptiva; un intervalo sin cambio de signo no descarta raíces en general |
| Jacobi | `A = [[1,2],[0.1,1]]`, `b = [3,1.1]`, `x0 = [0,0]` | Rechaza el problema por falta de dominancia diagonal estricta; el radio espectral de la matriz de iteración es aproximadamente `0.4472` | Tratar la dominancia estricta como condición suficiente; permitir otros casos con controles de convergencia |
| Newton modificado | Pasar `f = x**2 - 2` con `x0 = 1`, manteniendo el ejemplo global | Devuelve `-1`, que no es raíz de la función recibida; la función sobrescribe el argumento con `fx` global | Respetar el parámetro `f`; comprobar el residuo antes de terminar por denominador pequeño |
| Cramer | `A = [[1,2],[2,4]]`, `b = [1,2]` | Imprime que no hay solución única, pero devuelve `[0,0]`, cuyo residuo máximo es `2` | Devolver un estado de fallo o lanzar una excepción, en lugar de presentar ceros como solución |
| Barra MEF | Datos actuales, cuatro elementos y cinco nodos | La solución nodal es `[100,85.9375,71.875,57.8125,43.75]`, pero la gráfica añade `Ta5 = 10` como sexta muestra | Graficar únicamente los cinco nodos y representar la temperatura ambiente como condición externa |
| Las cuatro cuadraturas | `ItMax = 1` | Trapecio, Simpson 1/3, Simpson 3/8 y Boole devuelven respectivamente `n = 2,4,6,8`, aunque el cálculo usó `n = 1,2,3,4` | Devolver el último n usado y un estado que indique si se alcanzó la tolerancia o el máximo de iteraciones |

Para los tres primeros métodos directos, la solución del sistema de la primera fila de la tabla es `[3,1,2]`. La matriz tiene un pivote válido en una fila posterior a la primera candidata examinada.

## Observaciones de lectura del código

Estas observaciones se obtuvieron al inspeccionar los scripts y conviene atenderlas al generalizar las funciones:

- **Criterios de paro y casos singulares.** Unificar tolerancias, máximo de iteraciones, residuo y estado de convergencia. Validar pivotes y denominadores, no solo los datos del ejemplo. Newton y secante pueden devolver `None`, aunque sus llamadas de demostración esperan dos resultados.
- **Jacobi.** La función exige una solución de referencia para elaborar la tabla. Conviene hacerla opcional y tratar por separado el error cuando una componente de referencia vale cero. El error aproximado también necesita cuidado si la iteración nueva contiene ceros.
- **LU y otros métodos directos.** Intercambiar filas solo cuando el pivote es exactamente cero no implementa pivoteo parcial. Conviene elegir el pivote por magnitud y comprobar el residuo de la solución.
- **Primera derivada (`diferencias_finitas.py`).** El ejemplo calcula aproximaciones vectorizadas de la derivada de `exp(x)*sin(x)`. Las leyendas de las curvas `DFC` y `DFAt` están intercambiadas: la centrada lleva la fórmula hacia atrás y viceversa. Esta observación corresponde únicamente al archivo de primera derivada.
- **Segunda derivada y parciales.** Los nuevos archivos comparan fórmulas hacia adelante, atrás y centradas con una referencia simbólica. La segunda derivada usa `exp(x)*sin(x)`; el ejemplo de parciales usa `sin(x) + sin(y)` y presenta ocho superficies. El paso de diferenciación se define explícitamente y puede ser distinto del espaciado de los puntos usados para dibujar.
- **Cuadraturas con refinamiento.** Las cuatro requieren la integral de referencia `I` para calcular el error verdadero; conviene hacerla opcional y tratar la referencia cero. El ciclo interno sobre `k` repite el mismo cálculo de error sin cambiar la aproximación. El incremento de n se hace después del criterio de paro: al converger se devuelve el n correcto, pero al agotar el máximo se devuelve el de la siguiente malla. También conviene validar que `ItMax` sea positivo y hacer configurable la tolerancia.
- **Boole.** Los pesos de la fórmula compuesta y el incremento de cuatro subintervalos pasaron las pruebas polinómicas. El comentario que indica que n es múltiplo de tres debe decir múltiplo de cuatro; algunos comentarios de paridad también están invertidos.
- **Área sombreada de Simpson y Boole.** `fill_between` sobre los nodos une los puntos mediante segmentos rectos. Ese sombreado representa trapecios, aunque el resultado numérico se obtiene con Simpson o Boole; para ilustrar esas reglas deben dibujarse sus interpolantes por bloques.
- **Euler.** El integrador explícito escalar ya está implementado. Conviene validar paso y número de pasos, separar la referencia analítica del método y ampliar después a sistemas de EDO. El ejemplo concreto requiere evitar `y = 0` por el denominador de su ecuación.
- **Newton modificado.** El ejemplo de `(x + 1)**3` alcanza la raíz `-1`; el problema de reutilización aparece al pasar otra función. Conviene unificar también su salida y criterio de convergencia con los otros métodos de raíces.
- **Cramer.** El ejemplo configurado satisface `A1 @ S = b1` con residuo máximo aproximado de `1.78e-15`. La comprobación `det(A) == 0` y el vector de ceros devuelto en ese caso no ofrecen un manejo general de matrices singulares o casi singulares. El punto dibujado está fijado en el código y debería depender de la solución calculada.
- **Laplace por diferencias finitas.** La actualización en el mismo arreglo es un barrido Gauss–Seidel del esquema de cinco puntos. Después de 500 barridos sobre 100×100 nodos interiores, el máximo de `abs(u_ij - promedio_de_vecinos)` fue aproximadamente `0.0349346`. Falta un criterio de paro por residuo, además de un máximo de barridos. Este residuo corresponde al promedio de vecinos sin dividir por el paso de malla al cuadrado.
- **Condiciones de frontera de las placas.** El ejemplo por diferencias finitas prescribe 100 en los bordes superior e izquierdo, mientras que la serie de Fourier prescribe 100 solo arriba. Deben igualarse dominio, fronteras y orientación antes de comparar ambos resultados.
- **Series truncadas de EDP.** El calor usa cinco modos y la placa diez. Las fronteras e inicio constantes se aproximan mediante esas sumas; no se debe exigir que la suma truncada reproduzca exactamente el dato discontinuo en los extremos. Por ejemplo, la placa da aproximadamente `106.3054` en el punto medio del borde superior con diez modos, frente al dato de 100; conviene estudiar la convergencia al aumentar el número de modos.
- **Geometría de la barra MEF.** Cada matriz elemental usa `L = 10` en el denominador. Si L es la longitud de cada elemento, los cuatro elementos representan una longitud total de 40; si L pretende ser la longitud total de la barra, debe usarse la longitud elemental correspondiente. Conviene explicitar esa convención y usar coordenadas nodales en la gráfica.
- **Taylor.** En `series(x, x0, n)`, el parámetro `n` es el orden del término de resto. En este ejemplo los polinomios llamados P3, P5 y P7 tienen grados 2, 4 y 6; conviene distinguir orden de truncamiento y grado.
- **Gráficas y animaciones.** Algunos scripts omiten `plt.show()`, y el objeto HTML de una animación requiere una salida de notebook para verse. Las instrucciones del README explican cómo mostrarlos. También hay etiquetas de gráficas que conviene revisar.
- **Reutilización.** Los ejemplos se ejecutan al importar un archivo. Separar funciones y demostraciones bajo `if __name__ == "__main__":` facilitará su uso en otros programas y las pruebas automatizadas.

## Prioridad de mantenimiento

1. Corregir selección de pivotes y LU con permutaciones.
2. Corregir extremos de bisección y uniformar resultados de los métodos de raíces.
3. Corregir la salida de las cuadraturas al agotarse el máximo de iteraciones; generalizar el manejo de referencias y criterios de paro.
4. Respetar la función recibida en Newton modificado, manejar singularidad en Cramer y controlar el residuo de la placa.
5. Ajustar leyendas de diferenciación y representación de nodos y ambiente en la barra.
6. Separar funciones de ejemplos y añadir pruebas de los casos límite anteriores antes de ampliar la biblioteca.

Los métodos que aún no existen están separados en [metodos_pendientes.md](metodos_pendientes.md).
