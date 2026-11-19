# Capítulo 10: problemas de valor inicial

Correspondencia con el índice de la imagen proporcionada. Se añadieron 19 programas a `edo`; [euler.py](../edo/euler.py) conserva su contenido. Los apartados 10.1 y 10.15 son antecedentes y problemas, respectivamente, y no designan métodos adicionales.

## Archivos por apartado

| Apartado | Programa | Implementación |
| --- | --- | --- |
| 10.2.1 Euler explícito | [euler.py](../edo/euler.py) | Ejemplo original: `y'=(x**2-1)/y**2`, `y(0)=2`. |
| 10.2.2 Error de Euler | [error_truncamiento.py](../edo/error_truncamiento.py) | Error local de un paso y orden observado al reducir h. |
| 10.2.3 Euler implícito | [euler_implicito.py](../edo/euler_implicito.py) | Resuelve la ecuación de cada paso con Newton y derivada respecto de y. |
| 10.3 Euler modificado | [euler_modificado.py](../edo/euler_modificado.py) | Heun explícito: promedio de la pendiente inicial y la pendiente predicha. |
| 10.4 Punto medio | [punto_medio.py](../edo/punto_medio.py) | RK2 explícito con evaluación en el punto medio. |
| 10.5.1 RK de segundo orden | [runge_kutta_2.py](../edo/runge_kutta_2.py) | Familia RK2 de dos etapas; Ralston por defecto, `alpha=2/3`. Con `alpha=1/2` reproduce punto medio y con `alpha=1`, Heun. |
| 10.5.2 RK de tercer orden | [runge_kutta_3.py](../edo/runge_kutta_3.py) | RK3 clásico de Kutta. |
| 10.5.3 RK de cuarto orden | [runge_kutta_4.py](../edo/runge_kutta_4.py) | RK4 clásico de cuatro etapas. |
| 10.6.1 Adams–Bashforth | [adams_bashforth.py](../edo/adams_bashforth.py) | Versión explícita AB4, de cuatro pasos y orden cuatro. |
| 10.6.2 Adams–Moulton | [adams_moulton.py](../edo/adams_moulton.py) | AM de orden cuatro: coeficientes `9,19,-5,1`, divididos entre 24; ecuación implícita resuelta con Newton. |
| 10.7 Predictor–corrector | [predictor_corrector.py](../edo/predictor_corrector.py) | AB4 como predictor y una corrección AM4, con esquema PECE. |
| 10.8.1 Sistemas con Euler | [euler_sistemas.py](../edo/euler_sistemas.py) | Euler explícito vectorial. |
| 10.8.2 Sistemas con RK2 modificado | [euler_modificado_sistemas.py](../edo/euler_modificado_sistemas.py) | Heun vectorial. |
| 10.8.3 Sistemas con RK4 | [runge_kutta_4_sistemas.py](../edo/runge_kutta_4_sistemas.py) | RK4 clásico vectorial. |
| 10.9 Orden superior | [edo_orden_superior.py](../edo/edo_orden_superior.py) | Reduce `y''+2*y'+2*y=0` a dos ecuaciones de primer orden y aplica RK4. |
| 10.10.1 Rutina para una EDO | [solve_ivp_escalar.py](../edo/solve_ivp_escalar.py) | Equivalente funcional en Python: `scipy.integrate.solve_ivp`, método RK45. |
| 10.10.2 Rutina para un sistema | [solve_ivp_sistemas.py](../edo/solve_ivp_sistemas.py) | RK45 adaptativo de SciPy para el sistema vectorial. |
| 10.11 Error local de RK2 | [error_truncamiento.py](../edo/error_truncamiento.py) | Incluye el error local de Heun, comparado con Euler. |
| 10.12 Paso para precisión deseada | [paso_adaptativo.py](../edo/paso_adaptativo.py) | RK4 con duplicación de pasos, estimación de error, aceptación y rechazo de pasos. |
| 10.13 Estabilidad | [estabilidad.py](../edo/estabilidad.py) | Factores de amplificación de Euler, Heun, RK4 y Euler implícito sobre el eje real negativo; comparación temporal. |
| 10.14 EDO rígidas | [edo_rigida.py](../edo/edo_rigida.py) | Ejemplo con dos escalas temporales: Euler explícito, Euler implícito y Radau adaptativo. |

El índice de la imagen no especifica todas las variantes de RK2 ni los órdenes de Adams. La tabla identifica las variantes implementadas. Los programas son ejemplos en Python; las dos secciones que mencionan MATLAB se cubren con SciPy.

## Formato y ejecución

Los ejemplos siguen la estructura de `euler.py`: funciones `f` y `g`, condición inicial, paso h, número de pasos n, función del método, arreglos X e Y, comparación con la solución exacta y gráfica. En los sistemas, Y tiene forma `(n+1, numero_de_ecuaciones)`. Los errores relativos se marcan como indefinidos cuando la referencia es cero; también se informa el error absoluto.

Desde la raíz del repositorio:

```bash
python edo/euler_implicito.py
python edo/runge_kutta_4.py
python edo/adams_moulton.py
python edo/runge_kutta_4_sistemas.py
python edo/paso_adaptativo.py
python edo/edo_rigida.py
```

Los métodos escalares de paso fijo mantienen la EDO del ejemplo original y usan h = 0.2, n = 10. Los tres métodos multipaso generan sus tres valores iniciales con RK4; no usan la solución analítica para arrancar. Si n es menor que cuatro, la salida solo contiene el arranque disponible. Los métodos de paso fijo implementados avanzan con h positivo.

## Interpretación de errores y estabilidad

- **Newton:** Euler implícito y Adams–Moulton detienen la iteración por residuo y comunican fallos de convergencia. La tolerancia no lineal es independiente del error de discretización de la EDO.
- **AM4 y PECE:** Adams–Moulton resuelve la ecuación implícita hasta tolerancia; predictor–corrector realiza una sola corrección y vuelve a evaluar la pendiente para el siguiente paso.
- **Error local:** se mide la diferencia entre el valor exacto después de un paso y el valor calculado desde una condición exacta, sin dividir entre h. Se espera orden dos para Euler y tres para RK2; sus órdenes globales son uno y dos.
- **Paso adaptativo:** compara un paso RK4 de longitud h con dos medios pasos y estima el error de estos últimos como `abs(y_dos_medios-y_un_paso)/15`. Controla `atol+rtol*max(abs(y_actual),abs(y_nueva))`; conserva la solución de dos medios pasos. El control local no certifica una cota global. El historial contiene únicamente pasos aceptados y se informa cuántos se rechazaron.
- **SciPy:** `t_eval` determina dónde se presentan los resultados; el paso interno de RK45 o Radau se adapta mediante sus tolerancias. Los programas verifican el estado de salida del solucionador.
- **Rigidez:** en `y'=-1000*(y-cos(x))-sin(x)`, `y(0)=0`, la solución es `cos(x)-exp(-1000*x)`. Con h = 0.01, Euler explícito tiene factor de amplificación de magnitud nueve. Euler implícito es estable, pero resuelve pobremente la capa inicial con ese paso; Radau permite tratarla con paso adaptativo. La gráfica del error muestra esta diferencia.

Estos ejemplos cubren los temas identificados en el índice suministrado. Las hipótesis de existencia, suavidad, convergencia y estabilidad dependen de la ecuación y del método; el ejemplo escalar requiere que y permanezca distinto de cero.
