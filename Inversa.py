# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 21:23:25 2025

@author: AVITIA
"""

import numpy as np
import matplotlib.pyplot as plt
# eliminacion gausiana
def E_GJ(A):

    # filas de A 
    f = A.shape[0] 
    
    for j in range(f):  
        if A[j, j] == 0:
            print("Existe un cero en la diagonal")
            break
        
        A[j, j:] = A[j, j:] / A[j, j] 

        for i in range(j + 1, f): 

            A[i, j:] = - A[j, j:]*A[i, j] + A[i, j:]


    return A


def E_A(U):
    
    f2 = U.shape[0]
    
    for j in range(f2 - 1, -1, -1):
          
        for i in range(j - 1, -1, -1):
            
            U[i, j:] = -  U[i, j]*U[j,j:] + U[i, j:]
            
    return U
            

M = np.array([[5, 3, -1, 1, 0, 0],[3, 2, -1, 0, 1, 0],[1, 1, 1, 0, 0, 1]]).astype(float)

U = E_GJ(M)

print("La matriz triangular reducida es:")
print(U)

X = E_A(U)
IN = X[:, -3:]
print("La inversa es:")
print(IN)

