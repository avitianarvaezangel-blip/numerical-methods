import numpy as np 
import sympy as sp
import matplotlib.pyplot as plt
 
# definir funcion 
def NR_RM(f,x0,tol = 1e-10,ItMax = 100):
    
    # simbolico
    x = sp.Symbol('x')
    f = fx
    df = f.diff(x)
    df2 = f.diff(x,2)
    
    # De simbolico a numerico
    f_n = sp.lambdify(x , f, "numpy")
    df_n = sp.lambdify(x, df, "numpy")
    df2_n = sp.lambdify(x , df2, "numpy")
    
    for i in range(ItMax):
         f_x = f_n(x0)
         df_x = df_n(x0)
         df2_x = df2_n(x0)
         
         
         D = (df_x)**2 - (f_x*df2_x)
         # denominador diferente de cero
         if abs(D) < 1e-12:
             print("Denominador es casi igual a cero en i =",i)
             print("se detiene antes de tener una division por cero")
             print(" la aproximada es:" ,x0)
             return x0 
         
         x1 = x0 - (f_x*df_x)/D
         #print("x = ",x1 , "f(x) = ", f_n(x1))
         
         if abs(x1-x0) < tol:
             print("la raiz aproximada es:",x1)
             return x1
         x0 = x1
         
    print("la raiz no converge")
    return x0

x = sp.Symbol('x')
fx = x**3 + 3*x**2 + 3*x + 1

NR_RM(fx, x0 = 0)

# grafica

# vector de valores
xi = np.linspace(-2, 0, 101)

# dericadas
df = fx.diff(x)
df2 = fx.diff(x,2)
# funciones numericas 
f_n = sp.lambdify(x , fx, "numpy")
df_n = sp.lambdify(x, df, "numpy")
df2_n = sp.lambdify(x , df2, "numpy")
# funciones evaluadas
fi = f_n(xi)
dxi = df_n(xi)
dxi2 = df2_n(xi)

print("f(x) = ", fx)
print("f'(x) = ",df)
print("f''(x) = ",df2)

# plots 
plt.plot(xi,fi, label='f(x) = x**3 + 3*x**2 + 3*x + 1')
plt.plot(xi,dxi, label="f'(x)' = 3*x**2 + 6*x + 3")
plt.plot(xi,dxi2, label='f''(x) = 6*(x + 1)')
# linea horizontal 
plt.axhline(0, color='black')
plt.plot(-1 ,0 ,marker='o', label="raiz: x = -1 ")


# titulo, cuadricula y leyendas
plt.title('Metodo de Newton-Raphson para raices multiples')
plt.legend()
plt.grid()
