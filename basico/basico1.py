import numpy as np

#creamos un array de dimension 1
ar1=np.array([0,1,2,3])
ar2=np.array([[1,2],[3,4]])

print(ar1)
print(ar2)

#miramos la forma
print(ar2.shape) #dos filas y dos columnas
#miramos la dimension
print(ar1.ndim) #dimension 1
print(ar2.ndim) #dimension 2