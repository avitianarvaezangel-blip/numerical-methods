import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Variable y función simbólicas
x = sp.symbols('x')

f = 2*x*sp.exp(-x**2) + x**3

# Límites de integración
x0 = 0
xn = 5

# Iteraciones máximas
ItMax = 100

# Integral exacta
I = sp.integrate(f, (x, x0, xn)).evalf()

# Función numérica
fn = sp.lambdify(x, f, 'numpy')


def Simpson_1_3(f, x0, xn,I, ItMax):

    # Inicio con dos subintervalos
    n = 2
    
    # Inicio de lista
    A = [("n", "I", "et", "ea")]
    
    # Inicio de valor anterior en cero
    s_a = 0

    for j in range(ItMax):

        # Paso: n siempre es par
        h = (xn - x0)/n

        # Inicio de sumatoria
        S = f(x0) + f(xn)

        for i in range(1, n):

            # Cálculo de xi
            xi = x0 + i*h

            if i % 2 == 0:

                # Suma de términos con índice par
                S = S + 2*f(xi)

            else:

                # Suma de términos con índice impar
                S = S + 4*f(xi)

        for k in range(ItMax):
            
            et = abs((I - (h/3)*S)/I)*100
            
            
        if s_a == 0:
            
            ea = np.nan
            
        else:
            
            ea = abs(((h/3)*S - s_a)/((h/3)*S))*100
            
    
            
        A.append((round(n,1),round(float((h/3)*S), 6),round(et, 4),round(float(ea), 4)))
        
        # Actualizar 
        s_a = (h/3)*S
        
        # criterio de paro
        if ea < 0.001:
            
            break

        # Aumento en el número de subintervalos
        n = n + 2

    return (h/3)*S, A,n


Is, A, n = Simpson_1_3(fn, x0, xn, I, ItMax)

xi = np.linspace(x0, xn, 100)

A = np.array(A)

print(A)

xin = np.linspace(x0, xn, n + 1)


plt.plot(xi, fn(xi), 
         label=r'$f(x) = x^{3} + 2 x e^{- x^{2}}$',
         color='black', lw=3)

plt.axhline(0, color='gray')

plt.fill_between(xi, fn(xi), where=(xi >= x0) & (xi <= xn)
                 , color='red', alpha=0.5, 
                 label=r'$\int_{x_0}^{x_n} f(x) dx$')

plt.fill_between(xin, fn(xin), where=(xin >= x0) & (xin <= xn),
                 color='green', alpha=0.5, 
                 label=r'$\frac{h}{3} \left[ f(x_0) + 4 \sum_{i = impar}^{n - 1} f(x_i) + 2 \sum_{j = par}^{n - 2} f(x_j)  + f(x_n)\right]$')

plt.vlines(xin,0,  fn(xin),
           color='blue', lw=1.5)

plt.scatter(xin, fn(xin),
            color='blue', label=r'$f(x_i)$')

plt.plot(xin, fn(xin),
         color='blue', lw=1.5)

plt.title("Regla de Simpson 1/3", fontsize=20)

plt.xlabel("x", fontsize=12)

plt.ylabel("f(x)", fontsize=12)

plt.legend(fontsize=12)

plt.grid()

plt.show()
