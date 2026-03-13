import numpy as np

# funcion

def Eliminacion_Gaussiana(A,b):

  # matriz de coeficientes
  # en formato flotante
  A = A.astype(float)

  # vector b
  # en formato flotante
  b = b.astype(float)

  # numero de filas

  f = A.shape[0]

  # elininacion hacia delante

  # verificar que el pivote sea diferente de cero
  # si es el caso detener

  for k in range(f - 1):
    if A[k,k] == 0:
       print("pivote igual a 0")
       break

    for i in range(k + 1 ,f):
      factor = A[i,k]/A[k,k]
      A[i, k:] = - factor*A[k,k:] + A[i,k:]
      b[i] = - factor*b[k] + b[i]


     # print("U =",A)

     # print("b'",b)

  # sustitucion hacia atras

  # vector de ceros del tamaño del numero de filas

  x = np.zeros(f)

# inicio de sumatoria en cero
  for i in range(f - 1, -1, -1):
    S = 0

    for j in range(i + 1, f):
      S = S + A[i,j]*x[j]

# asignar entradas al vector cero x

    x[i] = (b[i] - S)/A[i,i]

  return x

# ingresar sistema de ecuaciones
# [A|b]

A = np.array([[2, 1, -1],
              [-1, 3, 2],
              [3, -1, 1]])

b = np.array([1, 12, 4])

print("b =",b)

# evaluacion de la funcion

x = Eliminacion_Gaussiana(A, b)

print("x = ", x)
