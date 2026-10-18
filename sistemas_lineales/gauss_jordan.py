import numpy as np
import matplotlib.pyplot as plt

# Matriz de coeficientes
A = np.array([
    [ 2,  1, -1],
    [-1,  3,  2],
    [ 3, -1,  1]
])

# vector b
b = np.array([1, 12, 4])


def Gauss_Jordan(A , b):
    
    # A y b tipo flotante
    A = np.array(A, dtype=float)
    
    b = np.array(b, dtype=float)
    
    # numero de filas
    f = A.shape[0]
    
    # Mostrar matriz Aumentada [A|b]
    print("[A|b] = \n",np.column_stack((A, b)))
    
    # Eliminacion hacia adelante
    for k in range(f - 1):
        
        # verificar que la entrada pivote sea diferente de 0
        if A[k,k] == 0:
            
            
            # separacion
            
            print("----------------------------------------------------------")
            
            # Notificar
            print("Pivote igual a 0 \n")
            
            
            
            # Mostrar A
            print("A = \n",np.column_stack((A, b)))
            
            # Cambiar a la siguiente fila donde el valor no sea cero
            for j in range(k + 1, f):
                
                # Pivote diferente de 0
                if A[j, k] != 0:
                    
                    # Intercambiar la fila actual k con la siguiente fila válida j
                    A[[k, j]] = A[[j, k]]
                    b[[k, j]] = b[[j, k]]
                    
                    # separacion
                    
                    print("----------------------------------------------------------")
                    
                    # Mostrar la operacion realizada
                    print("\n R_",k + 1,"-> <- R_",j + 1," \n")
                    
                    
                    # Mostrar [A|b] despues de la operacion
                    print("\n", np.column_stack((A, b)))
                    
                    # Detener cuando el pivote sea diferente de 0
                    break
                
                else:
                    print("Det(A) =",np.linalg.det(A))
                    raise ValueError("El sistema no tiene solución única.")
                    
                    
        # separacion
        
        print("------------------------------------------------")
                    
        factor = 1/A[k,k]
        
        A[k, :] = A[k, :]* factor
        b[k] = b[k] * factor
        
        print("\n R_",k + 1,"->", factor,"*R_",k + 1,"\n")
        
        print(np.column_stack((A,b)))


        for i in range(k + 1 ,f):
            
            # Determinacion del factor por el que hay que multiplicar
            factor = -A[i,k]
            
            # operacion en A y b
            A[i, k:] =   factor*A[k,k:] + A[i,k:]
            b[i] = factor*b[k] + b[i]
            
            # separacion 
            
            print("--------------------------------------------------")
            
            print("\n R_",i + 1,"->", factor,"*R_",k + 1," + R_",i + 1,"\n")
            
            print("\n",  np.column_stack((A, b)))
            
            
    factor = 1/A[f - 1, f - 1]
    
    A[f - 1, :] = A[ f - 1, :] * factor
    b[f - 1] = b[f - 1] * factor
    
    print("--------------------------------------------------")
    
    print("\n R_",f,"->", factor,"*R_",f,"\n")
    
    print(np.column_stack((A,b)))
    
    
    for k in range(f - 1, 0, -1):
        
        for i in  range(k - 1, -1, -1):
            
            # Determinacion del factor por el que hay que multiplicar
            factor = -A[i,k]
            
            # operacion en A y b
            A[i, k:] =   factor*A[k,k:] + A[i,k:]
            b[i] = factor*b[k] + b[i]
            
            print("--------------------------------------------------")
            
            print("\n R_",i + 1,"->", factor,"*R_",k + 1," + R_",i + 1,"\n")
            
            print(np.column_stack((A,b)))
            
            
    return b


x = Gauss_Jordan(A, b)

x2 = np.linalg.solve(A, b)

print("\n x = ", x)

print("\n x2 = ", x2)

# Crear los valores de x y y
x3 = np.linspace(-2, 5, 50)
y = np.linspace(-2, 6, 50)

X, Y = np.meshgrid(x3, y)

# Despejar z en cada ecuación:
#
# 2x + y - z = 1
Z1 = 2*X + Y - 1

# -x + 3y + 2z = 12
Z2 = (12 + X - 3*Y) / 2

# 3x - y + z = 4
Z3 = 4 - 3*X + Y

# Crear la gráfica tridimensional
fig = plt.figure(figsize=(10, 8))

ax = fig.add_subplot(111, projection="3d")


ax.plot_surface(
    X, Y, Z1,
    color="blue",
    alpha=0.4,
    label=r"$2 x_1 + x_1 - x_3 = 1$"
)

ax.plot_surface(
    X, Y, Z2,
    color="red",
    alpha=0.4,
    label=r"$-x_1 + 3 x_2 + 2 x_3 = 12$"
)

ax.plot_surface(
    X, Y, Z3,
    color="green",
    alpha=0.4,
    label=r"$3 x_1 - x_2 + x_3 = 4$"
)

# Graficar el punto de intersección
ax.scatter(
    x[0],
    x[1],
    x[2],
    color="black",
    s=100,
    label=x)

# Configuración de los ejes
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

ax.set_title("Gauss-Jordan", fontsize=30)

ax.legend(fontsize=20)
