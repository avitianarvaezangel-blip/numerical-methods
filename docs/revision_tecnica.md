# Revisión técnica del código existente

Revisión actualizada el 25 de octubre de 2026, sobre los 26 scripts de `main`, commit `642750b599618097bdcc2d6b9c5ccbd106e3cff5`. Incluye Newton modificado, Cramer, conducción 1D por elementos finitos y tres ejemplos de EDP, además de los métodos ya organizados.

## Alcance de la reorganización

Se conservó el contenido de los scripts y se cambiaron sus rutas. Se añadieron un índice, instrucciones de ejecución, dependencias y un plan de métodos pendientes. Las limitaciones descritas aquí pertenecen al código original y siguen pendientes de corrección.

## Verificación realizada

- Los **20 ejemplos de la actualización anterior** se ejecutaron el 25 de octubre con Matplotlib/Agg y completaron sus comprobaciones numéricas. Sus archivos permanecen idénticos en la nueva subida, por lo que esos resultados se conservan.
- Se ejecutaron los **seis ejemplos recién añadidos**, también con Matplotlib/Agg: **6/6 completados sin excepciones**. Se comprobó la raíz múltiple del ejemplo, el residuo de Cramer, el ensamblaje y balance de flujo de la barra, las fronteras de la placa por diferencias finitas y las ecuaciones de las dos series de Fourier.
- El residuo del sistema reducido de la barra fue aproximadamente `4.44e-15`; las series de calor y Laplace satisfacen sus respectivas EDP de forma simbólica. Para la placa por diferencias finitas se midió el residuo del esquema, que se detalla más adelante; completar 500 barridos no implica alcanzar cualquier tolerancia.
- Comprobaciones numéricas de raíces y sistemas, interpolación en los nodos, identidades de factorización e inversa, exactitud del trapecio para una función lineal y de Simpson 1/3 y 3/8 para una cúbica, y verificaciones de las expresiones de Taylor y Fourier.
- Para Euler, comprobación de la malla y de resultados finitos del ejemplo; también se verificó la reducción de error de primer orden al reducir el paso en `y' = y`, `y(0) = 1`.
- Para diferenciación, exactitud de la fórmula centrada sobre una cuadrática y menor error máximo que la fórmula hacia adelante en el ejemplo actual.
- Conservación de los casos límite comprobados el 18 de octubre y detallados en la tabla siguiente. Los scripts de raíces, sistemas lineales y Simpson 3/8 que presentan esos casos mantienen su contenido numérico.
- Comparación de los 26 scripts con sus archivos de `main`: contenido idéntico byte por byte. Se verificaron también la sintaxis y los 71 enlaces locales de la documentación.

Estas comprobaciones respaldan la ejecución de los ejemplos concretos. No constituyen una validación general para cualquier problema ni una revisión visual de todas las gráficas o animaciones.

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
| Simpson 3/8 | `f(x) = x**3`, intervalo `[0,1]`, `n = 4` | Acepta un número inválido de subintervalos y devuelve `0.21240234375`, frente a `0.25` | Exigir que `n` sea entero positivo y múltiplo de tres |
| Jacobi | `A = [[1,2],[0.1,1]]`, `b = [3,1.1]`, `x0 = [0,0]` | Rechaza el problema por falta de dominancia diagonal estricta; el radio espectral de la matriz de iteración es aproximadamente `0.4472` | Tratar la dominancia estricta como condición suficiente; permitir otros casos con controles de convergencia |
| Newton modificado | Pasar `f = x**2 - 2` con `x0 = 1`, manteniendo el ejemplo global | Devuelve `-1`, que no es raíz de la función recibida; la función sobrescribe el argumento con `fx` global | Respetar el parámetro `f`; comprobar el residuo antes de terminar por denominador pequeño |
| Cramer | `A = [[1,2],[2,4]]`, `b = [1,2]` | Imprime que no hay solución única, pero devuelve `[0,0]`, cuyo residuo máximo es `2` | Devolver un estado de fallo o lanzar una excepción, en lugar de presentar ceros como solución |
| Barra MEF | Datos actuales, cuatro elementos y cinco nodos | La solución nodal es `[100,85.9375,71.875,57.8125,43.75]`, pero la gráfica añade `Ta5 = 10` como sexta muestra | Graficar únicamente los cinco nodos y representar la temperatura ambiente como condición externa |

Para los tres primeros métodos directos, la solución del sistema de la primera fila de la tabla es `[3,1,2]`. La matriz tiene un pivote válido en una fila posterior a la primera candidata examinada.

## Observaciones de lectura del código

Estas observaciones se obtuvieron al inspeccionar los scripts y conviene atenderlas al generalizar las funciones:

- **Criterios de paro y casos singulares.** Unificar tolerancias, máximo de iteraciones, residuo y estado de convergencia. Validar pivotes y denominadores, no solo los datos del ejemplo. Newton y secante pueden devolver `None`, aunque sus llamadas de demostración esperan dos resultados.
- **Jacobi.** La función exige una solución de referencia para elaborar la tabla. Conviene hacerla opcional y tratar por separado el error cuando una componente de referencia vale cero. El error aproximado también necesita cuidado si la iteración nueva contiene ceros.
- **LU y otros métodos directos.** Intercambiar filas solo cuando el pivote es exactamente cero no implementa pivoteo parcial. Conviene elegir el pivote por magnitud y comprobar el residuo de la solución.
- **Diferenciación.** La versión actual calcula aproximaciones vectorizadas de la derivada de `exp(x)*sin(x)`. Las leyendas de las curvas `DFC` y `DFAt` están intercambiadas: la centrada lleva la fórmula hacia atrás y viceversa.
- **Trapecio y Simpson 1/3.** Ambos requieren la integral de referencia `I` para calcular el error verdadero; conviene hacerla opcional y tratar la referencia cero. El ciclo interno sobre `k` repite el mismo cálculo de error sin cambiar la aproximación. El valor `n` devuelto ya se incrementó después del último cálculo: en trapecio es un subintervalo mayor, y en Simpson 1/3 son dos. La gráfica de trapecio usa ese `n` incrementado, por lo que sus nodos no coinciden con el último cálculo; la de Simpson compensa el incremento mediante `n - 1` puntos.
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
3. Corregir el número de subintervalos devuelto por trapecio y Simpson 1/3; generalizar el manejo de referencias y criterios de paro.
4. Respetar la función recibida en Newton modificado, manejar singularidad en Cramer y controlar el residuo de la placa.
5. Ajustar leyendas de diferenciación y representación de nodos y ambiente en la barra.
6. Separar funciones de ejemplos y añadir pruebas de los casos límite anteriores antes de ampliar la biblioteca.

Los métodos que aún no existen están separados en [metodos_pendientes.md](metodos_pendientes.md).
