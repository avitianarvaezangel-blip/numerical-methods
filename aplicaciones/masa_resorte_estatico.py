import numpy as np
from scipy import linalg

# constantes de riguidez
k1 = 10
k2 = 5
k3 = 15

# masas
m1 = 2
m2 = 3
m3 = 2.5
g = 9.81

# matriz de riguidez
K = np.array([[k1 + 2*k2, -2*k2, 0],[-2*k2, 2*k2 + k3, -k3],[0, -k3, k3]])
#print("K = ", K)

# vector de pesos
W = np.array([[m1*g],[m2*g],[m3*g]])
#print("W = ", W)

INV_K = linalg.inv(K)
#print("K^(-1) = ", INV_K)

X = INV_K @ W
#X = np.dot(INV_K, W)
print("X = ", X)