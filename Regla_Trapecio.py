import numpy as np
import sympy as sp
import matplotlib.pyplot as plt 

# # Variable y función simbólicas
x = sp.symbols('x')

f = 2 * x * sp.exp(-x**2) + x**3

# Limetes de Integracion
x0 = 0 

xn = 5

# Iteracion Maxima
ItMax = 200

# Integral Exacta
I = sp.integrate(f , (x, x0, xn)).evalf()

# Funcion numerica
fn = sp.lambdify(x, f, 'numpy')

def R_Trapecio(f, x0, xn, I, ItMax):
    
    # Inicio con un trapecio
    n = 1
    
    # Inicio de lista vacia
    A = [("n", "I", "et", "ea")]
    
    # Inicio del valor anterior en cero
    S_a = 0
    
    for j in range(ItMax):
        
        # Paso
        h = (xn - x0)/n
        
        # Inicio de Sumatoria 
        
        S = f(x0) + f(xn)
    
        for i in range(1, n):
            
            # Caso para un trapecio
            if n == 1:
                
                return (h/2)*S
            
            # Caso para mas de un trapecio
            
            else:
                
                # calculo de xi's
                
                xi = x0 + i*h
                
                # Suma de terminos 2*f(xi)
                
                S = S + 2*f(xi)
                
                
        for k in range(ItMax):
            
            et = abs((I - (h/2)*S)/I)*100
            
            #return et
                
        if S_a == 0:
            
            ea = np.nan
            
        else:
            
            ea = abs(((h/2)*S - S_a)/((h/2)*S))*100
                
        # Agregar a la lista los calculos de la integral aprox.
        A.append((round(n,1),round(float((h/2)*S), 6),round(et, 4),round(float(ea), 4)))
        
        # Actualzacion del valor anterior
        S_a = (h/2)*S
        
        # criterio de paro
        if ea < 1:
            
            break
                
        # Aumento en el numero de trapecios
        n = n + 1
        
        
    return(h/2)*S, A, n

# Integral aproximada con trapecios
It, A, n = R_Trapecio(fn, x0, xn, I, ItMax)

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
                 label=r'$\frac{h}{2} \left[ f(x_0) + 2 \sum_{i = 0}^{n - 1} f(x_i)  + f(x_n)\right]$')

plt.vlines(xin,0,  fn(xin),
           color='blue', lw=1.5)

plt.scatter(xin, fn(xin),
            color='blue', label=r'$f(x_i)$')

plt.plot(xin, fn(xin),
         color='blue', lw=1.5)

plt.title("Regla del Trapecio", fontsize=20)

plt.xlabel("x", fontsize=12)

plt.ylabel("f(x)", fontsize=12)

plt.legend(fontsize=12)

plt.grid()

plt.show()
