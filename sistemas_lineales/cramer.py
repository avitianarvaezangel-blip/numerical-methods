import numpy as np

import matplotlib.pyplot as plt


def Cramer(A,b):
    
    f = A.shape[0]
    Det_A = np.linalg.det(A)
    x = np.zeros(f)
    
    if Det_A == 0:
        print("El sistema no tiene solucion unica")
    else:
        for j in range(f):
            Aj = np.copy(A)
            Aj[:,j] = b
            Det_Aj = np.linalg.det(Aj)
            x[j] = Det_Aj / Det_A
    return x
A1 = np.array([[2, 3, -1],[1, -4, 2],[3, 1, 1]]).astype(float)

b1  = np.array([5, -3, 4]).astype(float)

S = Cramer(A1, b1)

print("EL vector solucion es:")
print(S)

# Definimos el rango de valores
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)

# ecuaciones
Z1 = 2*X + 3*Y - 5
Z2 = (-X + 4*Y - 3) / 2
Z3 = 4 - 3*X - Y

# Creamos la figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficamos los planos
ax.plot_surface(X, Y, Z1, alpha=0.3, color='blue', label='Z1')
ax.plot_surface(X, Y, Z2, alpha=0.3, color='red', label='Z2')
ax.plot_surface(X, Y, Z3, alpha=0.3, color='yellow', label='Z3')

# Punto de intersección (solución)
ax.scatter(1, 1, 0, color='black', s=50, label="Solución")

# Etiquetas y título
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Regla de Cramer')
ax.legend()

plt.show()
            
            
