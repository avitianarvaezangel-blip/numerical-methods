import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


# parametros de entrada

x0 = 0

n1 = 1

n3 = 3

n5 = 5

n7 = 7

# funcion simbolica

x = sp.Symbol('x')

f = sp.exp(- x**2)

p1 = sp.exp(- x**2).series(x,x0,n1).removeO()

p3 = sp.exp(- x**2).series(x,x0,n3).removeO()

p5 = sp.exp(- x**2).series(x,x0,n5).removeO()

p7 = sp.exp(- x**2).series(x,x0,n7).removeO()

print("f(x) = ", f)

print("P1(x) =",p1)

print("P3(x) =",p3)

print("P5(x) =",p5)

print("P7(x) =",p7)

# de numerico a simbolico

fn = sp.lambdify(x, f , 'numpy')

p1n = sp.lambdify(x, p1 , 'numpy')

p3n = sp.lambdify(x, p3 , 'numpy')

p5n = sp.lambdify(x, p5, 'numpy')

p7n = sp.lambdify(x, p7, 'numpy')

# intervalo de la grafica

xi = np.linspace(-2, 2, 101)

fxi = fn(xi)

p1xi = p1n(xi)

p3xi = p3n(xi)

p5xi = p5n(xi)

p7xi = p7n(xi)

# x's

x1 = 10/3

x2 = 1/2

fx1 = fn(x1)

fx2 = fn(x2)

print("f(x1) = ", fx1)

print("f(x2) = ", fx2)

Int = sp.integrate(p7, (x, 0, 2))

Intf = sp.integrate(f, (x, 0, 2))

print("Integral aprox =", Int)

print("Integral Exac =", Intf)

# grafica

plt.plot(xi, fxi , label='f(x) = e^(- x^2)')

plt.plot(xi, p3xi, label='P3(x) = 1 - x^2')

plt.plot(xi, p5xi, label='P5(x) = 1 - x^2 + x^4/2')

plt.plot(xi, p7xi, label='P7(x) = 1 - x^2 + x^4/2 -x^6/6')

plt.axhline(y=0, color='k')


plt.title('Serie de Taylor')

plt.xlabel('x')

plt.ylabel('f(x)')

plt.legend()

plt.grid()