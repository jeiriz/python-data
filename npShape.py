# The shape of an array is the numbers of items of that dimension, returns a tuple

import numpy as np

# 0 dimension, 4 items
arr = np.array([1,2,3,4])
print(arr.shape)

# 4 dimensiones donde solo 1 tiene 5 items
arr = np.array([1,2,3,4,5],ndmin=3)
print(arr.shape)

# Reshaping
# Changue the dimension o values
arr = np.array([1,2,3,4,5,6])

# Cada valor del parentesis en una dimension nueva
# No se puede reshape cualquier valor, la multiplicacion de los valores del parentesis, debe ser multiplo de la cantidad de items del array
# Reshapea un array de 6 elementos, a 2 arrays de 3 elementos each
print(arr.reshape(2,3))
print("===")
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7,8,9,10,11,12])
# 3 dimensiones (tiene 3 items el reshape), 2 grupos de 3 arrays cada unos
arr2= arr.reshape(2,3,4)
# 2 dimensiones (dos corchetes), 6 arrays de 4 elementos cada uno
arr2= arr.reshape(6,4) #Si en vez de 4, fuera -1, significa que yo no se cual es el valor correspondiente para que complete el multiplo, entonces lo hace automatico
print("Arr2 ",arr2)
print(arr2.ndim)
# Check if the arr2|reshape is a copy o view. In this case, returns the original, so the reshape is a view
print(arr2.base)


# Flat | Aplanar arrays -> convert multimensional into a one dimensional
arrFlat= arr.reshape(-1)
print(arrFlat.ndim)
print(arrFlat)