import matplotlib.pyplot as plt
import numpy as np

n = 100

u = np.zeros((n + 2, n + 2 ))


u[0,:] = 100

u[:,0] = 100

It = 500

for k in range(It):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            
            u[i,j] = 0.25* (u[i+1,j] + u[i-1, j] + u[i, j+1] + u[i, j-1])
            
            
print("Distribución de temperatura:\n")
print(np.round(u, 2))

plt.figure(figsize=(3.5,3.5))

plt.imshow(u, cmap='jet', origin='upper',vmin=0,vmax=100)

plt.colorbar(label='Temperatura °C')

plt.title('Distribución de Temperatura')
plt.xlabel('x')
plt.ylabel('y')

