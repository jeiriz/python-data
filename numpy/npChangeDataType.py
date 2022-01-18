import numpy as np

arr = np.array([1, 2, 3, 4, 5],dtype="S")
print(arr.dtype)

# Crea copia
arrI = arr.astype("I")
print(arrI.dtype)
