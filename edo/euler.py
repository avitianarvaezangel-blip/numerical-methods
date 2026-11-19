import numpy as np
import matplotlib.pyplot as plt

def g(x):
    return  (x**3 - 3*x + 8)**(1/3)

xi = np.linspace(0, 2,100)


def f(x,y):
    return (x**2 - 1)/y**2


def Euler(f,x0,y0,h,n):
    
    x = np.zeros(n + 1)
    y = np.zeros(n + 1)
    
    x[0] = x0
    y[0] = y0
    
    for i in range(n):
        x[i + 1] = x[i] + h
        y[i + 1] = y[i] + f(x[i], y[i])*h
        
    return x,y

n = 10

X,Y = Euler(f, 0, 2, 0.2, n)

et = abs((g(X) - Y)/g(X))*100

print("et =",et)

print("x = ",X)

print("y = ",Y)


plt.plot(xi, g(xi), color='b',label='S. Exacta')

plt.plot(X, Y, color='r', label='M.Euler')

plt.scatter(X, Y, color='r')

plt.title("Metodo de Euler")

plt.xlabel("x")

plt.ylabel("f(x)")

plt.grid()

plt.legend()
