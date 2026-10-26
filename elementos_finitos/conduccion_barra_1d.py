import numpy as np
import matplotlib.pyplot as plt


h = 10/(12**2)

Kxx = 20/12

T1 = 100

Ta5 = 10

L = 10

r = 1

A = np.pi*(r**2)

Kc1 = (A*Kxx)/L * np.array([[1,-1]
                            ,[-1,1]
    ])

Khend = (h*A)* np.array([[0,0]
                         ,[0,1]
    ])

K1 = Kc1
K2 = Kc1
K3 = Kc1
K4 = Kc1 + Khend

def Ensamble(K_E):

    m = len(K_E)
    n = m + 1
    
    K = np.zeros((n, n))
    
    for i in range(m):
        K[i:i+2, i:i+2] += K_E[i]
    
    return K

K_E= np.array([K1, K2, K3, K4])

K = Ensamble(K_E)

F = np.zeros(5)

F[0] = T1

F[1] = K[0,0]*100

F[4] = h * A * Ta5

Km = K[1:,1:]

Fm = F[1:]


print("Km = ",Km)

print("Fm = ",Fm)


ink = np.linalg.inv(Km)

S = ink@Fm

print("S =" ,S)

S1 = np.zeros(len(S) + 2)

S1[0] = T1

S1[1:-1] = S

S1[-1] = Ta5

print("S =" ,S)

S1 = np.zeros(len(S) + 2)

S1[0] = T1

S1[1:-1] = S

S1[-1] = Ta5

print("S1 =", S1)

TC = np.array([S1])

plt.imshow(TC,cmap='jet')

plt.colorbar(label='Temperatura °C')

plt.yticks([])

plt.xlabel('X')

plt.title('Distribución de temperatura')
