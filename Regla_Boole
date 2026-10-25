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


def R_Boole(f, x0, xn,I, ItMax):

    # Inicio con 4 subintervalos
    n = 4
    
    # Inicio de lista
    A = [("n", "I", "et", "ea")]
    
    # Inicio de valor anterior en cero
    s_a = 0

    for j in range(ItMax):

        # Paso: n es multiplo de 3
        h = (xn - x0)/n

        # Inicio de sumatoria
        S = 7*f(x0) + 7*f(xn)

        for i in range(1, n):

            # Cálculo de xi
            xi = x0 + i*h

            if i % 2 != 0:

                # Suma de términos con índice par
                S = S + 32*f(xi)

            elif i % 4 != 0:

                # Suma de términos con índice impar
                S = S + 12*f(xi)
                
            else:
                
                S = S + 14*f(xi)

        for k in range(ItMax):
            
            et = abs((I - (2*h/45)*S)/I)*100
            
            
        if s_a == 0:
            
            ea = np.nan
            
        else:
            
            ea = abs(((2*h/45)*S - s_a)/((2*h/45)*S))*100
            
    
            
        A.append((round(n,1),round(float((2*h/45)*S), 6),round(et, 4),round(float(ea), 4)))
        
        # Actualizar 
        s_a = (2*h/45)*S
        
        if ea < 0.001:
            
            break

        # Aumento en el número de subintervalos
        n = n + 4

    return (2*h/45)*S, A,n

Is, A, n = R_Boole(fn, x0, xn, I, ItMax)

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
                 color='green', alpha=0.5
                 ,label="Regla de Boole")

plt.vlines(xin,0,  fn(xin),
           color='blue', lw=1.5)

plt.scatter(xin, fn(xin),
            color='blue', label=r'$f(x_i)$')

plt.plot(xin, fn(xin),
         color='blue', lw=1.5)

plt.title("Regla de Boole", fontsize=20)

plt.xlabel("x", fontsize=12)

plt.ylabel("f(x)", fontsize=12)

plt.legend(fontsize=10)

plt.grid()

plt.show()
