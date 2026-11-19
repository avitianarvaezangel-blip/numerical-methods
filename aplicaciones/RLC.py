import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

t = sp.Symbol('t')

q = sp.Function('q')

ED = sp.Eq(sp.diff(q(t), t, 2) 
           + 2* sp.diff(q(t) , t) 
           + 2* q(t), 10)

S = sp.dsolve(ED, q(t)
              , ics={q(0) : 0
              ,sp.diff(q(t), t).subs(t, 0) : 0})

# q(t) carga
Q = S.rhs

# q'(t) = i(t) corriente
i = sp.simplify(sp.diff(Q, t))

# vc(t)

Vc_t = 2*Q

print(sp.latex(sp.simplify(Vc_t)))


# i(t) numerica
i_n = sp.lambdify(t, i)

# vc(t) numerica

vcn = sp.lambdify(t, Vc_t)

# intervalo de tiempo
ti = np.linspace(0, 5, 100)

q_0 = 0 

dq_0 = 0

vc_0 = 0

n = 25

def Euler(q_0, dq_0, vc_0, n):
    
    h = 0.2
    
    t = np.zeros(n + 1)
    
    i = np.zeros(n + 1)
    
    vc = np.zeros(n + 1)
    
    t[0] = 0
    
    i[0] = dq_0
    
    vc[0] = vc_0
    
    for j in range(n):
        
        t[j + 1] = t[j] + h
        
        # y_i+1 = y_i + f(x_i, y_i)*h
        i[j + 1] = i[j] + (10 - 2*i[j] -vc[j])*h
        
        vc[j + 1] = vc[j] + (2*i[j])*h
        
    return t, i, vc
        
#print(i)

plt.plot(ti, i_n(ti), label=r'$i(t) = 10 e^{- t} \sin{\left(t \right)}$')

plt.plot(ti , vcn(ti), label=r'$v_c (t) = 10 - 10 \sqrt{2} e^{- t} \sin{\left(t + \frac{\pi}{4} \right)}$')

T, I, VC = Euler(q_0, dq_0, vc_0, n)


plt.plot(T, I, color='r', label=r'$i_{k + 1} = i_k + (10 - 2 i_k - v_{c,k})h$')

plt.plot(T, VC, label=r'$v_{c, k + 1} = v_{c,k} + 2 i_k h$', color='g')

plt.scatter(T, I, color='r')

plt.scatter(T, VC, color='g')

plt.legend(fontsize=12)

plt.xlabel("t [s]")

plt.ylabel("i(t) [A]")

plt.grid(0.7)

plt.title("Circuito RLC", fontsize=20)


