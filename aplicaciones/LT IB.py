import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

t = sp.Symbol('t', positive=True)

s = sp.Symbol('s')

x = sp.Symbol('x', positive=True)

i1 = sp.Function('i1')

i2 = sp.Function('i2')

ED1 = sp.Eq(
    sp.diff(i1(t), t)
    + 2*i1(t)
    + 10*sp.Integral(i1(x), (x, 0, t))
    + 2*(i1(t) - i2(t))
    + 10*sp.Integral(i1(x) - i2(x), (x, 0, t)),
    10
)

ED2 = sp.Eq(
    sp.diff(i2(t), t)
    + 2*(i2(t) - i1(t))
    + 10*sp.Integral(i2(x) - i1(x), (x, 0, t)),
    0
)


#LEDi = sp.laplace_transform(
#    ED1.lhs, t, s, noconds=True).subs({i1(0): 0, i2(0): 0})

#sp.pprint(LEDi)

#LED1i = sp.laplace_transform(
#    ED1.lhs, t, s, noconds=True
#    ).subs({i1(0): 0, i2(0): 0})

#LED1d = sp.laplace_transform(
#    ED1.rhs, t, s, noconds=True
#    ).subs({i1(0): 0, i2(0): 0})

#print(LED1i)

#print(LED1d)

I1, I2 = sp.symbols('I1 I2')

condiciones = {i1(0): 0, i2(0): 0}

# Representar las transformadas de las corrientes
reglas = {
    sp.LaplaceTransform(i1(t), t, s): I1,
    sp.LaplaceTransform(i2(t), t, s): I2
}

# Propiedad: L{integral de f desde 0 hasta t} = F(s)/s
# SymPy puede separar las integrales en términos positivos y negativos.
for f, F in ((i1, I1), (i2, I2)):
    for signo in (1, -1):
        integral = sp.Integral(signo*f(x), (x, 0, t))
        reglas[sp.LaplaceTransform(integral, t, s)] = signo*F/s


def transformar(ecuacion):
    izq = sp.laplace_transform(
        ecuacion.lhs, t, s, noconds=True
    ).subs(condiciones)

    der = sp.laplace_transform(
        ecuacion.rhs, t, s, noconds=True
    )

    return sp.Eq(sp.expand(izq.xreplace(reglas)), der)


# Transformar ambas ecuaciones
LED1 = transformar(ED1)
LED2 = transformar(ED2)

print("Sistema en el dominio s:")
sp.pprint(LED1)
sp.pprint(LED2)

# Resolver el sistema lineal
sol_s = sp.solve([LED1, LED2], (I1, I2))

I1s = sp.factor(sol_s[I1])
I2s = sp.factor(sol_s[I2])

print("\nI1(s) =")
sp.pprint(I1s)

print("\nI2(s) =")
sp.pprint(I2s)

# Aplicar transformadas inversas
i1t = sp.simplify(sp.inverse_laplace_transform(I1s, s, t))
i2t = sp.simplify(sp.inverse_laplace_transform(I2s, s, t))

print("\ni1(t) =")
sp.pprint(i1t)

print("\ni2(t) =")
sp.pprint(i2t)

# Graficar las soluciones
f1 = sp.lambdify(t, i1t, 'numpy')
f2 = sp.lambdify(t, i2t, 'numpy')

T = np.linspace(0, 3, 1000)

plt.figure(figsize=(9, 5))
plt.plot(T, f1(T), label=r'$i_1(t)$', linewidth=2)
plt.plot(T, f2(T), '--', label=r'$i_2(t)$', linewidth=2)
plt.xlabel('Tiempo t (s)')
plt.ylabel('Corriente (A)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()


