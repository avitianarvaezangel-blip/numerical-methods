# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 14:15:43 2026

@author: AVITIA
"""

import numpy as np 

import matplotlib.pyplot as plt

def B(f, xl, xu, tol = 1e-10, itmax = 100):
    
    if f(xl)*f(xu) > 0:
        print("la raiz no esta en el intervalo")
        return None
    
    for i in range(itmax):
        xr = (xl + xu)/2 
        fxr = f(xr)
        
        if abs(fxr) < tol or abs(xu - xl)/2 < tol:
           return xr, i + 1 
        
        if f(xl) * fxr < 0:
            xu = xr
        else:
            
            xl = xr 
            
    return xr, itmax

def f(x):
    return np.exp(x) - np.log(x) - 3 

R, It = B(f,1,2)

print("Raiz aprox =", R)

print("Iteraciones", It)

print("f(xr) =", f(R))


xi = np.linspace(0.5, 1.5, 100)

x = [R]

y = [0]

fxi = f(xi)

plt.plot(xi, fxi, label='f(x) = e**x - ln(x) - 3')

plt.axhline(0, color='k')

plt.scatter(x, y, color='r')

plt.legend()

plt.title("Metodo de Biseccion")

plt.grid()